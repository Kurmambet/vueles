# C:\projects\vueles\back-vue-sneakers\app\models\product.py
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    imageUrl = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product(id={self.id}, title='{self.title}', price={self.price}, imageUrl={self.imageUrl})>"

