from tkinter import *
from tkinter import ttk
import tkinter as tk

from PIL import ImageTk,Image

import main as productResponse
import urllib.request
import io

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

def next():
    global productIndex, productLists
    productIndex += 1
    changeContent(productIndex)

def previous():
    global productIndex, productLists
    if(productIndex > 0):
        productIndex -= 1
        changeContent(productIndex)


    #-----------------------------------------------------------------------------
    # for product in productObjects.productList.products:
    #     ttk.Label(root, text=product.title).pack()


root = tk.Tk()
root.geometry("512x612")
root.resizable(False,False)
productIndex = 0

productLists = productResponse.productList.products

#-------------------------------------------------------------------#Title
frame_title = Frame(root).pack()
title_label = tk.Label(frame_title, text=productLists[productIndex].title, font='Helvetica 18 bold')
title_label.pack()
#-------------------------------------------------------------------#Image
image = ImgFromUrl(productLists[productIndex].thumbnail)
image_label = tk.Label(root, image=image)
image_label.pack()
#-------------------------------------------------------------------#Description
frame_description = Frame(root).pack()
descripcion_title_label = tk.Label(frame_description, text="Descripción", font='Helvetica 12 bold').pack(anchor="w")
descripcion_content_label = tk.Label(frame_description, text=productLists[productIndex].description,wraplength=500, justify="left")
descripcion_content_label.pack()
#-------------------------------------------------------------------#Price
price_label = tk.Label(root, text="Precio: ", font='Helvetica 11 bold',pady=5).pack(anchor="w")
price_content_label = tk.Label(root, text=productLists[productIndex].price)
price_content_label.pack(anchor="w")
#-------------------------------------------------------------------#Buttons
button_frame = Frame(root).pack()
previous_button = tk.Button(button_frame,text="Anterior",command=previous).pack(side=LEFT)
next_button = tk.Button(button_frame,text="Siguiente",command=next).pack(side=RIGHT)
#-------------------------------------------------------------------#MainLoop
root.mainloop()