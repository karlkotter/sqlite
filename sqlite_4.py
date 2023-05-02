import tkinter as tk
import sqlite3

aken = tk.Tk()
aken.title("SQLite tri")

yhendus = sqlite3.connect('antmebas.db')
cursor = yhendus.cursor()
aken.mainloop()

            	                        