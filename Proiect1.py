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
Angajati[
 Angajat = {
  "CNP":2950926360020,
  "Nume": Enache,
  "Prenume": Adina,
    "Varsta": 30,
     "Salar":4.700,
    "Departament":Resurse umane,
    "Senioritate":mid
 }
Angajat = {
  "CNP":1801826360109,
  "Nume": Ionescu,
  "Prenume": Andrei,
    "Varsta": 45,
     "Salar":4.800,
    "Departament":Financiar,
    "Senioritate":senior
 }

Angajat = {
  "CNP":1901826360019,
  "Nume": Popescu,
  "Prenume":Radu,
    "Varsta": 35,
     "Salar":4.700,
    "Departament":Vanzari,
    "Senioritate":mid
 }

Angajat = {
  "CNP":1851826360010,
  "Nume": Antonescu,
  "Prenume": Lucian,
    "Varsta": 40,
     "Salar":4.800,
    "Departament":Productie,
    "Senioritate":senior
 }
 ]
 def adaugare_angajat:
        cnp = input("Introduceti CNP: 2880926360020")
        nume = input("Introduceti nume:Turcescu ")
        prenume = input("Introduceti prenume:Anca ")
        varsta = int(input("Introduceti varsta:37 "))
        salar = float(input("Introduceti salar:4.600 "))
        departament = input("Introduceti departament:Administratie ")
        senioritate = input("Introduceti senioritate (junior, mid, senior):mid ")
        angajat = Angajat(cnp, nume, prenume, varsta, salar, departament, senioritate)
        angajati.append(angajat)
        print("Angajat adaugat cu succes!")

    def cautare_angajat(cnp):
        for angajat in angajati:
            if angajat.cnp == cnp:
                return angajat
        return None

    def modificare_angajat(cnp):
        angajat = cautare_angajat(cnp)
        if angajat:
            angajat.nume = input("Introduceti noul nume: ")
            angajat.prenume = input("Introduceti noul prenume: ")
            angajat.varsta = int(input("Introduceti noua varsta: "))
            angajat.salar = float(input("Introduceti noul salar: "))
            angajat.departament = input("Introduceti noul departament: ")
            angajat.senioritate = input("Introduceti noua senioritate (junior, mid, senior): ")
            print("Datele angajatului au fost actualizate!")
        else:
            print("Angajatul nu a fost gasit!")

    def stergere_angajat(cnp):
        global angajati
        angajati = [angajat for angajat in angajati if angajat.cnp != cnp]
        print("Angajat sters cu succes!")

    def afisare_angajati:
        for angajat in angajati:
            print(f"CNP: {angajat.cnp}, Nume: {angajat.nume}, Prenume: {angajat.prenume}, Varsta: {angajat.varsta}, Salar: {angajat.salar}, Departament: {angajat.departament}, Senioritate: {angajat.senioritate}")

    def calculator_cost_total_salarii:
        total = sum(angajat.salar for angajat in angajati)
        print(f"Cost total salarii: {total}")

    def calculator_cost_total_salarii_departament(departament):
        total = sum(angajat.salar for angajat in angajati if angajat.departament == departament)
        print(f"Cost total salarii pentru departamentul {departament}: {total}")

    def calculator_fluturas_salar(cnp):
        angajat = cautare_angajat(cnp)
        if angajat:
            brut = angajat.salar
            cas = brut * 0.10
            cass = brut * 0.25
            impozit = (brut - (cas + cass)) * 0.10
            net = brut - (cas + cass + impozit)
            print(f"Fluturas salar pentru {angajat.nume} {angajat.prenume}:")
            print(f"Salar brut: {brut}, CAS: {cas}, CASS: {cass}, Impozit: {impozit}, Salar net: {net}")
        else:
            print("Angajatul nu a fost gasit!")

    def afisare_angajati_dupa_senioritate:
        angajati.sort
        afisare_angajati

    def afisare_angajati_dupa_departament:
        angajati.sort
        afisare_angajati

    def meniu:
        while True:
            print("Meniu:")
            print("1) Adaugare angajat")
            print("2) Cautare angajat (dupa CNP)")
            print("3) Modificare date angajat (dupa CNP)")
            print("4) Stergere angajat")
            print("5) Afisare angajati")
            print("6) Calculator cost total salarii")
            print("7) Calculator cost total salarii departament")
            print("8) Calculator fluturas salar angajat")
            print("9) Afisarea angajatilor (dupa senioritate)")
            print("10) Afisarea angajatilor (dupa departament)")
            print("11) Iesire")
            
            optiune = input("Alege o optiune: ")
            
            if optiune == '1':
                adaugare_angajat
            elif optiune == '2':
                cnp = input("Introduceti CNP: ")
                angajat = cautare_angajat(cnp)
                if angajat:
                    print(f"Angajat gasit: {angajat.nume} {angajat.prenume}")
                else:
                    print("Angajatul nu a fost gasit!")
            elif optiune == '3':
                cnp = input("Introduceti CNP: ")
                modificare_angajat(cnp)
            elif optiune == '4':
                cnp = input("Introduceti CNP: ")
                stergere_angajat(cnp)
            elif optiune == '5':
                afisare_angajati
            elif optiune == '6':
                calculator_cost_total_salarii
            elif optiune == '7':
                departament = input("Introduceti departament: ")
                calculator_cost_total_salarii_departament(departament)
            elif optiune == '8':
                cnp = input("Introduceti CNP: ")
                calculator_fluturas_salar(cnp)
            elif optiune == '9':
                afisare_angajati_dupa_senioritate
            elif optiune == '10':
                afisare_angajati_dupa_departament
            elif optiune == '11':
                print("Iesire din program.")
                break
            else:
                print("Optiune invalida! Te rog sa incerci din nou.")



        
 
