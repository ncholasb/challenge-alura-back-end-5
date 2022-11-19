from fastapi import APIRouter, Depends, HTTPException,  status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from datetime import datetime
from app.oauth2 import require_user


router = APIRouter()


@router.get('/categorias', response_model=schemas.ListCategoriaResponse)
async def get_categorias(db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    categorias = db.query(models.Categorias).group_by(models.Categorias.id).all()
    return {'status': 'success', 'results': len(categorias), 'categorias': categorias}


@router.get('/categorias/{id}')
async def get_categorias_by_id(id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    categoria = db.query(models.Categorias).filter(models.Categorias.id == id).first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No categoria with this id: {id} found")
    return categoria


@router.post("/categorias")
async def post_categorias(categoria: schemas.CreateCategoriaSchema, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    if categoria.titulo == "":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="O campo TÍTULO é obrigatório")

    if categoria.cor == "":
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="O campo COR é obrigatório")

    if categoria.cor != "" or categoria.titulo != "":
        new_categoria = models.Categorias(**categoria.dict())
        db.add(new_categoria)
        db.commit()
        db.refresh(new_categoria)
        return new_categoria


@router.put('/categorias/{id}')
async def put_categorias(id: str, categoria: schemas.UpdateCategoriaSchema, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    categoria_query = db.query(models.Categorias).filter(models.Categorias.id == id)
    db_categoria = categoria_query.first()

    if not db_categoria:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No categoria with this id: {id} found')

    categoria_query.update(categoria.dict(exclude_none=True), synchronize_session=False)
    db.commit()
    return db_categoria


@router.delete('/categorias/{id}')
def delete_categoria(id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    categoria_query = db.query(models.Categorias).filter(models.Categorias.id == id)
    categoria = categoria_query.first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No categoria with this id: {id} found')
    categoria_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/categorias/{id}/videos', response_model=schemas.ListVideoResponse)
def get_videos_by_category(id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    categoria_videos_query = db.query(models.Videos).filter(
        models.Videos.categoriaId == id).all()

    if not categoria_videos_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No categoria with this id: {id} found")

    return {'status': 'success', 'results': len(categoria_videos_query), 'videos': categoria_videos_query}
