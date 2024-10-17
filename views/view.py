from tkinter import *
from tkinter import ttk
import tkinter as tk

from PIL import ImageTk,Image

import main as productObjects
import urllib.request
import io

def ImgFromUrl(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image



    #-----------------------------------------------------------------------------
    # for product in productObjects.productList.products:
    #     ttk.Label(root, text=product.title).pack()


root = tk.Tk()
root.geometry("512x700")
root.resizable(False,False)
image = ImgFromUrl(productObjects.productList.products[0].thumbnail)
label1 = tk.Label(root, text=productObjects.productList.products[0].title, font='Helvetica 18 bold').pack()
label2 = tk.Label(root, image=image)
label2.pack()
label3 = tk.Label(root, text="Descripción", font='Helvetica 15 bold').pack()
label3 = tk.Label(root, text=productObjects.productList.products[0].description).pack()
root.mainloop()