# tema3
# 32) Sa se scrie un program care sa replice functionalitatea unui calculator. Utilizatorul trebuie sa introduca operatia pe care doreste sa o realizeze sub forma: "10 + 5" , "11 * 3" , "10 / 2" , "12 - 10", iar programul trebuie sa afiseze rezultatul operatiei.
# Pentru implementarea programului se va creea cate o functie pentru fiecare operatie: adunare, scadere, inmultire, impartire. 
# Executia programului va inceta in momentul in care utilizatorul introduce cuvantul "exit".
print('Calculator')

def adunare(arg1,arg2):
    return arg1 + arg2
def scadere(arg1,arg2):
    return arg1 - arg2
def inmultire(arg1,arg2):
    return arg1 * arg2
def impartire(arg1,arg2):
    return arg1 / arg2


while True:

    calcul = input('Introduceti numerele si operatiunea dorita : ')

    if calcul.upper() == 'EXIT':
        break

    if len(calcul) < 5:
        print('Nu ati introdus date valide! Datele trebuie sa fie de forma "a + b" ! Reincercati! ')
    elif ' ' not in calcul:
        print('Nu ati introdus date valide! Datele trebuie sa fie de forma "a + b" ! Reincercati! ')
    else:
        impartirea_datelor = calcul.split(' ')
        nr1 = impartirea_datelor[0].strip()
        nr2 = impartirea_datelor[2].strip()
        operator = impartirea_datelor[1].strip()

        nr1 = float(nr1)
        nr2 = float(nr2)

        if operator == '+':
            print(adunare(nr1,nr2))
        elif operator == '-':
            print(scadere(nr1,nr2))
        elif operator == '*':
            print(inmultire(nr1,nr2))
        elif operator == '/':
            print(impartire(nr1,nr2))
        else:
            print('Nu ati introdus o operatiune matematica valida! Reincercati! ')
