import tkinter as tk
from tkinter import scrolledtext
import sqlite3

yhendus = sqlite3.connect('c:/sqlite/antmebas.db')
c = yhendus.cursor()

def kuvaAndmed():
    c.execute("SELECT * FROM kkotter")
    andmed = c.fetchall()
    andmeteAken = tk.Tk()
    andmeteAken.title("Kõik andmed")
    andmeteAken.geometry("800x800") # määrake algne akna suurus
    tekstilahter = scrolledtext.ScrolledText(andmeteAken, font=("Arial", 12))
    tekstilahter.pack(fill="both", expand=True) # täitke akna kogu ruum
    for anne in andmed:
        tekstilahter.insert(tk.END, str(anne) + "\n")

aken = tk.Tk()
aken.title("SQLite tri")
nupp = tk.Button(aken, text="Kuva andmed", command=kuvaAndmed)
nupp.pack()

aken.mainloop()