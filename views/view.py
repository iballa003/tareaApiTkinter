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

def next():
    print("test")
    global productResponse, productIndex, title_label

    title_label.config(text=productResponse.productList.products[productIndex].title)

    productIndex += 1
    print(productIndex)

def previous():
    print("test")


    #-----------------------------------------------------------------------------
    # for product in productObjects.productList.products:
    #     ttk.Label(root, text=product.title).pack()


root = tk.Tk()
root.geometry("512x612")
root.resizable(False,False)
productIndex = 0


#-------------------------------------------------------------------#Title
frame_title = Frame(root).pack()
title_label = tk.Label(frame_title, text=productResponse.productList.products[productIndex].title, font='Helvetica 18 bold')
title_label.pack()
#-------------------------------------------------------------------#Image
image = ImgFromUrl(productResponse.productList.products[productIndex].thumbnail)
image_label = tk.Label(root, image=image)
image_label.pack()
#-------------------------------------------------------------------#Description
frame_description = Frame(root).pack()
descripcion_title_label = tk.Label(frame_description, text="Descripción", font='Helvetica 12 bold').pack(anchor="w")
descripcion_content_label = tk.Label(frame_description, text=productResponse.productList.products[productIndex].description,wraplength=500, justify="left").pack()
#-------------------------------------------------------------------#Price
price_label = tk.Label(root, text="Precio: ", font='Helvetica 11 bold',pady=5).pack(anchor="w")
price_content_label = tk.Label(root, text=productResponse.productList.products[productIndex].price).pack(anchor="w")
#-------------------------------------------------------------------#Buttons
button_frame = Frame(root).pack()
previous_button = tk.Button(button_frame,text="Anterior",command=previous).pack(side=LEFT)
next_button = tk.Button(button_frame,text="Siguiente",command=next).pack(side=RIGHT)
#-------------------------------------------------------------------#MainLoop
root.mainloop()