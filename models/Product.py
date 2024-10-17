from dataclasses import dataclass

from models.Dimensions import Dimensions
from models.Review import Review
from models.Meta import Meta

from typing import Optional
@dataclass
class Product:
    id: int
    title: str
    description: str
    category: str
    price: float
    discount_percentage: float
    rating: float
    stock: int
    tags: list[str]
    sku: str
    weight: int
    dimensions: Dimensions
    warranty_information: str
    shipping_information: str
    availability_status: str
    reviews: list[Review]
    return_policy: str
    minimum_order_quantity: int
    meta: Meta
    images: list[str]
    thumbnail: str
    brand: Optional[str] = None