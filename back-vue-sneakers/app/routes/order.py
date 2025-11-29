# C:\projects\vueles\back-vue-sneakers\app\routes\cart.py
from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.product_service import OrderService
from ..schemas.product import OrderCreate, OrderResponse, OrderListResponse

router = APIRouter(prefix="/api/orders", tags=["orders"])


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(request: OrderCreate, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.create_order(request)


@router.get("", response_model=OrderListResponse, status_code=status.HTTP_200_OK)
def get_orders(db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.get_all_orders()


@router.get("/{order_id}", response_model=OrderResponse, status_code=status.HTTP_200_OK)
def get_order(order_id: int, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.get_order_by_id(order_id)

@router.delete(
    "/{order_id}",
    response_model=OrderResponse,
    status_code=status.HTTP_200_OK,
)
def delete_order(order_id: int = Path(...), db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.delete_order(order_id)
