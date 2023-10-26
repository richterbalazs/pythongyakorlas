import math

def elso():
    # Írjuk ki 0-tól 150-ig a páros számokat!
    szamsor = 0
    while szamsor < 150:
        if szamsor % 2 == 0:
            print(szamsor, end=", ")
        szamsor += 1
    print(150, end="")

def ketto():

    # kérjünk be a felhasználótól 10 darab számot, majd azokat számoljuk össze amelyek 3-mal oszthatóak.
    osztharom = 0
    sorszam = 1

    while sorszam <= 10:
        szam = int(input("Kérem adja meg a(z) "+str(sorszam)+". számot:"))
        if szam % 3 == 0:
            osztharom += 1
        sorszam += 1
    print("A bekér számok alapján "+str(osztharom)+" olyan szám található, amely 3-mal osztható.")

def harom():

    # Addig kérjünk be számokat, amíg 10-zel osztható nem lesz!

    szam = int(input("Kérem adja meg a következő számot"))

    while not (szam % 10 == 0):
        szam = int(input("Kérem adja meg a következő számot"))

    print("Siker, a szám osztható 10-el így a program kilép.")

def negy():

    # Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot.

    szam = int(input("Kérem adja meg a következő számot"))

    while not (((((szam >= 10) and (szam <= 99)) or ((szam >= -99) and (szam <= -10)))) and (szam % 2 == 0)):
        szam = int(input("Kérem adja meg a következő számot"))

    print("Siker, a szám osztható 2 számjegyű és páros, így a program kilép")

def otodik():

    # Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.
    szam = int(input("Kérem adjon meg egy olyan számot, ami pozitív páratlan szám: "))
    while not ((szam > 0) and (szam % 2 == 1)):
        szam = int(input("Kérem adjon meg egy olyan számot, ami pozitív és páratlan szám"))

    print("Siker, a szám pozitív és páratlan.")

def hatodik():

     #Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.
     szam = int(input("Kérem adjon meg egy számot: "))

     while not ((szam % 3 == 0) and (int(math.sqrt(szam)))):
        szam = int(input("Kérem adjon meg egy számot"))

def het():

    #Kérj be 3 valós számot, amíg szerleszthető háromszög oldalait nem kapjuk!

    a = float(input("Kérem adjon meg egy valós számot:"))
    b = float(input("Kérem adjon meg egy másik valós számot."))
    c = float(input("Kérem adjon meg egy harmadik valós számot."))
    while not((a > b+c) and (b < a+c) and (c < a+b)):
        print("A háromszög nem szerkeszthető")
        a = float(input("Kérem adjon meg egy valós számot: "))
        b = float(input("Kérem adjon meg egy másik valós számot: "))
        c = float(input("Kérem adja meg a harmadik valós számot: "))

    print("A háromszög szerkeszthető")