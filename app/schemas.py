from datetime import datetime
from typing import List, Optional
import uuid
from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=6)
    passwordConfirm: str


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class FilteredUserResponse(UserBaseSchema):
    id: uuid.UUID


class VideoBaseSchema(BaseModel):
    titulo: str
    descricao: str
    url: str
    categoriaId:  str | None = "1"

    class Config:
        orm_mode = True


class UpdateVideoSchema(BaseModel):
    titulo: str
    descricao: str
    url: str
    categoriaId: str | None = "1"

    class Config:
        orm_mode = True


class UpdateCategoriaSchema(BaseModel):
    titulo: str
    cor: str

    class Config:
        orm_mode = True


class VideoResponse(VideoBaseSchema):
    id: int
    titulo: str
    descricao: str
    url: str


class ListVideoResponse(BaseModel):
    status: str
    results: int
    videos: List[VideoResponse]


class CategoriaBaseSchema(BaseModel):
    id: int
    titulo: str
    cor: str

    class Config:
        orm_mode = True


class CategoriaResponse(CategoriaBaseSchema):
    id: int
    titulo: str
    cor: str


class ListCategoriaResponse(BaseModel):
    status: str
    results: int
    categorias: List[CategoriaResponse]


class CreateCategoriaSchema(BaseModel):
    titulo: str
    cor: str


class CreateCategoriaDefaultSchema (CategoriaBaseSchema):
    id: int
