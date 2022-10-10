# TEMA 1 - Setup, Variabile, Tipuri de date

# Exercitii OBLIGATORII

"""
Exercitiul 1.
   În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
"""

# Variabila = o valoare care este tinuta in zona de memorie
#             o cutie in care depozitam o valoare

# ------------------------------------------------------------------------------

'''
Exercitiul 2. 
Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
Observație: Valorile vor fi alese de tine după preferințe.
'''
# Variabila String - Declarare si Initializare
prenume = 'Andreea'

# Variabila Int(Integer) - Declarare si Initializare
an_nastere = 2001

# Variabila Float - Declarare si Initializare
media = 8.9999

# Variabila Boolean - Declarare si Initializare
gen_feminin = True

print('\nExercitiul 2: ')

# Afisarea acestor variabile in consola
print(f'String: {prenume}, Int: {an_nastere}, Float: {media}, Boolean: {gen_feminin}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 3.
Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
'''
print('\nExercitiul 3: ')

print('Afisarea tipului de date al variabilelor: ')
print(f'{prenume} este de tip: {type(prenume)}.')
print(f'{an_nastere} este de tip: {type(an_nastere)}.')
print(f'{media} este de tip: {type(media)}.')
print(f'{gen_feminin} este de tip: {type(gen_feminin)}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 4. 
Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia.
'''
print('\nExercitiul 4: ')

# Rotunjirea float-ului
media = round(media)
# Afisarea tipului de date
print(f'\n{media} este de tip: {type(media)}.')  # Tipul de date va fi INT

# ------------------------------------------------------------------------------

'''
Exercitiul 5. 
Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
Rezolvă nepotrivirile de tip prin ce modalitate dorești.
'''
print('\nExercitiul 5: ')

# I Varianta de printare
print('I varianta de printare: ')
print(f'Variabila String: {prenume}.')
print(f'Variabila Int: {an_nastere}.')
print(f'Variabila Float(transformata in Int dupa rotunjire): {media}.')
print(f'Variabila Boolean: {gen_feminin}.')
# II Varianta de printare
print('\nII varianta de printare: ')
print('Variabila String: ', prenume, '.')
print('Variabila Int: ', an_nastere, '.')
print('Variabila Float(transformata in Int dupa rotunjire):', media, '.')
print('Variabila Boolean: ', gen_feminin, '.')

# ------------------------------------------------------------------------------

'''
Exercitiul 6.
Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
print('\nExercitiul 6: ')

# Citire de la tastatura a 2 string-uri
numele = input('Introduceti numele: ')
prenumele = input('Introduceti prenumele: ')
# Afisare
print(f' Numele complet {numele} {prenumele} are {len(numele) + len(prenumele)} caractere.')

# ------------------------------------------------------------------------------

'''
Exercitiul 7.
Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.
'''
print('\nExercitiul 7: ')

# Citire de la tastatura a 2 int-uri
lungimea = int(input('Introduceti lungimea dreptunghiului: '))
latimea = int(input('Introduceti latimea dreptunghiului: '))
# Afisare
print(f' Aria dreptunghiuli cu lungimea de {lungimea}cm si latimea de {latimea}cm este de {latimea * lungimea}cm^2.')

# ------------------------------------------------------------------------------

'''
Exercitiul 8.
Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';

'''
print('\nExercitiul 8: ')

statement = 'Coral is either the stupidest animal or the smartest rock'
count = 0
for i in range(0, len(statement)):
    if statement[i] == 't' and statement[i + 1] == 'h' and statement[i + 2] == 'e':
        count += 1

# ------------------------------------------------------------------------------

'''
Exercitiul 9.
Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.

'''
print('\nExercitiul 9: ')

# statement = 'Coral is either the stupidest animal or the smartest rock'
count = 0
for i in range(0, len(statement)):
    if statement[i] == 't' and statement[i + 1] == 'h' and statement[i + 2] == 'e':
        count += 1

# Printarea nr de repetitii al cuvantului 'the'
print(f' Cuvantul "the" apare in propozitie de {count} ori.')

# ------------------------------------------------------------------------------

'''
Exercitiul 10.
Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.

'''
print('\nExercitiul 10: ')

# statement = 'Coral is either the stupidest animal or the smartest rock'

assert not statement.isnumeric(), 'Stringul contine doar numere.'
print(f'Stringul "{statement}" nu contine doar numere.')


# ------------------------------------------------------------------------------

# Exercitii OPTIONALE

'''
Exercitiul 1. - OPTIONAL
Exercițiu:
- citește de la tastatură un string de dimensiune impară;
- afișează caracterul din mijloc.
'''
print('\nExercitiul 1 - Optional: ')

sir = input('Introduceti string-ul: ')
for i in range(0, len(sir)):
    if len(sir) % 2 == 0:
        print(' Sirul nu are dimensiune impara!')
        sir = input('Reintroduceti string-ul: ')

caracter_mij = int((len(sir) - 1) / 2)
print(f' Caracterul din mijlocul sirului: {sir[caracter_mij]}')

# ------------------------------------------------------------------------------

'''
Exercitiul 2. - OPTIONAL
Folosind assert, verifică dacă un string este palindrom.
'''
print('\nExercitiul 2 - Optional: ')

mes = input("Introduceti cuvantul si vedeti daca este palindrom:  ")
if mes != mes[::-1]:  # mes[::-1] inverseaza valoarea string-ului dat
    print(f"Cuvantul {mes} nu este palindrom.")
else:
    print(f"Cuvantul {mes} este palindrom.")

# ------------------------------------------------------------------------------

'''
Exercitiul 3. - OPTIONAL
Folosind o singură linie de cod :
- citește un string de la tastatură (ex: 'alabala portocala');
- salvează fiecare cuvânt într-o variabilă;
- printează ambele variabile pentru verificare.
'''
print('\nExercitiul 3 - Optional: ')
m1, m2 = input('Introduceti 2 cuvinte: ').split()
# Afisarea variabilelor - verificare
print(m1)
print(m2)

# ------------------------------------------------------------------------------

'''
Exercitiul 4. - OPTIONAL
Exercițiu:
- citește un string de la tastatură (ex: alabala portocala);
- salvează primul caracter într-o variabilă - indiferent care este el, încearcă
cu 2 stringuri diferite;
- capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
caracter => alAbAlA portocAla.
'''
print('\nExercitiul 4 - Optional: ')

text = input('Introduceti textul: ')
# Variabila in care se salveaza primul caracter al sirului
a = text[0]
# String-ul in care se salveaza textul capitalizat
new_text = ''
for i in range(len(text)):
    # Verificam fiecare caracter al sirului daca este la fel cu primul caracter al sirului
    if text[i] == a and text[i].islower():
        # Daca sunt la fel si nu este deja majuscula , atunci trasformam caracterul in majuscula
        new_text += text[i].upper()
    else:
        # Altfel, pastram caracterul in sirul final asa cum e
        new_text += text[i]

# Modelam sirul de caractere rezultat a.i. primul si ultimul caracter sa fie scrise cu litera mica
new_text = new_text[0].lower() + new_text[1:-1] + new_text[-1].lower()

print(f' Afisati textul final: {new_text}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 5. - OPTIONAL
Exercițiu:
- citește un user de la tastatură;
- citește o parolă;
- afișează: 'Parola pt user x este ***** și are x caractere';
- ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
afișeze corect.
eg: parola abc => ***
parola abcd => ****
'''

print('\nExercitiul 5 - Optional: ')

# Citire de la tastatura a 2 string-uri
user = input('Introduceti numele user-ului: ')
parola = input('Introduceti parola: ')

psw = ''  # Parola secretizata
for i in range(len(parola)):
    # in psw se adauga '*' pentru fiecare caracter aflat in parola introdusa
    psw += '*'

# Afisare
print(f' Parola pentru userul {user} este {psw} si are {len(psw)} caractere.')
