# tema4
# 33.Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]].
#  Sa se extraga numele "Ionut" din lista si sa se afiseze.

list=[[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
 nume_ionut = list[1][1]
print(f"nume extras este: {nume_ionut}")


# # 34.Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]].
# #  Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

list=[[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
litera_r = list[1][2][2]
 print(f"litera extrasa este: {litera_r}")


# 35. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]].
#  Sa se afiseze toate numerele de tip float din lista.

 list = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
    numere_float = list[2]
    print("Numerele de tip float din list sunt:", numere_float)

# 36. Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]].
#  Scrieti un program care citeste un nume de la tastatura si verifica daca numele se afla in lista.
 list = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
    nume = input("Introduceti un nume pentru a verifica daca se afla in list: ")
    if nume in list[1]:
        print(f"Numele '{nume}' se afla in list.")
    else:
        print(f"Numele '{nume}' nu se afla in list.")
#   37.Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. 
#      Sa se afiseze numerele pare din lista. 
    list = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    numere_pare = [numar for numar in list if numar % 2 == 0]
    print("Numerele pare din list sunt:", numere_pare)
#  38.Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. 
# Sa se afiseze cel mai mic numar si cel mai mare numar din lista.
lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    minim = min(lista)
    maxim = max(lista)
    print(f"Cel mai mic numar din lista este: {minim}")
    print(f"Cel mai mare numar din lista este: {maxim}")
# 39.Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. 
# Sa se scrie o functie care primeste ca parametru lista si un numar. 
# Functia trebuie sa afiseze toate numerele din lista care sunt divizibile cu numarul dat.
#  Numarul dat este introdus de la tastatura de catre utilizatorul programului.
 lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    
    def afiseaza_divizibile(lista, numar):
        divizibile = [x for x in lista if x % numar == 0]
        if divizibile:
            print(f"Numerele din lista divizibile cu {numar} sunt:", divizibile)
        else:
            print(f"Nu exista numere in lista divizibile cu {numar}")
    
    numar = int(input("Introduceti un numar pentru a verifica divizibilitatea: "))
    afiseaza_divizibile(lista, numar)
# 40.Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97].
# Sa se scrie o functie care primeste ca parametru lista si afiseaza suma numerelor impare din lista.
 lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    
    def suma_impare(lista):
        suma = sum([numar for numar in lista if numar % 2 != 0])
        return suma
    
    print(f"Suma numerelor impare din lista este: {suma_impare(lista)}")
# 41.Se da lista: [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]. Sa se scrie o functie care primeste ca parametru lista si un numar. Functia trebuie sa afiseaza indexul numarului daca
# acesta se afla in lista sau "Not Found" in caz contrar.
lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    
    def gaseste_index(lista, numar):
        if numar in lista:
            return lista.index(numar)
        else:
            return "Not Found"
    
    numar = int(input("Introduceti un numar pentru a cauta indexul sau in lista: "))
    rezultat = gaseste_index(lista, numar)
    print(f"Indexul numarului {numar} in lista este: {rezultat}")

