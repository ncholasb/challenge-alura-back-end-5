from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import videos, categorias, user, auth
from app.database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(
    title="Challenge Backend 5 - Alura: FastAPI + Postgres (docker)"
)

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, tags=['Auth'], prefix='/api/auth')
app.include_router(user.router, tags=['Users'], prefix='/api/users')
app.include_router(videos.router, tags=['Videos'], prefix='/api')
app.include_router(categorias.router, tags=['categorias'], prefix='/api')


@app.get('/')
async def docs_redirect():
    return RedirectResponse(url='/docs')
