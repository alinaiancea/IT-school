# tema6
# 49) Sa se scrie un program care tine evidenta elevilor dintr-o scoala.
# Programul trebuie sa dispuna de un meniu care ne pune la dispozitie
# urmatoarele optiuni:
    
# 1.Adaugare elev
# 2.Afisarea elevilor existenti
# 3.Modificare informatii elev existent
# 4.Stergere elev
# 5.Cautare elev dupa nume si prenume
# 6.Afisare elevi in ordinea mediei
# 7.Afisare elevi cu media peste 8
# 8.Afisare elevi in ordine alfabetica (in functie de Nume)
# 9.Iesire din program

# Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
# Nume
# Prenume
# Nota romana
# Nota matematica
# Nota engleza
# Media (sa se calculeze automat pe baza notelor introduse)
def calculeaza_medie(note):
return (note["romana"] + note["matematica"] + note["engleza"]) / 3
def adauga_elev(lista_elevi):
nume = input("Introduceți numele: ") 
prenume = input("Introduceți prenumele: ")
 nota_romana = float(input("Introduceți nota la Romana (0-10): "))  
if 0 <= nota_romana <= 10: 
 nota_matematica = float(input("Introduceți nota la Matematica (0-10): "))
 if 0 <= nota_matematica <= 10:
  nota_engleza = float(input("Introduceți nota la Engleza (0-10): ")) 
if 0 <= nota_engleza <= 10:
  elev_nou = {
  "nume": nume,
   "prenume": prenume,  
        "romana": nota_romana,  
        "matematica": nota_matematica,  
        "engleza": nota_engleza
    }  
     lista_elevi.append(elev_nou) 
  print(f"Elevul {nume} {prenume} a fost adăugat cu succes!")
  def afiseaza_elevi(lista_elevi):
    print("\n--- Lista elevilor ---")
   for i, elev in enumerate(lista_elevi, 1):
print(f"{i}. {elev['nume']} {elev['prenume']}: Romana: {elev['romana']}, "
f"Matematica: {elev['matematica']}, Engleza: {elev['engleza']}, " 
 f"Media: {elev['medie']:.2f}")
 def modifica_elev(lista_elevi):
 afiseaza_elevi(lista_elevi) 
 while True:
  index = int(input("\nIntroduceți numărul elevului pe care doriți să îl modificați: "))
if 0 <= index < len(lista_elevi):
          break 
 else:
     print("Numărul introdus nu este valid!") 
   elev = lista_elevi[index]
   print(f"\nModificare date pentru elevul: {elev['nume']} {elev['prenume']}")
 nume_nou = input(f"Nume nou (sau Enter pentru a păstra '{elev['nume']}'): ") 
if nume_nou: 
 elev['nume'] = nume_nou 
    prenume_nou = input(f"Prenume nou (sau Enter pentru a păstra '{elev['prenume']}'): ") 
 if prenume_nou: 
    elev['prenume'] = prenume_nou 
    nota_romana_str = input(f"Nota nouă la Romana (sau Enter pentru a păstra '{elev['romana']}'): ")
    if 0 <= nota_romana <= 10:
      elev['romana'] = nota_romana 
     else:
        print("Nota trebuie să fie între 0 și 10! Nota nu a fost modificată.")
       nota_matematica_str = input(f"Nota nouă la Matematica (sau Enter pentru a păstra '{elev['matematica']}'): ")
       if 0 <= nota_matematica <= 10: 
        elev['matematica'] = nota_matematica  
      else:
         print("Nota trebuie să fie între 0 și 10! Nota nu a fost modificată.") 
  nota_engleza_str = input(f"Nota nouă la Engleza (sau Enter pentru a păstra '{elev['engleza']}'): ") 
 if 0 <= nota_engleza <= 10: 
     elev['engleza'] = nota_engleza 
    else:
       print("Nota trebuie să fie între 0 și 10! Nota nu a fost modificată.")
     elev['medie'] = calculeaza_medie(elev)
   print("Datele elevului au fost actualizate cu succes!") 
 def sterge_elev(lista_elevi):
    def sterge_elev(lista_elevi):
   while True:
      index = int(input("\nIntroduceți numărul elevului pe care doriți să îl ștergeți: "))-1
      if 0 <= index < len(lista_elevi): 
       break
     else:
         print("Numărul introdus nu este valid!")
         elev = lista_elevi[index] 
       confirmare = input(f"Sigur doriți să ștergeți elevul {elev['nume']} {elev['prenume']}? (da/nu): ")
      if confirmare.lower() == "da": 
    lista_elevi.pop(index)
 print("Elevul a fost șters cu succes!")
  else: 
  print("Operațiunea de ștergere a fost anulată.") optiunea_aleasa_de_utilizator == 6: # Afisare elevi in ordinea mediei

        while True:
            lista_sortata = sorted(lista_catalog, key=functie_sortare_dupa_medie, reverse=True)

            print('Catalogul sortat in functie de media fiecarui elev este : ')

            for element in lista_sortata:
                print(element)
        
            inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 7: # Afisare elevi cu media peste 8
        while True:
            x = ''
            for element in lista_catalog:
                if element['MEDIA'] > 8:
                    print(element)

            inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 8: # Afisare elevi in ordine alfabetica (in functie de Nume)

        while True:
            lista_sortata = sorted(lista_catalog, key=functie_sortare_dupa_nume, reverse=False)

            print('Catalogul sortat in functie de numele fiecarui elev este : ')

            for element in lista_sortata:
                print(element)
        
            inchidere_previzualiare = input('Doriti inchiderea previzualizarii si iesirea in meniul principal (Da/Nu) : ' ).lower() == 'da'
            if inchidere_previzualiare:
                break

    elif optiunea_aleasa_de_utilizator == 9: #Iesire din aplicatie
        print('La nevedere!')
        break
