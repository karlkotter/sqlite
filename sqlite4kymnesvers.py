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

# Loome tabeli kuvamiseks
veergude_nimed = ["ID", "first_name", "last_name", "email", "car_make", "car_model", "car_year", "car_price"]

treeview = ttk.Treeview(root, columns=veergude_nimed, show="headings")
for veerg in veergude_nimed:
    treeview.heading(veerg, text=veerg)
    treeview.pack()



root.mainloop()

# Sulgeme andmebaasiühenduse
cursor.close()
connection.close()
