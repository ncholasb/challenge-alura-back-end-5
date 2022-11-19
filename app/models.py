import uuid
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, Integer
from .database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    #verified = Column(Boolean, nullable=False, server_default='False')
    #verification_code = Column(String, nullable=True, unique=True)
    #role = Column(String, server_default='user', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


class Videos(Base):
    __tablename__ = 'videos'

    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    url = Column(String, nullable=False)
    categoriaId = Column(String, ForeignKey(
        'categorias.id', ondelete='CASCADE'), nullable=True)
    categoria = relationship('Categorias')


class Categorias(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    titulo = Column(String, nullable=False)
    cor = Column(String, nullable=False)
