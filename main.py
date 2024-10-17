import requests
from dataclass_wizard import fromdict
from models.api_response import APIResponse

# api-endpoint
URL = "https://dummyjson.com/products"
response = requests.get(URL)
data = response.json()
productList = fromdict(APIResponse, data)
# #print(productList.total)

# for product in productList.products:
#     print(product.title)

