from fastapi import APIRouter, Depends, HTTPException,  status, Response
from sqlalchemy import func
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models
from datetime import datetime
from app.oauth2 import require_user


router = APIRouter()


@router.get('/videos', response_model=schemas.ListVideoResponse)
async def get_videos(db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    videos = db.query(models.Videos).group_by(models.Videos.id).all()
    return {'status': 'success', 'results': len(videos), 'videos': videos}


@router.get('/videos/{id}')
async def get_videos_by_id(id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    video = db.query(models.Videos).filter(models.Videos.id == id).first()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No video with this id: {id} found")
    return video


@router.post("/videos")
async def post_videos(video: schemas.VideoBaseSchema, db: Session = Depends(get_db), user_id: str = Depends(require_user)):
    if video.categoriaId == "":
        video.categoriaId = "1"

    new_video = models.Videos(**video.dict())

    db.add(new_video)
    db.commit()
    db.refresh(new_video)
    return new_video


@router.put('/videos/{id}')
async def put_videos(id: str, video: schemas.UpdateVideoSchema, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    video_query = db.query(models.Videos).filter(models.Videos.id == id)
    db_video = video_query.first()

    if not db_video:
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'No video with this id: {id} found')

    video_query.update(video.dict(exclude_none=True), synchronize_session=False)
    db.commit()
    return db_video


@router.delete('/videos/{id}')
def delete_video(id: str, db: Session = Depends(get_db), user_id: str = Depends(require_user)):

    video_query = db.query(models.Videos).filter(models.Videos.id == id)
    video = video_query.first()
    if not video:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No video with this id: {id} found')
    video_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/videos/?search={search}', response_model=schemas.ListVideoResponse)
def get_videos_search(db: Session = Depends(get_db), search: str = '', user_id: str = Depends(require_user)):
    videos = db.query(models.Videos).group_by(models.Videos.id).filter(models.Videos.titulo.ilike(f"%{search}%")).all()

    return {'status': 'success', 'results': len(videos), 'videos': videos}
