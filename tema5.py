# tema5
# 42) Sa se creeze un tuple cu 5 elemente diferite si
# sa se afiseze al doilea si ultimul element.
tuple = (5, 8, 10, 12, 15)

print("Tuple:", tuple)
print("Al doilea element:", tuple[1])
print("Ultimul element:", tuple[-1])
# 43) Sa se creeze 2 tuple cu cate 3 elemente fiecare. 
# Sa se concateneze cele doua si sa 
# se afiseze noul tuple rezultat in urma operatiei.

tuple1 = (4, 5, 6)
tuple2 = ('d', 'f', 'g')
result_tuple = tuple1 + tuple2
print("Primul tuple:", tuple1)
print("Al doilea tuple:", tuple2)
print("Tuple concatenat:", result_tuple)

# 44) Sa se creeze un tuplu cu 10 elemente. 
# Sa se citeasca de la tastatura un element si 
# sa se verifice daca elementul se afla in tuplul creat.

zece_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
print("Tuple:", zece_tuple)
element = int(input("Introduceti un numar pentru a verifica daca este in  tuple: "))
if element in ten_tuple:
    print(f"{element} este in tuple")
else:
     print(f"{element} is not in the tuple") 

# 45) Sa se creeze un tuple cu 5 elemente.
# Sa se citeasca un element de la tastatura si
# sa se afiseze indexul elementului in acel tuple. 
# In caz ca nu se regaseste in tuple, sa se afiseze "not found".   
cinci_tuple = ('prune', 'portocale', 'cirese', 'piersici', 'afine')
print("Tuple:", cinci_tuple)
cauta_element = input("Introdu un element pentru a gasi index: ")
if cauta_element in cinci_tuple:
     print(f"Index al {cauta_element}: {cinci_tuple.index(cauta_element)}")
else:
     print("not found")   
# 46) Sa se creeze un tuplu cu 10 elemente. 
# Sa se extraga un subtuplu din el pornind de 
# la pozitia 2 pana la pozitia 5 si sa se afiseze.
alphabet_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print("Original tuple:", alphabet_tuple)
subtuple = alphabet_tuple[2:6]
print("Subtuple from position 2 to 5:", subtuple)
# 47) Se da o lista [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9].
# Sa se stearga elementele duplicate si sa se afiseze rezultatul.
duplicate_list = [1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 9]
print("Original list:", duplicate_list)
unique_list = list(dict.fromkeys(duplicate_list)) 
print("List after removing duplicates (method 1):", unique_list)
unique_list2 = list(set(duplicate_list))
print("List after removing duplicates (method 2):", unique_list2)
# 48)Se dau doua seturi: {1,2,3,4,5,6} si {4,5,6,7,8,9}.
# Sa se afiseze elementele care se afla in ambele seturi.
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print("Set 1:", set1)
print("Set 2:", set2)
common_elements = set1.intersection(set2)
print("Elements in both sets:", common_elements)








