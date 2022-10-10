# TEMA 2 - Operatori, condiționale

# Exercitii OBLIGATORII

"""
Exercitiul 1.
Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
"""
import random

'''
 Sintaxa: if (...conditie...): ..........
          else (.....): ........... () - nu sunt obligatorii
     In cazul in care conditia este True, atunci se executa instructiunile care
     se afla dupa cele ':' ale lui if
     In caz contrar, se executa setul de instructiuni aflate in dreptul lui else
'''

# ------------------------------------------------------------------------------
# Definirea si Initializarea lui X
X = int(input('Introduceti un numar intreg: '))

'''
Exercitiul 2.
Verifică și afișează dacă x este număr natural sau nu.
'''
print('\nExercitiul 2: ')

if X >= 0:
    print(f'Numarul {X} este un numar natural!')
else:
    print(f'Numarul {X} nu este un numar natural!')
# ------------------------------------------------------------------------------

'''
Exercitiul 3.
Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
'''
print('\nExercitiul 3: ')

if X > 0:
    print(f' Numarul {X} este pozitiv!')
elif X == 0:
    print(f' Numarul {X} este neutru!')
else:
    print(f' Numarul {X} este negativ!')

# ------------------------------------------------------------------------------

'''
Exercitiul 4.
Verifică și afișează dacă x este între -2 și 13.
'''
print('\nExercitiul 4: ')

minim = -2
maxim = 13
if minim <= X <= maxim:
    print(f'Numarul {X} se afla in intervalul [{minim},{maxim}].')
else:
    print(f'Numarul {X} nu se afla in intervalul [{minim},{maxim}].')

# ------------------------------------------------------------------------------

'''
Exercitiul 5.
Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
'''
print('\nExercitiul 5: ')

Y = int(input('Introduceti valoarea lui Y: '))
if (X - Y) < 5:
    print(f' Diferenta dintre {X} si {Y} este mai mica decat 5(ea fiind {X - Y}).')
else:
    print(f' Diferenta dintre {X} si {Y} nu este mai mica decat 5(ea fiind {X - Y}).')

# ------------------------------------------------------------------------------

'''
Exercitiul 6.
Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''
print('\nExercitiul 6: ')

minim = 5
maxim = 27
if not minim <= X <= maxim:
    print(f'Numarul {X} nu se afla in intervalul [{minim},{maxim}].')
else:
    print(f'Numarul {X} se afla in intervalul [{minim},{maxim}].')

# ------------------------------------------------------------------------------

'''
Exercitiul 7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
'''
print('\nExercitiul 7: ')

if X == Y:
    print(f' Numerele X={X} si Y={Y} sunt egale.')
elif X > Y:
    print(f'Numarul X={X} este mai mare ca numarul Y={Y}.')
else:
    print(f'Numarul Y={Y} este mai mare ca numarul X={X}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 8.
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
print('\nExercitiul 8: ')

Z = int(input(' Introduceti valoarea celei de-a treia laturi: '))

if X == Y == Z:
    print(f' Triunghiul cu laturile: x={X}, y={Y} si z={Z} este echilateral.')
elif X == Y or X == Z or Y == Z:
    print(f' Triunghiul cu laturile: x={X}, y={Y} si z={Z} este isoscel.')
else:
    print(f' Triunghiul cu laturile: x={X}, y={Y} si z={Z} este oarecare.')

# ------------------------------------------------------------------------------

'''
Exercitiul 9.
Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu
'''
print('\nExercitiul 9: ')

litera = input('Introduceti o litera: ')

if litera == 'A' or litera == 'a' or litera == 'E' or litera == 'e' or litera == 'I' \
        or litera == 'i' or litera == 'O' or litera == 'o' or litera == 'U' or litera == 'u':
    print(f'Litera {litera} este o vocala!')
elif litera.isnumeric():
    print(f'Caracterul {litera} este un numar!')
elif litera == '.' or litera == ',' or litera == ':' or litera == ';' or litera == '!' \
        or litera == '?':
    print(f'Caracterul {litera} este un semn de punctuatie!')
else:
    print(f'Litera {litera} este o consoana!')

# ------------------------------------------------------------------------------

'''
Exercitiul 10.
Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F
'''
print('\nExercitiul 10: ')

# Introducearea mai multor note deodata
note_initiale = list(map(int, input('Introduceti notele: ').split()))
# Afisarea notelor introduse in consola
print(f'Notele in sistem romanesc: {note_initiale}')

for i in range(len(note_initiale)):
    if note_initiale[i] < 0 or note_initiale[i] > 10:
        print('Nota introdusa nu este corecta: ')
        note_initiale[i] = int(input('Reintroduceti nota: '))

for i in range(len(note_initiale)):
    if note_initiale[i] <= 4:
        note_initiale[i] = 'F'
    elif 4 < note_initiale[i] <= 6:
        note_initiale[i] = 'E'
    elif 6 < note_initiale[i] <= 7:
        note_initiale[i] = 'D'
    elif 7 < note_initiale[i] <= 8:
        note_initiale[i] = 'C'
    elif 8 < note_initiale[i] <= 9:
        note_initiale[i] = 'B'
    else:
        note_initiale[i] = 'A'

print(f'Notele in sistem european: {note_initiale}')

# ------------------------------------------------------------------------------

# Exercitii OPTIONALE

'''
Exercitiul 1. - OPTIONAL
Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
'''
print('\nExercitiul 1 - Optional: ')

nr = 0  # Variabila care contine nr de cifre al numarului X
X_initial = X
while X != 0:
    X = int(X / 10)
    nr += 1
if nr >= 4:
    print(f'Nr {X_initial} are minim 4 cifre ({nr} cifre).')
else:
    print(f'Nr {X_initial} nu are minim 4 cifre(doar {nr} cifre).')

# ------------------------------------------------------------------------------

'''
Exercitiul 2. - OPTIONAL
Verifică dacă x are exact 6 cifre.
'''
print('\nExercitiul 2 - Optional: ')

# nr - variabila ce contine nr de cifre al nr X
if nr == 6:
    print(f'Nr {X_initial} are {nr} cifre.')
else:
    print(f'Nr {X_initial} nu are 6 cifre(doar {nr} cifre).')

# ------------------------------------------------------------------------------

'''
Exercitiul 3. - OPTIONAL
Verifică dacă x este număr par sau impar (x e int).
'''
print('\nExercitiul 3 - Optional: ')

# X_initial - variabila care contine valoarea lui X introdusa de la tastatura
if int(X_initial) % 2 == 0:
    print(f'Nr X={X_initial} este numar PAR.')
else:
    print(f'Nr X={X_initial} este numar IMPAR.')
# ------------------------------------------------------------------------------

'''
Exercitiul 4. - OPTIONAL
x, y, z (int)
Afișează care este cel mai mare dintre ele?
'''
print('\nExercitiul 4 - Optional: ')

# Sa cunoastem numerele, le mai printam o data
print(f' X={X_initial}, Y={Y}, Z={Z} ')
maximul = 0  # Variabila in care vom salva cel mai mare numar
if X_initial > Y:
    if Z > X_initial:
        maximul = Z
    else:
        maximul = X_initial
elif Z > Y:
    maximul = Z
else:
    maximul = Y

print(f' Cel mai mare numar dintre ele este: {maximul}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 5. - OPTIONAL
X, y, z - reprezintă unghiurile unui triunghi
Verifică și afișează dacă triunghiul este valid sau nu.
'''
print('\nExercitiul 5 - Optional: ')
X, Y, Z = input('Introduceti unghiurile triunghiului(in °): ').split()
if int(X) + int(Y) + int(Z) == 180:
    print('Triunghiul este valid!')
else:
    print('Triunghiul NU este valid!!!')

# ------------------------------------------------------------------------------

'''
Exercitiul 6. - OPTIONAL
Având stringul: 'Coral is either the stupidest animal or the smartest rock'
● Citiți de la tastatură un int x
● Afișează stringul fără ultimele x caractere
Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
'''
print('\nExercitiul 6 - Optional: ')

statement = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('x= '))
statement_final = statement[0:(len(statement) - x)]
if x == 1:
    print(f'String-ul fara {x} caracter: "{statement_final}"')
else:
    print(f'String-ul fara {x} caractere: "{statement_final}"')

# ------------------------------------------------------------------------------

'''
Exercitiul 7. - OPTIONAL
Același string. Declară un string nou care să fie format din primele 5 caractere
+ ultimele 5
'''
print('\nExercitiul 7 - Optional: ')

# statement = 'Coral is either the stupidest animal or the smartest rock'
new_statement = statement[:5] + statement[-5:]
print(f'Noul string: {new_statement}')

# ------------------------------------------------------------------------------

'''
Exercitiul 8. - OPTIONAL
Același string.
● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
este o funcție care te ajuta sa faci asta)
● Folosind această variabilă + slicing, afișează tot stringul până la acest
cuvant
● output: 'Coral is either the stupidest animal or the smartest '
'''
print('\nExercitiul 8 - Optional: ')

# statement = 'Coral is either the stupidest animal or the smartest rock'
index = statement.find('rock')
print(f' Mesajul final: "{statement[:index]}".')

# ------------------------------------------------------------------------------

'''
Exercitiul 9. - OPTIONAL
Citește de la tastatura un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
'''
print('\nExercitiul 9 - Optional: ')

mesaj = input('Introduceti un cuvant: ')
assert any(mesaj[0]) == any(mesaj[len(mesaj) - 1])
print('Primul si ultimul caracter sunt aceleasi! ')

# ------------------------------------------------------------------------------

'''
Exercitiul 10. - OPTIONAL
Avand stringul '0123456789'
● Afișați doar numerele pare
● Afișați doar numerele impare
(hint: folositi slicing, controlați din pas)
'''
print('\nExercitiul 10 - Optional: ')

# Declararea si Initializarea string-ului
numere = '0123456789'
nr_pare = ''  # String-ul care va contine nr PARE
nr_impare = ''  # String-ul care va contine nr IMPARE

# Afisarea nr PARE
for i in range(0, len(numere), 2):
    nr_pare += numere[i]
print(f' Numerele pare din sir sunt: {nr_pare}')

# Afisarea nr IMPARE
for i in range(1, len(numere), 2):
    nr_impare += numere[i]
print(f' Numerele impare din sir sunt: {nr_impare}')

# ------------------------------------------------------------------------------

# Exercitii BONUS

import time

'''
Exercitiul 11. - BONUS
Joc ghicit zarul
Caută pe net și vezi cum se generează un număr random
Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
Luați un numărul ghicit de la utilizator
Verificați și afișați dacă utilizatorul a ghicit
Veți avea 3 opțiuni
● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
● Ai ghicit. Felicitari! Ai ales x si zarul a fost y
'''
print('\nExercitiul 11 - Bonus: ')

# Scrierea unui mesaj de bun venit in joc
print("Bun venit in Jocul Ghicitul Zarului! \n Ai doar 3 incercari! ")

# 2s intarziere
time.sleep(2)

# Generarea unui numar random
dice_roll = random.randrange(1, 6)

# Luarea nr de la utilizator
zar = int(input('Ghiciti numarul: '))
count = 1  # contorizeaza nr incercarilor
while zar != dice_roll and count < 3:
    # Daca nr introdus e mai mic ca cel generat
    if zar < dice_roll:
        print(" Prea mic!")
        print(f'Mai ai {3 - count} incercari!')
        zar = int(input('Ghiciti iar: '))
        count += 1
    # Daca nr introdus e mai mare ca cel generat
    elif zar > dice_roll:
        print(" Prea mare!")
        print(f'Mai ai {3-count} incercari!')
        zar = int(input('Ghiciti iar: '))
        count += 1
    else:
        break

# Mesaj final
if zar == dice_roll:
    print(f'**** Ati ghicit!!! **** \n Ai ales {zar} si zarul a fost {dice_roll}.')
    time.sleep(2)
    print(' FELICITARI! ')
elif zar > dice_roll:
    print(f' Ai pierdut! Ai ales un numar mai mare. Ai ales {zar} dar a fost {dice_roll}.')
else:
    print(f' Ai pierdut! Ai ales un numar mai mic. Ai ales {zar} dar a fost {dice_roll}.')

# ------------------------------------------------------------------------------
