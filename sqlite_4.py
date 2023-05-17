import sqlite3
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkbs

connection = sqlite3.connect('antmebas.db')
cursor = connection.cursor()

def kuvatud_andmed(valitud_arv):
    for i in treeview.get_children():
        treeview.delete(i)

    cursor.execute('SELECT * FROM kkotter')
    andmed = cursor.fetchmany(valitud_arv)

    for rida in andmed:
        treeview.insert('', 'end', values=rida)

def otsi_andmeid():
    otsingusõna = otsing_sisend.get()
    cursor.execute("SELECT * FROM kkotter WHERE car_make LIKE ? OR car_model LIKE ?", ('%'+otsingusõna+'%', '%'+otsingusõna+'%'))
    andmed = cursor.fetchall()

    for i in treeview.get_children():
        treeview.delete(i)

    for rida in andmed:
        treeview.insert('', 'end', values=rida)

def lisa_andmed():
    first_name = first_name_sisend.get()
    last_name = last_name_sisend.get()
    email = email_sisend.get()
    car_make = car_make_sisend.get()
    car_model = car_model_sisend.get()
    car_year = car_year_sisend.get()
    car_price = car_price_sisend.get()

    cursor.execute("INSERT INTO kkotter (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, email, car_make, car_model, car_year, car_price))
    connection.commit()

    kuvatud_andmed(int(valik_var.get()))

def kustuta_rida():
    valitud_rida = treeview.focus()
    if valitud_rida:
        rida_info = treeview.item(valitud_rida)['values']
        cursor.execute("DELETE FROM kkotter WHERE ID=?", (rida_info[0],))
        connection.commit()
        treeview.delete(valitud_rida)

def muuda_teemavarvi():
    if style.theme_use() == 'vapor':
        style.theme_use('litera')
    else:
        style.theme_use('vapor')

root = tk.Tk()
root.title("Andmete kuvamine")
root.attributes('-fullscreen', True)

style = ttkbs.Style(theme='vapor')

valik_var = tk.StringVar()
valik_var.set("5")

valikukast = ttk.Combobox(root, textvariable=valik_var, values=["5", "10", "20", "30", "1000"])
valikukast.pack(pady=10)

nupp = ttk.Button(root, text="Kuva andmed", command=lambda: kuvatud_andmed(int(valik_var.get())))
nupp.pack(pady=10)

otsing_sisend = ttk.Entry(root)
otsing_sisend.insert(tk.END, "Otsing")
otsing_sisend.pack(pady=10)

sisestuse_raam = ttk.Frame(root)
sisestuse_raam.pack(pady=10)

first_name_sisend = ttk.Entry(sisestuse_raam)
first_name_sisend.insert(tk.END, "Eesnimi")
first_name_sisend.pack(side=tk.LEFT, padx=5)

last_name_sisend = ttk.Entry(sisestuse_raam)
last_name_sisend.insert(tk.END, "Perekonnanimi")
last_name_sisend.pack(side=tk.LEFT, padx=5)

email_sisend = ttk.Entry(sisestuse_raam)
email_sisend.insert(tk.END, "Email")
email_sisend.pack(side=tk.LEFT, padx=5)

car_make_sisend = ttk.Entry(sisestuse_raam)
car_make_sisend.insert(tk.END, "Autotootja")
car_make_sisend.pack(side=tk.LEFT, padx=5)

car_model_sisend = ttk.Entry(sisestuse_raam)
car_model_sisend.insert(tk.END, "Automudel")
car_model_sisend.pack(side=tk.LEFT, padx=5)

car_year_sisend = ttk.Entry(sisestuse_raam)
car_year_sisend.insert(tk.END, "Auto aasta")
car_year_sisend.pack(side=tk.LEFT, padx=5)

car_price_sisend = ttk.Entry(sisestuse_raam)
car_price_sisend.insert(tk.END, "Auto hind")
car_price_sisend.pack(side=tk.LEFT, padx=5)

lisa_nupp = ttk.Button(root, text="Lisa andmed", command=lisa_andmed)
lisa_nupp.pack(pady=10)

veergude_nimed = ["ID", "first_name", "last_name", "email", "car_make", "car_model", "car_year", "car_price"]

treeview = ttk.Treeview(root, columns=veergude_nimed, show="headings")
for veerg in veergude_nimed:
    treeview.heading(veerg, text=veerg)
treeview.pack(pady=10)

kustuta_nupp = ttk.Button(root, text="Kustuta rida", command=kustuta_rida)
kustuta_nupp.pack(pady=10)

teemavärvi_nupp = ttk.Button(root, text="Muuda teemavärvi", command=muuda_teemavarvi)
teemavärvi_nupp.pack(pady=10)

root.mainloop()
cursor.close()
connection.close()
