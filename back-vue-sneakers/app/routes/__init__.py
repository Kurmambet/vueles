from .products import router as products_router
from .favorites import router as favorites_router
from .order import router as orders_router

__all__ = ["products_router", "favorites_router", "orders_router"]
