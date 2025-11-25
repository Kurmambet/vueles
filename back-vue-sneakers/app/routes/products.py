# C:\projects\vueles\back-vue-sneakers\app\routes\products.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_service import ProductService
from ..schemas.product import ProductResponse, ProductListResponse

router = APIRouter(prefix="/api/products", tags=["products"])


@router.get("", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products(title: str | None = None,
                 sortBy: str | None = None,
                 db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_all_products(title=title, sortBy=sortBy)


@router.get(
    "/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK
)
def get_product(product_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_product_by_id(product_id)


