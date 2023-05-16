import sqlite3
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkbs

# Loome andmebaasiühenduse
connection = sqlite3.connect('c:/sqlite/antmebas.db')
cursor = connection.cursor()

# Funktsioon, mis kuvab andmed vastavalt valitud ridade arvule
def kuvatud_andmed(valitud_arv):
    # Tühjendame eelnevalt kuvatud andmed
    for i in treeview.get_children():
        treeview.delete(i)

    # Küsime andmed andmebaasist
    cursor.execute('SELECT * FROM kkotter')
    andmed = cursor.fetchmany(valitud_arv)

    # Kuvame andmed tabelis
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
    # Hoiame sisestatud väärtused muutujates
    first_name = first_name_sisend.get()
    last_name = last_name_sisend.get()
    email = email_sisend.get()
    car_make = car_make_sisend.get()
    car_model = car_model_sisend.get()
    car_year = car_year_sisend.get()
    car_price = car_price_sisend.get()

    # Lisame andmed andmebaasi
    cursor.execute("INSERT INTO kkotter (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, email, car_make, car_model, car_year, car_price))
    connection.commit()

    # Kuvame uuendatud andmed
    kuvatud_andmed(int(valik_var.get()))

def kustuta_rida():
    valitud_rida = treeview.focus()
    if valitud_rida:
        rida_info = treeview.item(valitud_rida)['values']
        cursor.execute("DELETE FROM kkotter WHERE ID=?", (rida_info[0],))
        connection.commit()
        treeview.delete(valitud_rida)

# Loome GUI
root = tk.Tk()
root.title("Andmete kuvamine")
root.geometry("1800x400")

# Rakendame ttkbootstrap dark_theme kujunduse
style = ttkbs.Style(theme='vapor')

# Loome valikukasti
valik_var = tk.StringVar()
valik_var.set("5")  # Vaikeväärtus on 5

valikukast = ttk.Combobox(root, textvariable=valik_var, values=["5", "10", "20", "30"])
valikukast.pack(pady=10)

# Nupu vajutamisel kuvatakse valitud arv ridu
nupp = ttk.Button(root, text="Kuva andmed", command=lambda: kuvatud_andmed(int(valik_var.get())))
nupp.pack(pady=10)

otsing_sisend = ttk.Entry(root)
otsing_sisend.pack(pady=10)

otsing_nupp = ttk.Button(root, text="Otsi", command=otsi_andmeid)
otsing_nupp.pack(pady=10)

first_name_sisend = ttk.Entry(root)
first_name_sisend.pack(pady=5)

last_name_sisend = ttk.Entry(root)
last_name_sisend.pack(pady=5)

email_sisend = ttk.Entry(root)
email_sisend.pack(pady=5)

car_make_sisend = ttk.Entry(root)
car_make_sisend.pack(pady=5)

car_model_sisend = ttk.Entry(root)
car_model_sisend.pack(pady=5)

car_year_sisend = ttk.Entry(root)
car_year_sisend.pack(pady=5)

car_price_sisend = ttk.Entry(root)
car_price_sisend.pack(pady=5)

lisa_nupp = ttk.Button(root, text="Lisa andmed", command=lisa_andmed)
lisa_nupp.pack(pady=10)

veergude_nimed = ["ID", "first_name", "last_name", "email", "car_make", "car_model", "car_year", "car_price"]

treeview = ttk.Treeview(root, columns=veergude_nimed, show="headings")
for veerg in veergude_nimed:
    treeview.heading(veerg, text=veerg)
    treeview.pack()

kustuta_nupp = ttk.Button(root, text="Kustuta rida", command=kustuta_rida)
kustuta_nupp.pack(pady=10)

root.mainloop()
cursor.close()
connection.close()
