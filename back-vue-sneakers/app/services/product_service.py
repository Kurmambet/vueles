#  C:\projects\vueles\back-vue-sneakers\app\services\product_service.py
from sqlalchemy.orm import Session
from typing import List
from ..repositories.product_repository import ProductRepository, FavoriteRepository
from ..schemas.product import FavoriteListResponse, FavoriteResponse, ProductResponse, ProductListResponse, ProductCreate
from fastapi import HTTPException, status


class ProductService:
    def __init__(self, db: Session):
        self.product_repository = ProductRepository(db)

    def get_all_products(self, title: str | None, sortBy: str | None) -> ProductListResponse:
        products = self.product_repository.get_all(title=title, sortBy=sortBy)
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        return ProductListResponse(
            products=products_response, total=len(products_response)
        )

    def get_product_by_id(self, product_id: int) -> ProductResponse:
        product = self.product_repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with id {product_id} not found",
            )
        return ProductResponse.model_validate(product)

    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        product = self.product_repository.create(product_data)
        return ProductResponse.model_validate(product)



class FavoriteServise:
    def __init__(self, db: Session):
        self.favorite_repository = FavoriteRepository(db)

    def get_all_favorites(self) -> FavoriteListResponse:
        favorites = self.favorite_repository.get_all()
        favorites_response = [FavoriteResponse.model_validate(fav) for fav in favorites]
        return FavoriteListResponse(favorites=favorites_response)

    def add_to_favorites(self, product_id: int) -> FavoriteResponse:
        # Проверка: не добавили ли уже этот товар
        existing = self.favorite_repository.get_by_product_id(product_id)
        if existing:
            return FavoriteResponse.model_validate(existing)

        # Создаём запись
        favorite = self.favorite_repository.create(product_id)
        return FavoriteResponse.model_validate(favorite)
