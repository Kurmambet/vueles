# C:\projects\vueles\back-vue-sneakers\app\routes\favorites.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_service import FavoriteServise
from ..schemas.product import FavoriteListResponse, FavoriteResponse

router = APIRouter(prefix="/api/favorites", tags=["favorites"])



@router.get("", response_model=FavoriteListResponse)
def get_favorites(db: Session = Depends(get_db)):
    service = FavoriteServise(db)
    return service.get_all_favorites()


@router.post("/{product_id}", response_model=FavoriteResponse)
def add_favorite(product_id: int, db: Session = Depends(get_db)):
    service = FavoriteServise(db)
    return service.add_to_favorites(product_id)

