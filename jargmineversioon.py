import tkinter as tk
from tkinter import scrolledtext
import sqlite3

# Lehekülje suurus
LEHE_SUUURUS = 10

def kuvaAndmed(aktiivne_leht=1):
    with sqlite3.connect('c:/sqlite/antmebas.db') as yhendus:
        c = yhendus.cursor()
        c.execute("SELECT COUNT(*) FROM kkotter")
        kogus = c.fetchone()[0]
        c.execute(f"SELECT * FROM kkotter LIMIT {LEHE_SUUURUS} OFFSET {(aktiivne_leht-1)*LEHE_SUUURUS}")
        andmed = c.fetchall()

        andmeteAken = tk.Tk()
        andmeteAken.title("Kõik andmed")
        andmeteAken.geometry("800x500")

        # Loome päise rea koos veerunimedega
        veerunimed = [i[0] for i in c.description]
        for j, nimi in enumerate(veerunimed):
            nimi_silt = tk.Label(andmeteAken, text=nimi, font=("Arial", 12))
            nimi_silt.grid(row=0, column=j)

        # Kuvame iga rea ja samba kohta andmed
        for i, rida in enumerate(andmed):
            for j, veerg in enumerate(rida):
                andme_silt = tk.Label(andmeteAken, text=veerg, font=("Arial", 12))
                andme_silt.grid(row=i+1, column=j)

        # Lisa nuppudega lehekülje kerimise funktsionaalsus
        nupp_raam = tk.Frame(andmeteAken)
        nupp_raam.grid(row=i+2, column=0, columnspan=len(veerunimed))

        # Eelmine nupp
        if aktiivne_leht > 1:
            eelmine_nupp = tk.Button(nupp_raam, text="Eelmine", command=lambda: kuvaAndmed(aktiivne_leht-1))
            eelmine_nupp.grid(row=0, column=0)

        # Järgmine nupp
        if aktiivne_leht < kogus // LEHE_SUUURUS + 1:
            jargmine_nupp = tk.Button(nupp_raam, text="Järgmine", command=lambda: kuvaAndmed(aktiivne_leht+1))
            jargmine_nupp.grid(row=0, column=1)

    andmeteAken.mainloop()

kuvaAndmed()
