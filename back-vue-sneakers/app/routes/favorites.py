# C:\projects\vueles\back-vue-sneakers\app\routes\favorites.py
from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_service import FavoriteServise
from ..schemas.product import FavoriteListResponse, FavoriteResponse
from pydantic import BaseModel

router = APIRouter(prefix="/api/favorites", tags=["favorites"])





@router.get("", response_model=FavoriteListResponse)
def get_favorites(db: Session = Depends(get_db)):
    service = FavoriteServise(db)
    return service.get_all_favorites()

class FavoriteRequest(BaseModel):
    product_id: int


@router.post("", response_model=FavoriteResponse)
def add_favorite(request: FavoriteRequest, db: Session = Depends(get_db)):
    service = FavoriteServise(db)
    return service.add_to_favorites(request.product_id)



@router.delete("/{favorite_id}", response_model=FavoriteResponse)
def delete_favorite(favorite_id: int = Path(...), db: Session = Depends(get_db)):
    service = FavoriteServise(db)
    return service.delete_favorite(favorite_id)
