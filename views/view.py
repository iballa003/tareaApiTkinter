from re import search
from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
from dataclass_wizard import fromdict
from models.api_response import APIResponse
from PIL import ImageTk,Image
import urllib.request
import io

#-----------------------------------------------------------------------------#
#                               Functions                                     #
#-----------------------------------------------------------------------------#
def ImgFromUrl(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image

def changeContent(index):
    title_label.config(text=productLists[index].title)
    image2 = ImgFromUrl(productLists[index].thumbnail)
    image_label.config(image=image2)
    image_label.image=image2
    descripcion_content_label.config(text=productLists[index].description)
    price_content_label.config(text=productLists[index].price)
    rating_content_label.config(text=productLists[productIndex].rating)

def next():
    global productIndex, productLists
    productIndex += 1
    changeContent(productIndex)

def previous():
    global productIndex, productLists
    if(productIndex > 0):
        productIndex -= 1
        changeContent(productIndex)

#-----------------------------------------------------------------------------#
#                               API                                           #
#-----------------------------------------------------------------------------#
URL = "https://dummyjson.com/products"
response = requests.get(URL)
data = response.json()
productsApiRequest = fromdict(APIResponse, data)
#-----------------------------------------------------------------------------#
#                               Tkinter                                       #
#-----------------------------------------------------------------------------#
root = tk.Tk()
root.geometry("512x612")
root.resizable(False,False)
productIndex = 0

productLists = productsApiRequest.products

##--------##Tkinter Search bar##--------##
search_label = ttk.Label(root, text="Buscar:", font='Helvetica 12 bold')
search_label.pack()
search_bar = Entry(root)
search_bar.pack()
Search_string = StringVar(search_bar, "")
search_bar.config(textvariable = Search_string)

##--------##Tkinter Title##--------##
frame_title = Frame(root).pack()
title_label = ttk.Label(frame_title, text=productLists[productIndex].title, font='Helvetica 18 bold')
title_label.pack()
##--------##Image##--------##
image = ImgFromUrl(productLists[productIndex].thumbnail)
image_label = ttk.Label(root, image=image)
image_label.pack()
##--------##Tkinter Description##--------##
frame_description = Frame(root)
frame_description.pack()
descripcion_title_label = ttk.Label(frame_description, text="Descripción", font='Helvetica 12 bold')
descripcion_title_label.pack(anchor="w")
descripcion_content_label = ttk.Label(frame_description, text=productLists[productIndex].description,wraplength=500, justify="left")
descripcion_content_label.pack()
##--------##Tkinter Price##--------##
frame_price = Frame(root).pack()
price_label = tk.Label(root, text="Precio: ", font='Helvetica 11 bold',pady=5).pack(anchor="w")
price_content_label = ttk.Label(frame_price, text=productLists[productIndex].price)
price_content_label.pack(anchor="w")
##--------##Tkinter Rating##--------##
rating_label = tk.Label(root, text="Rating: ", font='Helvetica 11 bold',pady=5).pack(anchor="w")
rating_content_label = ttk.Label(root, text=productLists[productIndex].rating)
rating_content_label.pack(anchor="w")
##--------##Tkinter Buttons##--------##
button_frame = Frame(root)
button_frame.pack()
previous_button = ttk.Button(button_frame,text="Anterior",command=previous)
previous_button.pack(side=LEFT)
next_button = ttk.Button(button_frame,text="Siguiente",command=next)
next_button.pack(side=RIGHT)
##--------##MainLoop##--------##
root.mainloop()