#  C:\projects\vueles\back-vue-sneakers\app\repositories\product_repository.py
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.product import Favorites, Product
from ..schemas.product import ProductCreate


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, title: str | None = None, sortBy: str | None = None):
        query = self.db.query(Product)
    
        # фильтрация по title
        if title:
            # заменяем *word* → %word%
            clean = title.replace("*", "%")
            query = query.filter(Product.title.ilike(clean))

        # сортировка
        if sortBy:
            if sortBy.startswith("-"):
                field = sortBy[1:]
                query = query.order_by(desc(getattr(Product, field)))
            else:
                query = query.order_by(asc(getattr(Product, sortBy)))
        return query.all()

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def create(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product



class FavoriteRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Favorites).all()

    def get_by_product_id(self, product_id: int):
        return self.db.query(Favorites).filter(Favorites.product_id == product_id).first()

    def create(self, product_id: int) -> Favorites:
        favorite = Favorites(product_id=product_id)
        self.db.add(favorite)
        self.db.commit()
        self.db.refresh(favorite)
        return favorite


    def get_by_id(self, favorite_id: int):
        return self.db.query(Favorites).filter(Favorites.id == favorite_id).first()

    def delete(self, favorite):
        self.db.delete(favorite)
        self.db.commit()
