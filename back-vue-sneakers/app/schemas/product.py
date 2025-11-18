# C:\projects\vueles\back-vue-sneakers\app\schemas\product.py
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=200, description="Product name")

    price: float = Field(..., gt=0, description="Product price(must be greater than 0")

    imageUrl: Optional[str] = Field(None, description="Product image URL")


class ProductCreate(ProductBase):
    pass


class ProductResponse(BaseModel):
    id: int = Field(..., description="Unique product ID")
    title: str
    price: float
    imageUrl: Optional[str]

    class Config:
        from_attributes = True


class ProductListResponse(BaseModel):
    products: list[ProductResponse]
    total: int = Field(..., description="Total number of products")
