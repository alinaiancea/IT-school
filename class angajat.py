class Angajat:
        """
        Clasa care reprezintă un angajat al companiei.
        Atributele includ CNP, nume, prenume, vârstă, salariu, departament și senioritate.
        """

        def __init__(self, cnp, nume, prenume, varsta, salar, departament, senioritate):
            self.cnp = cnp
            self.nume = nume
            self.prenume = prenume
            self.varsta = varsta
            self.salar = salar
            self.departament = departament
            self.senioritate = senioritate

        def __repr__(self):
            return f"Angajat(CNP={self.cnp}, Nume={self.nume}, Prenume={self.prenume}, Varsta={self.varsta}, Salar={self.salar}, Departament={self.departament}, Senioritate={self.senioritate})"


class Companie:
        """
        Clasa care gestionează angajații din companie.
        Permite adăugarea, căutarea, modificarea, ștergerea și afișarea angajaților.
        """

        def __init__(self):
            self.angajati =[ 
 {
  "CNP":2950926360020,
  "Nume": "Enache",
  "Prenume": "Adina",
    "Varsta": 30,
     "Salar":4.700,
    "Departament":"Resurse umane",
    "Senioritate":"mid"
 }

 {
  "CNP":1801826360109,
  "Nume": "Ionescu",
  "Prenume": "Andrei",
    "Varsta": 45,
     "Salar":4.800,
    "Departament":"Financiar",
    "Senioritate":"senior"
 }

 {
  "CNP":1901826360019,
  "Nume": "Popescu",
  "Prenume":"Radu",
    "Varsta": 35,
     "Salar":4.700,
    "Departament":"Vanzari",
    "Senioritate":"mid"
 }

 {
  "CNP":1851826360010,
  "Nume": "Antonescu",
  "Prenume": "Lucian",
    "Varsta": 40,
     "Salar":4.800,
    "Departament":"Productie",
    "Senioritate":"senior"
 }

]

        def adaugare_angajat(self):
            cnp = input("Introduceti CNP: ")
            nume = input("Introduceti Nume: ")
            prenume = input("Introduceti Prenume: ")
            varsta = int(input("Introduceti Varsta: "))
            salar = float(input("Introduceti Salar: "))
            departament = input("Introduceti Departament: ")
            senioritate = input("Introduceti Senioritate (junior, mid, senior): ")

            angajat = Angajat(cnp, nume, prenume, varsta, salar, departament, senioritate)
            self.angajati.append(angajat)
            angajat = {
        "CNP": cnp,
        "Nume": nume,
        "Prenume": prenume,
        "Varsta": varsta,
        "Salar": salar,
        "Departament": departament,
        "Senioritate": senioritate
    }
            print("Angajat adaugat cu succes!")
# verificare ca CNP-ul are exact 13 caractere și sunt doar cifre:
if len(cnp) == 13 and cnp.isdigit():
    # CNP valid
# else:
#     #  CNP invalid
# verificare ca vârsta este peste 18 și mai mică de 65:
# if 18 < varsta < 65:
    # Vârsta este validă
# else:
    # Vârsta este invalidă
# Verifică dacă salariul este mai mare de 4050 lei:
# if salar > 4050:
    # Salariul este valid
# else:
    # Salariul este invalid
# Verifică dacă senioritatea este una dintre următoarele: "junior" "mid" sau "senior":
# if senioritate in ["junior", "mid", "senior"]:
    # Senioritate validă
# else:
    # Senioritate invalidă 
    # Se verifica daca angajatul se afla in  departament:
     departamente = ["Productie", "Vânzări", "Resurse umane", "Financiar"]
     departament = input("Introduceți departamentul: ")
#  if departament in departamente:
# departament valid
# else:
# Departament invalid!
        
def cautare_angajat(self):
            cnp = input("Introduceti CNP-ul angajatului de cautat: ")
            for angajat in self.angajati:
                if angajat.cnp == cnp:
                    print(angajat)
                    return
            print("Angajatul nu a fost gasit.")

def modificare_angajat(self):
            cnp = input("Introduceti CNP-ul angajatului de modificat: ")
            for angajat in self.angajati:
                if angajat.cnp == cnp:
                    angajat.nume = input("Introduceti Nume nou: ")
                    angajat.prenume = input("Introduceti Prenume nou: ")
                    angajat.varsta = int(input("Introduceti Varsta noua: "))
                    angajat.salar = float(input("Introduceti Salar nou: "))
                    angajat.departament = input("Introduceti Departament nou: ")
                    angajat.senioritate = input("Introduceti Senioritate noua (junior, mid, senior): ")
                    print("Datele angajatului au fost modificate.")
                    return
            print("Angajatul nu a fost gasit.")

def stergere_angajat(self):
            cnp = input("Introduceti CNP-ul angajatului de sters: ")
            for angajat in self.angajati:
                if angajat.cnp == cnp:
                    self.angajati.remove(angajat)
                    print("Angajat sters cu succes.")
                    return
            print("Angajatul nu a fost gasit.")

def afisare_angajati(self):
            for angajat in self.angajati:
                print(angajat)

def calculator_cost_total_salari(self):
            total = sum(angajat.salar for angajat in self.angajati)
            print(f"Cost total salarii: {total}")

def calculator_cost_total_salari_departament(self):
            departament = input("Introduceti departamentul: ")
            total = sum(angajat.salar for angajat in self.angajati if angajat.departament == departament)
            print(f"Cost total salarii pentru departamentul {departament}: {total}")

def calculator_fluturas_salar(self):
            cnp = input("Introduceti CNP-ul angajatului: ")
            for angajat in self.angajati:
                if angajat.cnp == cnp:
                    brut = angajat.salar
                    cas = brut * 0.10
                    cass = brut * 0.25
                    impozit = (brut - cas - cass) * 0.10
                    print(f"Fluturas salar pentru {angajat.nume} {angajat.prenume}:")
                    print(f"Salar brut: {brut}")
                    print(f"CAS: {cas}")
                    print(f"CASS: {cass}")
                    print(f"Impozit: {impozit}")
                    return
            print("Angajatul nu a fost gasit.")

def afisare_angajati_dupa_senioritate(self):
            senioritate = input("Introduceti senioritatea (junior, mid, senior): ")
            for angajat in self.angajati:
                if angajat.senioritate == senioritate:
                    print(angajat)

def afisare_angajati_dupa_departament(self):
            departament = input("Introduceti departamentul: ")
            for angajat in self.angajati:
                if angajat.departament == departament:
                    print(angajat)

def meniu(self):
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
                    self.adaugare_angajat()
                elif optiune == "2":
                    self.cautare_angajat()
                elif optiune == "3":
                    self.modificare_angajat()
                elif optiune == "4":
                    self.stergere_angajat()
                elif optiune == "5":
                    self.afisare_angajati()
                elif optiune == "6":
                    self.calculator_cost_total_salari()
                elif optiune == "7":
                    self.calculator_cost_total_salari_departament()
                elif optiune == "8":
                    self.calculator_fluturas_salar()
                elif optiune == "9":
                    self.afisare_angajati_dupa_senioritate()
                elif optiune == "10":
                    self.afisare_angajati_dupa_departament()
                elif optiune == "11":
                 print("Iesire din program.")
                break
            else:
              print("Optiune invalida, va rugam sa incercati din nou.")
