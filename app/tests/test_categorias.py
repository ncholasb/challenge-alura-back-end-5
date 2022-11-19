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
# ------------------------ CATEGORIAS ------------------------


def test_post_categorias():
    response = client.post("/api/categorias",
                           json={
                               "titulo": "teste titulo",
                               "cor": "teste cor"
                           })
    assert response.status_code == 200


def test_put_categoria():
    create = client.post("/api/categorias",
                         json={
                             "titulo": "2 teste titulo",
                             "cor": "2 teste cor"
                         })
    assert create.status_code == 200

    update = client.put("/api/categorias/2",
                        json={
                            "titulo": "update teste titulo",
                            "cor": "update teste cor"
                        })
    assert update.status_code == 200

    confirm = client.get("/api/categorias/2")
    assert confirm.status_code == 200
    assert confirm.json() == {
        "cor": "update teste cor",
        "id": 2,
        "titulo": "update teste titulo"
    }


def test_get_categorias():
    response = client.get("/api/categorias")
    assert response.status_code == 200
    data = response.json()
    assert data["categorias"][0] == {
        "titulo": "teste titulo",
        "id": 1,
        "cor": "teste cor"
    }


def test_get_categoria_id():
    response = client.get("/api/categorias/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "titulo": "teste titulo",
        "cor": "teste cor"
    }


def test_delete_categoria():
    response = client.delete("/api/categorias/1")
    assert response.status_code == 204
