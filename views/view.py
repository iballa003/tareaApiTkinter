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

def search():
    global productLists
    coincidences = filter(check_coincidences, productLists)
    coincidences_list = list(coincidences)
    titles = []
    if len(coincidences_list) > 0:
        for x in coincidences_list:
            titles.append(x.title)
    print(titles)
    openNewWindow(titles)

def check_coincidences(e):
    search_bar_content = search_bar.get()
    if (search_bar_content.lower() in e.title.lower() or search_bar_content.lower() in e.category.lower()) and search_bar_content != "":
        return True

def changeContent(index):
    title_label.config(text=productLists[index].title)
    image2 = ImgFromUrl(productLists[index].thumbnail)
    image_label.config(image=image2)
    image_label.image=image2
    category_label.config(text=productLists[index].category)
    descripcion_content_label.config(text=productLists[index].description)
    price_content_label.config(text=productLists[index].price)
    rating_content_label.config(text=productLists[productIndex].rating)


def openNewWindow(productos):
    newWindow = Toplevel(root)
    newWindow.title("Coincidencias")
    newWindow.geometry("280x500")
    if len(productos) > 0:
        Label(newWindow,text="Productos encontrados:",font='Helvetica 18 bold').pack()
        for producto in productos:
            Label(newWindow,
              text=producto).pack()
    else:
        Label(newWindow,
              text="No se han encontrado productos").pack()
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
#root.geometry("512x612")
root.resizable(False,False)
productIndex = 0
style = ttk.Style()
style.configure("FrameTitle", background="red")
productLists = productsApiRequest.products
##--------##Tkinter Search bar##--------##
search_label = ttk.Label(root, text="Buscar:", font='Helvetica 12 bold')
search_label.grid(row=0,column=2,sticky=W)
search_bar = Entry(root)
search_bar.grid(row=0, column=3,sticky=W)
#label1 = ttk.Label(root, text=" ", font='Helvetica 12 bold').grid(row=0,column=4)
Search_string = StringVar(search_bar, "")
search_bar.config(textvariable = productLists[productIndex].title)
search_button = ttk.Button(root,text="Buscar",command=search)
search_button.grid(row=0, column=4,sticky=W)
##--------##Tkinter Title##--------##

title_label = ttk.Label(root, text=productLists[productIndex].title, font='Helvetica 18 bold')
title_label.grid()
##--------##Image##--------##
image = ImgFromUrl(productLists[productIndex].thumbnail)
image_label = ttk.Label(root, image=image)
image_label.grid()
##--------##Tkinter Category##--------##
category_title_label = ttk.Label(root, text="Categoría", font='Helvetica 12 bold')
category_title_label.grid()
category_label = ttk.Label(root, text=productLists[productIndex].category)
category_label.grid()
##--------##Tkinter Description##--------##
frame_description = Frame(root)
frame_description.grid()
descripcion_title_label = ttk.Label(frame_description, text="Descripción", font='Helvetica 12 bold')
descripcion_title_label.grid()
descripcion_content_label = ttk.Label(frame_description, text=productLists[productIndex].description,wraplength=500, justify="left")
descripcion_content_label.grid()
##--------##Tkinter Price##--------##
frame_price = Frame(root).grid()
price_label = tk.Label(root, text="Precio: ", font='Helvetica 11 bold',pady=5).grid()
price_content_label = ttk.Label(frame_price, text=productLists[productIndex].price)
price_content_label.grid()
##--------##Tkinter Rating##--------##
rating_label = tk.Label(root, text="Rating: ", font='Helvetica 11 bold',pady=5).grid()
rating_content_label = ttk.Label(root, text=productLists[productIndex].rating)
rating_content_label.grid()
##--------##Tkinter Buttons##--------##
button_frame = Frame(root)
button_frame.grid()
previous_button = ttk.Button(button_frame,text="Anterior",command=previous)
previous_button.grid()
next_button = ttk.Button(button_frame,text="Siguiente",command=next)
next_button.grid()
##--------##MainLoop##--------##
root.mainloop()