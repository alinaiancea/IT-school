# Proiect1
# Textul proiectului suna in felul urmator:

# Mini proiect
# Sa se scrie un program care tine evidenta angajatilor dintr-o companie.
# Informatiile pe care trebuie sa le retinem despre un angajat sunt urmatoarele:
#     1) CNP
#     2) Nume
#     3) Prenume
#     4) Varsta
#     5) Salar
#     6) Departament
#     7) Senioritate (junior, mid, senior)

# Programul trebuie sa dispuna de un meniu care ne permite sa efectuam urmatoarele actiuni:
#     1) Adaugare angajat
#     2) Cautare angajat (dupa CNP)
#     3) Modificare date angajat (dupa CNP)
#     4) Stergere angajat
#     5) Afisare angajati
#     6) Calculator cost total salarii
#     7) Calculator cost total salarii departament
#     8) Calculator fluturas salar angajat (CAS - 10% din brut, CASS - 25% din brut, Impozit - 10% din ce a ramas)
#     9) Afisarea angajatilor (dupa senioritate)
#     10) Afisarea angajatilor (dupa departament)
#     11) Iesire

# Lista pentru a stoca angajații

angajati[
 angajat1 = {
  "CNP":2950926360020,
  "Nume": Enache,
  "Prenume": Adina,
    "Varsta": 30,
     "Salar":4.700,
    "Departament":Resurse umane,
    "Senioritate":mid
 }


angajat2 = {
  "CNP":1801826360109,
  "Nume": Ionescu,
  "Prenume": Andrei,
    "Varsta": 45,
     "Salar":4.800,
    "Departament":Financiar,
    "Senioritate":senior
 }

angajat3 = {
  "CNP":1901826360019,
  "Nume": Popescu,
  "Prenume":Radu,
    "Varsta": 35,
     "Salar":4.700,
    "Departament":Vanzari,
    "Senioritate":mid
 }

angajat4 = {
  "CNP":1851826360010,
  "Nume": Antonescu,
  "Prenume": Lucian,
    "Varsta": 40,
     "Salar":4.800,
    "Departament":Productie,
    "Senioritate":senior
 }

 ]
 
def adaugare_angajat():
    cnp = input("Introduceti CNP: ")
    nume = input("Introduceti Nume: ")
    prenume = input("Introduceti Prenume: ")
    varsta = int(input("Introduceti Varsta: "))
    salar = float(input("Introduceti Salar: "))
    departament = input("Introduceti Departament: ")
    senioritate = input("Introduceti Senioritate (junior, mid, senior): ")
    
    angajat = {
        "CNP": cnp,
        "Nume": nume,
        "Prenume": prenume,
        "Varsta": varsta,
        "Salar": salar,
        "Departament": departament,
        "Senioritate": senioritate
    }
    
    angajati.append(angajat)
    print("Angajat adaugat cu succes!")

def cautare_angajat():
    cnp = input("Introduceti CNP-ul angajatului de cautat: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            print(angajat)
            return
    print("Angajatul nu a fost gasit.")

def modificare_angajat():
    cnp = input("Introduceti CNP-ul angajatului de modificat: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            angajat["Nume"] = input("Introduceti Nume nou: ")
            angajat["Prenume"] = input("Introduceti Prenume nou: ")
            angajat["Varsta"] = int(input("Introduceti Varsta noua: "))
            angajat["Salar"] = float(input("Introduceti Salar nou: "))
            angajat["Departament"] = input("Introduceti Departament nou: ")
            angajat["Senioritate"] = input("Introduceti Senioritate noua (junior, mid, senior): ")
            print("Datele angajatului au fost modificate.")
            return
    print("Angajatul nu a fost gasit.")

def stergere_angajat():
    cnp = input("Introduceti CNP-ul angajatului de sters: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            angajati.remove(angajat)
            print("Angajat sters cu succes.")
            return
    print("Angajatul nu a fost gasit.")

def afisare_angajati():
    for angajat in angajati:
        print(angajat)

def calculator_cost_total_salari():
    total = sum(angajat["Salar"] for angajat in angajati)
    print(f"Cost total salarii: {total}")

def calculator_cost_total_salari_departament():
    departament = input("Introduceti departamentul: ")
    total = sum(angajat["Salar"] for angajat in angajati if angajat["Departament"] == departament)
    print(f"Cost total salarii pentru departamentul {departament}: {total}")

def calculator_fluturas_salar():
    cnp = input("Introduceti CNP-ul angajatului: ")
    for angajat in angajati:
        if angajat["CNP"] == cnp:
            brut = angajat["Salar"]
            cas = brut * 0.10
            cass = brut * 0.25
            impozit = (brut - cas - cass) * 0.10
            print(f"Fluturas salar pentru {angajat['Nume']} {angajat['Prenume']}:")
            print(f"Salar brut: {brut}")
            print(f"CAS: {cas}")
            print(f"CASS: {cass}")
            print(f"Impozit: {impozit}")
            return
    print("Angajatul nu a fost gasit.")

def afisare_angajati_dupa_senioritate():
    senioritate = input("Introduceti senioritatea (junior, mid, senior): ")
    for angajat in angajati:
        if angajat["Senioritate"] == senioritate:
            print(angajat)

def afisare_angajati_dupa_departament():
    departament = input("Introduceti departamentul: ")
    for angajat in angajati:
        if angajat["Departament"] == departament:
            print(angajat)

def meniu():
    while True:
        print("Meniu:")
        print("1. Adaugare angajat")
        print("2. Cautare angajat")
        print("3. Modificare date angajat")
        print("4. Stergere angajat")
        print("5. Afisare angajati")
        print("6. Calculator cost total salarii")
        print("7. Calculator cost total salarii departament")
        print("8. Calculator fluturas salar angajat")
        print("9. Afisarea angajatilor (dupa senioritate)")
        print("10. Afisarea angajatilor (dupa departament)")
        print("11. Iesire")
        
        optiune = input("Alegeti o optiune: ")
        
        if optiune == "1":
            adaugare_angajat()
        elif optiune == "2":
            cautare_angajat()
        elif optiune == "3":
            modificare_angajat()
        elif optiune == "4":
            stergere_angajat()
        elif optiune == "5":
            afisare_angajati()
        elif optiune == "6":
            calculator_cost_total_salari()
        elif optiune == "7":
            calculator_cost_total_salari_departament()
        elif optiune == "8":
            calculator_fluturas_salar()
        elif optiune == "9":
            afisare_angajati_dupa_senioritate()
        elif optiune == "10":
            afisare_angajati_dupa_departament()
        elif optiune == "11":
            print("Iesire din program.")
            break
        else:
            print("Optiune invalida. Va rugam sa incercati din nou.")

# Pornim programul