from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..database import Base, get_db
from ..main import app

SQLALCHEMY_DATABASE_URL = "postgresql:///./test.db"

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
# ------------------------ AUTH ------------------------


def test_register():
    response = client.post("/api/auth/register",
                           json={
                               {
                                   "name": "Test User",
                                   "email": "user@example.com",
                                   "password": "testuserpassword",
                                   "passwordConfirm": "testuserpassword"
                               }
                           })
    data = response.json()
    assert data["username"] == "Test User"
    assert data["email"] == "user@example.com"
    assert response.status_code == 200
