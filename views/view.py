from tkinter import *
from tkinter import ttk
import tkinter as tk
import main as productObjects
import requests
from dataclass_wizard import fromdict

from models.api_response import APIResponse



def mostrarLista():
    # URL = "https://dummyjson.com/products"
    # response = requests.get(URL)
    # data = response.json()
    # productList = fromdict(APIResponse, data)
    for product in productObjects.productList.products:
        ttk.Label(root, text=product.title).pack()


root = tk.Tk()
root.geometry("512x700")
root.resizable(False,False)
mostrarLista()
root.mainloop()