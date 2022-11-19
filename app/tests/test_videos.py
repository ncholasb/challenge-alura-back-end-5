from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base, get_db
from ..main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# ------------------------ TESTES ------------------------
# ------------------------ VIDEOS ------------------------


def test_post_videos_com_categoria():
    response = client.post("/api/videos",
                           json={
                               "titulo": "Teste titulo",
                               "descricao": "Teste descricao",
                               "url": "google.com",
                               "categoriaId": "1"
                           })
    assert response.status_code == 200
    response2 = client.post("/api/videos",
                            json={
                                "titulo": "2 Teste titulo",
                                "descricao": "2 Teste descricao",
                                "url": "2 google.com",
                                "categoriaId": "1"
                            })
    assert response2.status_code == 200
    response3 = client.post("/api/videos",
                            json={
                                "titulo": "3 Teste titulo",
                                "descricao": "3 Teste descricao",
                                "url": "3 google.com",
                                "categoriaId": "1"
                            })
    assert response3.status_code == 200


def test_put_categoria():
    update = client.put("/api/videos/2",
                        json={
                            "titulo": "update Teste titulo",
                            "descricao": "update Teste descricao",
                            "url": "update google.com",
                            "categoriaId": "2"
                        })
    assert update.status_code == 200

    confirm = client.get("/api/videos/2")
    assert confirm.status_code == 200
    assert confirm.json() == {'id': 2,
                              'url': 'update google.com',
                              'descricao': 'update Teste descricao',
                              'titulo': 'update Teste titulo',
                              'categoriaId': '2'
                              }


def test_post_videos_sem_categoria():
    response = client.post("/api/videos",
                           json={
                               "titulo": "2 Teste titulo",
                               "descricao": "2 Teste descricao",
                               "url": "2 google.com",
                               "categoriaId": ""
                           })
    assert response.status_code == 200


def test_get_videos():
    response = client.get("/api/videos")
    assert response.status_code == 200
    data = response.json()
    assert data["videos"][0] == {
        "titulo": "Teste titulo",
        "descricao": "Teste descricao",
        "url": "google.com",
        "categoriaId": "1",
        "id": 1
    }


def test_search_video():
    response = client.get("/api/videos/?search=titulo")
    assert response.status_code == 200
    data = response.json()
    assert len(data['videos']) > 0


def test_get_videos_by_categoryID():
    response = client.get("/api/categorias/1/videos")
    assert response.status_code == 200
    data = response.json()
    assert len(data['videos']) > 0


def test_get_videos_by_id():
    response = client.get("/api/videos/1")
    assert response.status_code == 200
    assert response.json() == {
        "titulo": "Teste titulo",
        "descricao": "Teste descricao",
        "url": "google.com",
        "categoriaId": "1",
        "id": 1
    }


def test_delete_video():
    response = client.delete("/api/videos/3")
    assert response.status_code == 204
