import sqlite3
import csv
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
    
    cursor.execute("SELECT AVG(car_price) FROM kkotter;")
    vastus = cursor.fetchone()[0]
    print("Auto keskmine hind on:", vastus)
    cursor.execute("SELECT MAX(car_price) FROM kkotter;")
    vastus = cursor.fetchone()[0]
    print("Kõige kõrgem hind:", vastus)

def uusimatAutot():

    cursor.execute("SELECT car_make, car_model FROM kkotter ORDER BY car_year DESC LIMIT 5;")
    results = cursor.fetchall()
    print("Uusimad autod on:")
    for result in results:
        print(result[0], result[1])

def kallimAutoPerenimi():
    automark = input("Sisestage automark Toyota, Citroen, Audi, etc: ")
    perenimi = "kotter"
    cursor.execute("SELECT * FROM kkotter WHERE car_make = ? ORDER BY hind DESC, ASC LIMIT 5", (automark,))

    cursor.execute("SELECT car_make, car_price FROM kkotter WHERE ... ORDER BY car_year DESC LIMIT 5;")

def reaKustutamine():

    id = int(input("Sisestage ID nr, mida soovite andmebaasist kustutada: "))
    cursor.execute("DELETE FROM kkotter WHERE id = ?", (id,))
    print("ID", id, "on kustutatud")

def reaKustutamineAgaRaskem():
    car_year = int(input("Sisestage aasta PEAB JAAMA ALLA 2000 vist: "))
    car_mark = input("Sisesta automark: ")
    cursor.execute("DELETE FROM kkotter WHERE car_year < ? AND car_make = ?", (car_year, car_mark))
    print("Kõik read, mille aasta on alla", car_year, "ja mark on", car_mark, "on edukalt kustutatud")

def ekspordiAndmed():

    cursor.execute("SELECT * FROM kkotter")
    andmed = cursor.fetchall()
    with open('andmed.csv', mode='w', newline='') as csv_fail:
        kirjutaja = csv.writer(csv_fail, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        kirjutaja.writerow([i[0] for i in cursor.description])
        for rida in andmed:
            kirjutaja.writerow(rida)

    print("Andmed on edukalt eksporditud CSV faili")



if valik == 1:
    andmeteLisamine()

elif valik == 2:
    alla2000autod()

elif valik == 3:
    keskmineAutoAastaHind()

elif valik == 4:
    uusimatAutot()

elif valik == 5:
    kallimAutoPerenimi()

elif valik == 6:
    reaKustutamine()

elif valik == 7:
    reaKustutamineAgaRaskem()

elif valik == 8:
    ekspordiAndmed()






