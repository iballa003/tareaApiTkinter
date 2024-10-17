from dataclasses import dataclass

from models.Product import Product
@dataclass
class APIResponse:
    products: list[Product]
    total: int
    skip: int
    limit: int