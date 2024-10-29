from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter as tk
import requests
from dataclass_wizard import fromdict
from weasyprint import HTML

from models.Product import Product
from models.Empresa import Empresa
from models.api_response import APIResponse
from PIL import ImageTk,Image
import urllib.request
import io
from typing import List

#-----------------------------------------------------------------------------#
#                               Functions                                     #
#-----------------------------------------------------------------------------#
def img_from_url(url):
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    image = ImageTk.PhotoImage(im)
    return image

def search():
    global product_lists
    coincidences = filter(check_coincidences, product_lists)
    coincidences_list = list(coincidences)
    coincidences_list.sort(key=lambda x: x.title)
    openNewWindow(coincidences_list)

def generate_products_pdf(productos: List[Product]):
    empresa: Empresa = Empresa(
        nombre="Iballa Tech",
        titular="Iballatech Industries Montero",
        cif="12345678",
        direccion="Calel",
        email="hola@iballa.com",
    )
    current_date = datetime.now()
    format_date = current_date.strftime("%Y-%m-%d-%H:%M")
    pdf_content = """
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8" />
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                } 
                .logo img {
                    width:200px; 
                    height:200px;
                }
                header {
                    display: flex;
                    justify-content: space-between;
                }
                .infoEmpresa {
                    display: flex;
                    flex-direction: column;
                }
                .fotoProducto {
                    width: 100px;
                }
                td {
                    padding: 10px;
                }
                .precio {
                    color: red;
                }
                .indice {
                    font-size: 25px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
        <header>
                <div class='logo'>
                    <img src='./img/logo.jpg'/>
                </div>
                <div class='infoEmpresa'>
                    <p>""" + empresa.nombre + """</p>
                    <p>""" + empresa.titular + """</p>
                    <p>""" + empresa.cif + """</p>
                    <p>""" + empresa.direccion + """</p>
                    <p>""" + empresa.email + """</p>
                    <p>""" + format_date + """</p>
                </div>
            </header>
            <br>
            <hr><hr>
            <h1>Productos</h1>
    """
    index = 0
    for producto in productos:
        index += 1
        pdf_content += """
                    <table>
                        <tr>
                            <td class= 'indice'>""" + str(index) + """</td>
                            <td><img class='fotoProducto' src='""" + producto.thumbnail + """'/></td>
                            <td>""" + producto.title + """</td>
                            <td>""" + producto.category + """</td>
                            <td class='precio'>""" + str(producto.price) + """</td>
                        </tr>
                    </table>
                """
    pdf_content += """
        </body>
        </html>
        """
    htmldoc = HTML(string=pdf_content)
    htmldoc.write_pdf(target=f"busqueda_resultado_{format_date}.pdf")

def check_coincidences(e):
    search_bar_content = search_bar.get()
    if (search_bar_content.lower() in e.title.lower() or search_bar_content.lower() in e.category.lower()) and search_bar_content != "":
        return True

def change_content(index):
    title_label.config(text=product_lists[index].title)
    image2 = img_from_url(product_lists[index].thumbnail)
    image_label.config(image=image2)
    image_label.image=image2
    category_label.config(text=product_lists[index].category)
    descripcion_content_label.config(text=product_lists[index].description)
    price_content_label.config(text=product_lists[index].price)
    rating_content_label.config(text=product_lists[product_index].rating)


def openNewWindow(products_list):
    new_window = Toplevel(root)
    new_window.title("Coincidencias")
    if len(products_list) > 0:
        Label(new_window,text="Productos encontrados:",font='Helvetica 18 bold').pack()
        for producto in products_list:
            Label(new_window,
              text=producto.title).pack()
        genertate_pdf_button = ttk.Button(new_window, text="Generar PDF",padding=10, command=lambda: generate_products_pdf(products_list))
        genertate_pdf_button.pack(padx=10, pady=10)
    else:
        Label(new_window,
              text="No se han encontrado productos").pack()

def next():
    global product_index, product_lists
    product_index += 1
    change_content(product_index)

def previous():
    global product_index, product_lists
    if(product_index > 0):
        product_index -= 1
        change_content(product_index)

#-----------------------------------------------------------------------------#
#                               API                                           #
#-----------------------------------------------------------------------------#
URL = "https://dummyjson.com/products"
response = requests.get(URL)
data = response.json()
products_api_request = fromdict(APIResponse, data)
#-----------------------------------------------------------------------------#
#                               Tkinter                                       #
#-----------------------------------------------------------------------------#
root = tk.Tk()
#root.geometry("512x612")
root.resizable(False,False)
product_index = 0
style = ttk.Style()
style.configure("FrameTitle", background="red")
product_lists = products_api_request.products
##--------##Tkinter Search bar##--------##
search_label = ttk.Label(root, text="Buscar:", font='Helvetica 12 bold')
search_label.grid(row=0,column=2,sticky=W)
search_bar = Entry(root)
search_bar.grid(row=0, column=3,sticky=W)
#label1 = ttk.Label(root, text=" ", font='Helvetica 12 bold').grid(row=0,column=4)
Search_string = StringVar(search_bar, "")
search_button = ttk.Button(root,text="Buscar",command=search)
search_button.grid(row=0, column=4,sticky=W)
##--------##Tkinter Title##--------##

title_label = ttk.Label(root, text=product_lists[product_index].title, font='Helvetica 18 bold')
title_label.grid()
##--------##Image##--------##
image = img_from_url(product_lists[product_index].thumbnail)
image_label = ttk.Label(root, image=image)
image_label.grid()
##--------##Tkinter Category##--------##
category_title_label = ttk.Label(root, text="Categoría", font='Helvetica 12 bold')
category_title_label.grid()
category_label = ttk.Label(root, text=product_lists[product_index].category)
category_label.grid()
##--------##Tkinter Description##--------##
frame_description = Frame(root)
frame_description.grid()
descripcion_title_label = ttk.Label(frame_description, text="Descripción", font='Helvetica 12 bold')
descripcion_title_label.grid()
descripcion_content_label = ttk.Label(frame_description, text=product_lists[product_index].description, wraplength=500, justify="left")
descripcion_content_label.grid()
##--------##Tkinter Price##--------##
frame_price = Frame(root).grid()
price_label = tk.Label(root, text="Precio: ", font='Helvetica 11 bold',pady=5).grid()
price_content_label = ttk.Label(frame_price, text=product_lists[product_index].price)
price_content_label.grid()
##--------##Tkinter Rating##--------##
rating_label = tk.Label(root, text="Rating: ", font='Helvetica 11 bold',pady=5).grid()
rating_content_label = ttk.Label(root, text=product_lists[product_index].rating)
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