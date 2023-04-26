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
    # prompt the user to enter input parameters
    automark = input("Sisestage automark mida saavite kuvada: ")
    pnimi = input("Sisestage omaniku perekonnanimi: ")
    
    # establish a connection to the database
    conn = sqlite3.connect("antmebas.db")
    cursor = conn.cursor()
    
    # execute the SQL query to get the 5 most expensive cars of the selected make owned by the specified owner's last name
    cursor.execute("SELECT car_make, car_model FROM kkotter WHERE car_make=? AND owner_last_name=? ORDER BY price DESC LIMIT 5", (automark, pnimi))
    vastus = cursor.fetchall()
    
    # print the results
    print(f"The 5 most expensive {automark} cars owned by {pnimi} are:")
    for result in vastus:
        print(result[0], result[1])


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








