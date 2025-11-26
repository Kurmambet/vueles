# C:\projects\vueles\back-vue-sneakers\app\models\product.py
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from datetime import datetime
from ..database import Base

# class Product(Base):
#     __tablename__ = "products"

#     id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String, nullable=False, index=True)
#     price: Mapped[float] = mapped_column(Float, nullable=False)
#     imageUrl: Mapped[str | None] = mapped_column(String)
#     created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

#     favorite: Mapped["Favorites"] = relationship(back_populates="product", uselist=False)

# from sqlalchemy.orm import Mapped, mapped_column, relationship

# class Favorites(Base):
#     __tablename__ = "favorites"

#     id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     product_id: Mapped[int] = mapped_column(
#         ForeignKey("products.id", ondelete="CASCADE"),
#         unique=True
#     )

#     product: Mapped["Product"] = relationship()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    imageUrl = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Product(id={self.id}, title='{self.title}', price={self.price}, imageUrl={self.imageUrl})>"


class Favorites(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), unique=True)

    def __repr__(self):
        return f"<Favorite(id={self.id}, productId={self.product_id})>"
