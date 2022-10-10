# TEMA 4  Functii( Flow Control -- Functii)

# Exercitii OBLIGATORII

"""
Exercitiul 1.
Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
    ● ‘Mașina mea preferată este x’.
    ● Fă același lucru cu un for each.
    ● Fă același lucru cu un while.
"""
print('\nExercitiul 1: ')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']

print('------ FOR ------')
for i in range(len(masini)):
    print(f'Masina mea preferata este {masini[i]}.')
print(' ')

print('------ FOR EACH------')
for masina in masini:
    print(f'Masina mea preferata este {masina}.')
print(' ')

print('------ WHILE ------')
i = 0
while i < len(masini):
    print(f'Masina mea preferata este {masini[i]}.')
    i += 1
print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 2.
Aceeași listă:
Folosește un for else
În for
    - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
      exceptând primul și ultimul.
În else:
    - Printează lista.
'''
print('\nExercitiul 2: ')

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
#           'Fiat', 'Trabant', 'Opel']

for i in range(1, len(masini) - 1):
    masini[i] = masini[i].upper()
else:
    print(f'Lista de masini finala este: {masini}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 3.
Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
    Printează ‘am găsit mașina dorită de dvs’
    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
    Printează ‘Am găsit mașina X. Mai căutam‘
'''
print('\nExercitiul 3: ')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
          'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('Am găsit mașina dorită de dvs.')
        break
    else:
        print(f'Am găsit mașina {masina}. Mai căutam...')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 4.
Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
    - Dacă mașina e Trabant sau Lăstun:
  Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
    - Printează S-ar putea să vă placă mașina x.
'''
print('\nExercitiul 4: ')

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
#           'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        continue
    else:
        print(f'S-ar putea sa va placa mașina {masina}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 5.
Modernizează parcul de mașini:
    ● Crează o listă goală, masini_vechi.
    ● Itereaza prin mașini.
    ● Când găsesti Lăstun sau Trabant:
        - Salvează aceste mașini în masini_vechi.
        - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).

    ● Printează Modele vechi: x.
    ● Modele noi: x.
'''
print('\nExercitiul 5: ')

masini_vechi = []
print('------ FOR ------')
for i in range(len(masini)):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f' Modele vechi: {masini_vechi}')
print(f' Modele noi: {masini}')
print(' ')

print('------ FOR EACH ------')
for masina in masini:
    if masina == 'Trabant' or masina == 'Lăstun':
        masini_vechi.append(masina)
        masina = 'Tesla'
print(f' Modele vechi: {masini_vechi}')
print(f' Modele noi: {masini}')
print(' ')

print('------ WHILE ------')
i = 0
while i < len(masini):
    if masini[i] == 'Trabant' or masini[i] == 'Lăstun':
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
    i += 1
print(f' Modele vechi: {masini_vechi}')
print(f' Modele noi: {masini}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 6.
Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.
    ● Prezintă doar mașinile care se încadrează în acest buget.
    ● Itereaza prin dict.items() și accesează mașina și prețul.
    ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
      xLastun
    ● Iterează prin listă.
'''
print('\nExercitiul 6: ')

pret_masini = {'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100,
               'Audi': 19000, 'BMW': 23000}
buget = 15000

for i in range(len(list(pret_masini.values()))):
    if list(pret_masini.values())[i] <= buget:
        print(f' Masinile care se incadreaza in acest buget sunt: {list(pret_masini.keys())[i]}')

# Iterare prin DICT.ITEMS()
for model, pret in pret_masini.items():
    print(f'Masina {model} - pret: {pret} euro.')
print('')
for model, pret in pret_masini.items():
    if pret <= buget:
        print(f'Pentru un buget de sub 15000 euro puteți alege masina {model}, avand pretul de {pret} euro.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 7.
Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
    ● Iterează prin ea.
    ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
print('\nExercitiul 7: ')

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print('------ FOR ------')
ok = 0  # Variabila in care se salveaza numarul aparitiilor lui 3
for i in range(len(numere)):
    if numere[i] == 3:
        ok += 1
print(f' Cifra 3 apare de {ok} ori in lista numere.')
print(' ')

print('------ FOR EACH ------')
ok = 0
for numar in numere:
    if numar == 3:
        ok += 1
print(f' Cifra 3 apare de {ok} ori in lista numere.')
print(' ')

print('------ WHILE ------')
ok = 0
i = 0
while i < len(numere):
    if numere[i] == 3:
        ok += 1
    i += 1
print(f' Cifra 3 apare de {ok} ori in lista numere.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 8.
Aceeași listă:
    ● Iterează prin ea
    ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
print('\nExercitiul 8: ')

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0

print('------ FOR ------')
for i in range(len(numere)):
    suma += numere[i]
print(f' Suma numerelor din lista este {suma}.')
print(' ')

print('------ FOR EACH ------')
suma = 0
for numar in numere:
    suma += numar
print(f' Suma numerelor din lista este {suma}.')
print(' ')

print('------ WHILE ------')
suma = 0
i = 0
while i < len(numere):
    suma += numere[i]
    i += 1
print(f' Suma numerelor din lista este {suma}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 9.
Aceeași listă:
    ● Iterează prin ea.
    ● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
print('\nExercitiul 9: ')

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim = numere[0]  # Cd primul element ca fiind cel mai mare din lista

print('------ FOR ------')
for i in range(len(numere)):
    if numere[i] > maxim:
        maxim = numere[i]
print(f' Cel mai mare numar: {maxim}.')
print(' ')

print('------ FOR EACH ------')
maxim = numere[0]
for numar in numere:
    if numar > maxim:
        maxim = numar
print(f' Cel mai mare numar: {maxim}.')
print(' ')

print('------ WHILE ------')
maxim = numere[0]
i = 0
while i < len(numere):
    if numere[i] > maxim:
        maxim = numere[i]
    i += 1
print(f' Cel mai mare numar: {maxim}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 10.
Aceeași listă:
    ● Iterează prin ea.
    ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
    ● Afișază noua listă.
'''
print('\nExercitiul 10: ')

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print('------ FOR ------')
print(f'Lista initiala: {numere}')
for i in range(len(numere)):
    if numere[i] <= 0:
        numere[i] = abs(numere[i])
    else:
        numere[i] = -abs(numere[i])
print(f'Noua lista de numere: {numere}.')
print(' ')

print('------ FOR EACH ------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(f'Lista initiala: {numere}')
for numar in numere:
    if numar <= 0:
        numar = abs(numar)
    else:
        numar = -abs(numar)
print(f'Noua lista de numere: {numere}.')
print(' ')

print('------ WHILE ------')
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(f'Lista initiala: {numere}')
i = 0
while i < len(numere):
    if numere[i] <= 0:
        numere[i] = abs(numere[i])
    else:
        numere[i] = -abs(numere[i])
    i += 1
print(f'Noua lista de numere: {numere}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

# Exercitii OPTIONALE

'''
Exercitiul 1. - OPTIONAL
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
    Itereaza prin listă alte_numere
    Populează corect celelalte liste
    Afișeaza cele 4 liste la final
'''
print('\nExercitiul 1 - Optional:')

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

print('------ FOR ------')
for i in range(len(alte_numere)):
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
    if alte_numere[i] >= 0:
        numere_pozitive.append(alte_numere[i])
    else:
        numere_negative.append(alte_numere[i])
print(f'Lista de numere pare: {numere_pare}.')
print(f'Lista de numere impare: {numere_impare}.')
print(f'Lista de numere pozitive: {numere_pozitive}.')
print(f'Lista de numere negative: {numere_negative}.')
print(' ')

print('------ FOR EACH ------')
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for numar in alte_numere:
    if numar % 2 == 0:
        numere_pare.append(numar)
    else:
        numere_impare.append(numar)
    if numar >= 0:
        numere_pozitive.append(numar)
    else:
        numere_negative.append(numar)
print(f'Lista de numere pare: {numere_pare}.')
print(f'Lista de numere impare: {numere_impare}.')
print(f'Lista de numere pozitive: {numere_pozitive}.')
print(f'Lista de numere negative: {numere_negative}.')
print(' ')

print('------ WHILE ------')
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
i = 0
while i < len(alte_numere):
    if alte_numere[i] % 2 == 0:
        numere_pare.append(alte_numere[i])
    else:
        numere_impare.append(alte_numere[i])
    if alte_numere[i] >= 0:
        numere_pozitive.append(alte_numere[i])
    else:
        numere_negative.append(alte_numere[i])
    i += 1
print(f'Lista de numere pare: {numere_pare}.')
print(f'Lista de numere impare: {numere_impare}.')
print(f'Lista de numere pozitive: {numere_pozitive}.')
print(f'Lista de numere negative: {numere_negative}.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 2. - OPTIONAL
Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
    https://www.youtube.com/watch?v=lyZQPjUT5B4
'''
print('\nExercitiul 2 - Optional ')

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

print('------ FOR ------')
print(f'Lista nesortata este: {alte_numere}')
aux = 0
for i in range(len(alte_numere)):
    for j in range(len(alte_numere) - 1):
        if alte_numere[j] > alte_numere[j + 1]:
            aux = alte_numere[j]
            alte_numere[j] = alte_numere[j + 1]
            alte_numere[j + 1] = aux
print(f'Lista ordonata este {alte_numere}')
print(' ')

print('------ WHILE ------')
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
print(f'Lista nesortata este: {alte_numere}')
for j in range(len(alte_numere)):
    swapped = False
    i = 0
    while i < len(alte_numere) - 1:
        if alte_numere[i] > alte_numere[i + 1]:
            alte_numere[i], alte_numere[i + 1] = alte_numere[i + 1], alte_numere[i]
            swapped = True
        i += 1
    if not swapped:
        break
print(f'Lista sortata este: {alte_numere}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 3. - OPTIONAL
Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr

Programul îi spune:
● Nr secret e mai mare
● Nr secret e mai mic
● Felicitări! Ai ghicit!
'''
print('\nExercitiul 3 - Optional: ')
import random
numar_secret = random.randrange(1, 30)

print('--- GHICITOARE DE NUMAR ---')
numar_ghicit = int(input('Ghiciti numarul(intre 1 si 30): '))
while numar_ghicit != numar_secret:
    # Daca nr introdus e mai mic ca cel generat
    if numar_ghicit < numar_secret:
        print(" Nr secret e mai mare.")
        numar_ghicit = int(input('Ghiciti iar: '))
    # Daca nr introdus e mai mare ca cel generat
    elif numar_ghicit > numar_secret:
        print(" Nr secret e mai mic.")
        numar_ghicit = int(input('Ghiciti iar: '))
    else:
        break
print(" Felicitări! Ai ghicit!")

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 4. - OPTIONAL
Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''
print('\nExercitiul 4 - Optional: ')

numar = int(input('Alege un numar: '))
for i in range(numar):
    for j in range(i + 1):
        print(i + 1, end="")
    print('')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 5. - OPTIONAL
tastatura_telefon = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9],
[0]
]
    Iterează prin listă 2d
    Printează ‘Cifra curentă este x’
    (hint: nested for - adică for în for)
'''
print('\nExercitiul 5 - Optional: ')

tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print('------ FOR ------')
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}.')
print(' ')

print('------ FOR EACH ------')
for lista in tastatura_telefon:
    for numar in lista:
        print(f'Cifra curenta este {numar}.')
print(' ')

print('------ WHILE ------')
i, j = 0, 0
while i < len(tastatura_telefon):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}.')
    i += 1

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------
