import sqlite3

yhendus = sqlite3.connect('c:/sqlite/antmebas.db')
cursor = yhendus.cursor()

menuu = yhendus.execute("SELECT * FROM kkotter")

def menu():
    print ("[1] Lisa andmed")
    print ("[2] Kuva read, mis sisaldavad < 2000 autosid")
    print ("[3] Kuva keskmine autode aasta, kallim hind")
    print ("[4] Kuva 5 uusimat autode aastat, mudeliga")
    print ("[5] Kuva 5 enda valitud autot (koige kallim)")
    print ("[6] Kustuta id järgi")
    print ("[7] Kustuta read mis sisaldavad alla 2000 autosid, kindla margi kohaselt")
    print ("[8] Ekspordi CSVsse")
    print ("[0] Lahku")

menu()
valik = int(input("sisesta valik: "))


def andmeteLisamine():
    
    print("Sisestage andmed, mida soovite lisada tabelisse")
    first_name = input("Eesnimi: ")
    last_name = input("Perenimi: ")
    email = input("Email: ")
    car_make = input("Auto tegija: ")
    car_model = input("Auto mudel: ")
    car_year = int(input("Auto aasta: "))
    car_price = int(input("Auto hind: "))

    yhendus.execute("INSERT INTO kkotter (first_name, last_name, email, car_make, car_model, car_year, car_price) VALUES (?, ?, ?, ?, ?, ?, ?)", (first_name, last_name, email, car_make, car_model, car_year, car_price))
    yhendus.commit()
    print("andmed lisatud")

def alla2000autod():

    cursor.execute("SELECT * FROM kkotter WHERE car_year < 2000 ORDER BY car_year ASC LIMIT 20")
    autod = cursor.fetchall()
    for rida in autod:
        print(rida)
    yhendus.commit()

def keskmineAutoAastaHind():
    print("tere")


if valik == 1:
    andmeteLisamine()

elif valik == 2:
    alla2000autod()

elif valik == 3:
    keskmineAutoAastaHind()







