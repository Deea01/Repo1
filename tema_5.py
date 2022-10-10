# TEMA 5  Functii

# Exercitii OBLIGATORII

"""
Exercitiul 1.
Funcție care să calculeze și să returneze suma a două numere
"""
print('\nExercitiul 1: ')


def suma_2_numere(nr_1, nr_2):
    return int(nr_1) + int(nr_2)


a, b = input('Introduceti 2 numere: ').split()
print(f'Suma numerelor {a} si {b} este: {suma_2_numere(a, b)}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 2.
Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
"""
print('\nExercitiul 2: ')


def detectie_paritate(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


nr = int(input('Introduceti un numar: '))
if detectie_paritate(nr):
    print('Numarul este par.')
else:
    print('Numarul este impar.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 3.
Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
"""
print('\nExercitiul 3: ')


def contor_caractere(nume, prenume, nume_mijlociu):
    return int(len(nume)) + int(len(prenume)) + int(len(nume_mijlociu))


numele, prenumele, numele_mijlociu = input('Introduceti numele dvs complet: ').split()
print(f'Numele tau complet contine {contor_caractere(numele, prenumele, numele_mijlociu)} caractere.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 4.
Funcție care returnează aria dreptunghiului
"""
print('\nExercitiul 4: ')


def arie_dreptunghi(latime, Lungime):
    return float(latime) * float(Lungime)


l, L = input('Introduceti dimensiunile dreptunghiului: ').split()
print(f'Aria dreptunghiului este: {arie_dreptunghi(l,L)} cm^2.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 5.
Funcție care returnează aria cercului
"""
print('\nExercitiul 5: ')
PI = 3.14

def arie_cerc(raza):
    return float(raza) * PI


r = int(input('Introduceti valoarea razei cercului: '))
print(f'Aria cercului este {arie_cerc(r)}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 6.
Funcție care returnează True dacă un caracter x se găsește într-un string dat
și False dacă nu găsește.
"""
print('\nExercitiul 6: ')


def gasire_caracter(text, caracter):
    if text.find(caracter) == -1:
        return False
    else:
        return True


sir = 'Alandala portocala'
crt = input(' Alegeti caracterul care doriti sa-l gasiti in string: ')
if gasire_caracter(sir, crt):
    print('Caracterul se gaseste in stringul dat.')
else:
    print('Caracterul nu se gaseste in stringul dat.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 7.
Funcție fără return, primește un string și printează pe ecran:
    ● Nr de caractere lower case este x
    ● Nr de caractere upper case exte y
"""
print('\nExercitiul 7: ')


def low_upp(text):
    contor_lower, contor_upper = 0, 0
    for i in range(len(text)):
        if text[i].islower():
            contor_lower += 1
        else:
            contor_upper += 1
    print(f'Nr de caractere lower case este {contor_lower}.')
    print(f'Nr de caractere upper case este {contor_upper}.')


sir = input('Introduceti string-ul: ')
low_upp(sir)

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 8.
Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive.
"""
print('\nExercitiul 8: ')


def lista_pozitiva(numere):
    numere_pozitive = []
    for numar in numere:
        if numar >= 0:
            numere_pozitive.append(numar)
    return numere_pozitive


lista_numere = [1, -3, 4, -6, 7, -1, 0]
print(f'Lista initiala de numere: {lista_numere}')
print(f'Lista de numere pozitive: {lista_pozitiva(lista_numere)}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 9.
Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
    ● Primul număr x este mai mare decat al doilea nr y
    ● Al doilea nr y este mai mare decat primul nr x
    ● Numerele sunt egale.
"""
print('\nExercitiul 9: ')


def comparare_numere(a, b):
    if a > b:
        print(f'Numarul {a} este mai mare decat al doilea nr {b}.')
    elif a < b:
        print(f'Numarul {a} este mai mic decat al doilea nr {b}.')
    else:
        print('Numerele sunt egale.')


n1, n2 = input('Introduceti 2 numere: ').split()
comparare_numere(n1, n2)

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 10.
Funcție care primește un număr și un set de numere.
    ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
    ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
      returnează False
"""
print('\nExercitiul 10: ')


def adaugare_set(nr, numere):
    if nr in numere:
        print('Nu am adaugat numărul în set. Acesta există deja.')
        return False
    else:
        numere.add(nr)
        print('Am adaugat numărul nou în set.')
        return True


set_numere = {1, 3, 5, 7, 9}
print(f'Setul de numere: {set_numere}')
n = int(input('Introduceti nr ce doriti sa-l adaugam in set: '))
print(adaugare_set(n, set_numere))
print(f'Setul final de numere: {set_numere}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

# Exercitii OPTIONALE

"""
Exercitiul 1. - OPTIONAL
Funcție care primește o lună din an și returnează câte zile are acea luna
"""

print('\nExercitiul 1 - Optional:')


def nr_zile_luni(luna):
    lista_luni_31_zile = ['Ianuarie', 'Martie', 'Mai', 'Iulie', 'August',
                          'Octombrie', 'Decembrie']
    lista_luni_30_zile = ['Aprilie', 'Iunie', 'Septembrie', 'Noiembrie']

    an = int(input('Introduceti anul: '))
    if luna in lista_luni_31_zile:
        return 31
    elif luna in lista_luni_30_zile:
        return 30
    elif luna == 'Februarie':
        if an % 4 == 0:
            return 28
        else:
            return 27


month = input('Introduceti luna: ')
nr_zile = nr_zile_luni(month)
print(f'Luna {month} are {nr_zile} de zile.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 2. - OPTIONAL
Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea,
împărțirea a două numere.
În final vei putea face:
a, b, c, d = calculator(10, 2)
    ● print("Suma: ", a)
    ● print("Diferenta: ", b)
    ● print("Inmultirea: ", c)
    ● print("Impartirea: ", d)
'''
print('\nExercitiul 2 - Optional:')


def calculator(nr_1, nr_2):
    suma = int(nr_1) + int(nr_2)
    diff = int(nr_1) - int(nr_2)
    prod = int(nr_1) * int(nr_2)
    cat = int(nr_1) / int(nr_2)
    return suma, diff, prod, cat


a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 3. - OPTIONAL
Funcție care primește o lista de cifre (adică doar 0-9)
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
'''
# print('\nExercitiul 3 - Optional:')


def creare_dict(lista_cifre):
    dict_cifre = {0: lista_cifre.count(0), 1: lista_cifre.count(1), 2: lista_cifre.count(2),
                  3: lista_cifre.count(3), 4: lista_cifre.count(4), 5: lista_cifre.count(5),
                  6: lista_cifre.count(6), 7: lista_cifre.count(7), 8: lista_cifre.count(8),
                  9: lista_cifre.count(9)}
    return dict_cifre


cifre = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(f'Lista de numere este: {cifre}.')
print(f'Dict-ul care ne spune numarul de aparitie al cifrelor: {creare_dict(cifre)}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 4. - OPTIONAL
Funcție care primește 3 numere. Returnează valoarea maximă dintre ele
'''


print('\nExercitiul 4 - Optional:')


def maximul_3_numere(nr_1, nr_2, nr_3):
    if nr_1 > nr_2:
        if nr_3 > nr_1:
            maxim = nr_3
        else:
            maxim = nr_1
    elif nr_3 > nr_2:
        maxim = nr_3
    else:
        maxim = nr_2

    return maxim


a, b, c = input('Introduceti 3 numere: ').split()
print(f'Valoarea maxima dintre ele este: {maximul_3_numere(a, b, c)}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 5. - OPTIONAL
Funcție care să primească un număr și să returneze suma tuturor numerelor
de la 0 la acel număr
Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)
'''
print('\nExercitiul 5 - Optional:')


def suma_factoriala(n):
    suma = 0
    for i in range(n+1):
        suma += i
    return suma


nr = int(input('Introduceti un numar: '))
print(f'Suma numerelor pana la {nr}: {suma_factoriala(nr)}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

# Exercitii OPTIONALE - BONUS

'''
Exercitiul 1. - OPTIONAL - BONUS
Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați
numerele comune

Exemplu:
list1 = [1, 1, 2, 3]

list2 = [2, 2, 3, 4]
Răspuns: {2, 3}
'''
print('\nExercitiul 1 - Optional-Bonus:')


def intersectie_liste(lista_1, lista_2):
    return set(lista_1).intersection(lista_2)


list1 = [1, 1, 2, 3]
print(f'Lista 1: {list1}')
list2 = [2, 2, 3, 4]
print(f'Lista 2: {list2}')

print(f'Intersectia listelor: {intersectie_liste(list1,list2)}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 2. - OPTIONAL - BONUS
Funcție care să aplice o reducere de preț
Dacă produsul costa 100 lei și aplicăm reducere de 10%. Pretul va fi 90
Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e
invalidă.
'''


print('\nExercitiul 2 - Optional-Bonus:')

def reducere_pret(pret_produs):
    discount = int(input('Va rugam introduceti procentul de reducere: '))
    while discount < 0 or discount > 100:
        print('ATENTIE!!! Reducere invalida!')
        discount = int(input('Va rugam introduceti din nou procentul de reducere: '))
        break
    print(f'Pentru produsul cu pretul de {pret_produs} lei, s-a oferit o reducere de {discount}%.')
    pret_produs -= discount/100 * pret_produs
    print(f'Pretul final al produsului a devenit {pret_produs} lei.')


pret_prod = int(input('Introduceti pretul produsului: '))
reducere_pret(pret_prod)

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 3. - OPTIONAL - BONUS
Funcție care să afișeze data și ora curentă din ro
(bonus: afișați și data și ora curentă din China)
'''
print('\nExercitiul 3 - Optional-Bonus:')

# DATA si ORA CURENTA din ROMANIA
from _datetime import datetime
import pytz


def data_ora_curenta(locatia):
    if locatia == 'Romania':
        azi = datetime.now()
    else:
        azi = datetime.now(pytz.timezone(locatia))

    print(f'Data: {azi.strftime("%d-%m-%y")} si Ora: {azi.strftime("%H:%M:%S")}.')


print('Data si ora curenta din Romania: ')
data_ora_curenta('Romania')
print(' ')
print('Data si ora curenta din China: ')
data_ora_curenta('Hongkong')

# Afisarea datei si orei curente a oricarei tari
fusuri_orare = pytz.all_timezones  # din aceste fusuri orare alegi regiunea
print(f'Fusuri orare: {fusuri_orare}')
loc = input('Alegeti tara unde doriti sa aflati data si ora curenta: ')
data_ora_curenta(loc)

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 4. - OPTIONAL - BONUS
Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la
Crăciun dacă nu vrei să ne zici cand e ziua ta :)
'''
print('\nExercitiul 4 - Optional-Bonus:')
from datetime import date

def numaratoare_inversa_Ziua_mea():
    print('Ziua mea de nastere este: 02 Februarie ')
    ziua_mea = date(year = 2023, month = 2, day = 2)
    zile_ramase = (ziua_mea - date.today()).days
    print(f'Mai sunt inca {zile_ramase} de zile ramase pana atunci.')


numaratoare_inversa_Ziua_mea()

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------
