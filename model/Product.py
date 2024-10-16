import Dimensions
import Review
import Meta
class Product:
    id : int
    title : str
    description : str
    category : str
    price : float
    discount_percentage : float
    rating: float
    stock:int
    tags:[]
    sku:str
    weight:int
    dimensions: Dimensions
    warranty_information: str
    shipping_information:str
    availabilityStatus:str
    reviews: [Review]
    returnPolicy:str
    minimumOrderQuantity:int
    meta: Meta
    images: []
    thumbnail:str
    brand:None