# backend/seed_data.py
import sys
import os

# Если запускаешь не как модуль — раскомментируй эти 3 строки:
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))
# from app.database import SessionLocal, init_db

from app.database import SessionLocal, init_db
from app.models.product import Product

products_data = [
    {"title": "Мужские Кроссовки Nike Blazer Mid Suede", "price": 12999, "imageUrl": "/sneakers/sneakers-1.jpg"},
    {"title": "Мужские Кроссовки Nike Air Max 270", "price": 15600, "imageUrl": "/sneakers/sneakers-2.jpg"},
    {"title": "Мужские Кроссовки Nike Blazer Mid Suede", "price": 8499, "imageUrl": "/sneakers/sneakers-3.jpg"},
    {"title": "Кроссовки Puma X Aka Boku Future Rider", "price": 7800, "imageUrl": "/sneakers/sneakers-4.jpg"},
    {"title": "Кроссовки Future Rider", "price": 9550, "imageUrl": "/sneakers/sneakers-5.jpg"},
    {"title": "Кроссовки Black Edition", "price": 16999, "imageUrl": "/sneakers/sneakers-6.jpg"},
    {"title": "Кроссовки Orange Boomb Edition", "price": 7499, "imageUrl": "/sneakers/sneakers-7.jpg"},
    {"title": "Кроссовки Nike Air Max 270", "price": 15600, "imageUrl": "/sneakers/sneakers-8.jpg"},
    {"title": "Кроссовки Nike Air Force 1", "price": 5900, "imageUrl": "/sneakers/sneakers-9.jpg"},
    {"title": "Кроссовки Adidas Ultraboost", "price": 11500, "imageUrl": "/sneakers/sneakers-10.jpg"},
    {"title": "Кроссовки Puma Clyde All-Pro", "price": 7600, "imageUrl": "/sneakers/sneakers-11.jpg"},
    {"title": "Кроссовки Converse Chuck Taylor All-Star", "price": 13000, "imageUrl": "/sneakers/sneakers-12.jpg"},
]

def create_products(db):
    existing = db.query(Product).count()
    if existing > 0:
        print(f"Уже есть {existing} товаров, пропускаю создание.")
        return

    for data in products_data:
        product = Product(**data)
        db.add(product)
    
    db.commit()
    print(f"Создано {len(products_data)} товаров")

def seed_database():
    print("Начинаем заполнение базы тестовыми данными...")
    init_db()
    db = SessionLocal()
    try:
        create_products(db)
        print("Готово! База заполнена.")
    except Exception as e:
        print(f"Ошибка: {e}")
        db.rollback()
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
