# TEMA 3  Structuri de date

# Exercitii OBLIGATORII

"""
Exercitiul 1.
Declară o listă note_muzicale în care să pui do re mi etc până la do
● Afișeaz-o
● Inversează ordinea folosind slicing și suprascrie această listă.
● Printează varianta actuală (inversată).
● Pe această listă aplică o metodă care bănuiești că face același lucru,
adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
deoarece metoda face asta automat.
● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
inițială.
Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
suprascrierea automat și permanentizează aceste modificări. Ambele variante
își găsesc utilitatea în funcție de ce ne dorim în acel moment.
"""
print('\nExercitiul 1: ')

# Definirea si Initializarea listei note_muzicale
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']

# Afisarea listei
print(f' Lista note muzicale: {note_muzicale}')

# Inversarea ordinii si Suprascrierea listei
note_muzicale = note_muzicale[::-1]

# Afisarea listei inversate
print(f' Lista inversata de note muzicale: {note_muzicale}')

# Inversarea listei folosind o metoda
note_muzicale.reverse()

# Afisarea rezultatului final
print(f' Lista inversata(cu aj. metodei) de note muzicale: {note_muzicale}')

# ------------------------------------------------------------------------------

'''
Exercitiul 2.
De câte ori apare ‘do’?
'''
print('\nExercitiul 2: ')

count_do = 0  # Variabila care contine nr aparitiilor in lista ale lui DO
for i in note_muzicale:
    if i == 'do':
        count_do += 1

print(f' DO apare de {count_do} ori.')

# ------------------------------------------------------------------------------

'''
Exercitiul 3.
Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
Găsește 2 variante să le unești într-o singură listă.
'''
print('\nExercitiul 3: ')

lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]

# I Varianta
lista1.extend(lista2)
print(f'Lista extinsa: {lista1}')

# II Varianta
lista1 = [3, 1, 0, 2]  # Suprascriere pentru a putea rula deodata Variantele
lista_v2 = lista1 + lista2
print(f'Lista extinsa: {lista_v2}')

# ------------------------------------------------------------------------------

'''
Exercitiul 4.
● Sortează și afișază lista generată la exercițiul anterior.
● Sortează numărul 0 folosind o funcție.
● Afișaza iar lista.
'''
print('\nExercitiul 4: ')

# Voi folosi lista_v2 pentru contine toate elementele
lista_numere = lista_v2
lista_numere.sort()
print(f' Lista de numere sortata: {lista_numere}')

# ------------------------------------------------------------------------------

'''
Exercitiul 5.
Folosind un if verifică lista generată la exercițiul 3 și afișază:
● Lista este goală.
● Lista nu este goală.
'''
print('\nExercitiul 5: ')

if lista_numere:
    print('Lista nu este goală')
else:
    print('Lista este goală')

# ------------------------------------------------------------------------------

'''
Exercitiul 6.
Folosește o funcție care să șteargă lista de la exercițiul 3.
'''
print('\nExercitiul 6: ')

# Stergerea listei de numere
lista_numere.clear()

# ------------------------------------------------------------------------------

'''
Exercitiul 7.
Copy paste la exercițiul 5. Verifică încă o dată.
Acum ar trebui să se afișeze că lista e goală.
'''
print('\nExercitiul 7: ')

if lista_numere != []:
    print('Lista nu este goală')
else:
    print('Lista este goală')

# ------------------------------------------------------------------------------

'''
Exercitiul 8.
Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
Folosește o funcție că să afișezi Elevii (cheile)
'''
print('\nExercitiul 8: ')

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

# Afisarea elevilor
print(f' Elevii sunt: {dict1.keys()}')

# ------------------------------------------------------------------------------

'''
Exercitiul 9.
Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie
'''
print('\nExercitiul 9: ')

# Crearea unei liste care contine numele elevilor
nume_elevi = list(dict1.keys())

# Afisarea elevilor si a notelor lor sub forma dorita
for i in range(len(dict1)):
    print(f' {nume_elevi[i]} a luat nota {dict1.get(nume_elevi[i])}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 10.
Dorel a făcut contestație și a primit 6
● Modifică nota lui Dorel în 6
● Printează nota după modificare
'''
print('\nExercitiul 10: ')

# Modificarea notei lui Dorel
dict1['Dorel'] = 6

# Afisarea notei dupa modificare
print(f' Nota lui {nume_elevi[2]} este {dict1["Dorel"]}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 11.
Gigel se transferă din clasă
● Căuta o funcție care să îl șteargă
● Vine un coleg nou. Adaugă Ionică, cu nota 9
● Printează noii elevi
'''
print('\nExercitiul 11: ')

# Stergerea elevului Gigel
dict1.pop('Gigel')

# Adaugarea lui Ionica, nota 9
dict1['Ionica'] = 9

# Afisarea elevilor
nume_elevi = list(dict1.keys())  # Actualizarea listei cu numele elevilor
for i in range(len(dict1)):
    print(f' {nume_elevi[i]} a luat nota {dict1.get(nume_elevi[i])}.')

# ------------------------------------------------------------------------------

'''
Exercitiul 12.
Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
● Adaugă în zilele_sapt ‘luni’
● Afișeaza zile_sapt
'''
print('\nExercitiul 12: ')

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}

# Adaugare - cum elementul exista deja, el nu va fi adaugat
zile_sapt.add('luni')

# Afisare
print(f' Set zile_sapt: {zile_sapt}')

# ------------------------------------------------------------------------------

'''
Exercitiul 13.
Folosește un if și verifică dacă:
● Weekend este un subset al zilelor din săptămâna.
● Weekend nu este un subset al zilelor din săptămâna.
'''
print('\nExercitiul 13: ')

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămâna.')
else:
    print('Weekend nu este un subset al zilelor din săptămâna.')

# ------------------------------------------------------------------------------

'''
Exercitiul 14.
Afișează diferențele dintre aceste 2 seturi.
'''
print('\nExercitiul 14: ')

print(f'Diferenta dintre seturi: {zile_sapt-weekend}')  # I Varianta
print(f'Diferenta dintre seturi: {zile_sapt.difference(weekend)}')  # II Varianta

# ------------------------------------------------------------------------------

'''
Exercitiul 15.
Afișază intersecția elementelor din aceste 2 seturi.
'''
print('\nExercitiul 15: ')

print(f'Intersectia dintre seturi: {zile_sapt.intersection(weekend)}')

# ------------------------------------------------------------------------------

# # Exercitii OPTIONALE
#
# '''
# Exercitiul 1. - OPTIONAL
# Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
# Google search hint
# “how to check if item îs în list python”
# '''
# print('\nExercitiul 1 - Optional: ')
#
# echipa_fotbal = []  # Declararea listei
# n = 5  # Nr de jucatori
# for i in range(n):
#     # Introducerea de la tastatura a jucatorilor
#     echipa_fotbal.append(input(f'Introduceti jucatorul nr. {i + 1}: '))
#
# print(f' Jucatori in teren: {echipa_fotbal}')
#
# # Schimbari in echipa
# nr_schimbari = 0
#
# # Crearea unui dict pentru vizualizarea jucatorilor din teren
# teren = {echipa_fotbal[0]: True, echipa_fotbal[1]: True, echipa_fotbal[2]: True,
#          echipa_fotbal[3]: True, echipa_fotbal[4]: True}
#
# while nr_schimbari < 3:
#     jucator_schimbat, jucator_nou = input(f' Ce jucator doresti sa schimbi si cine intra? ').split()
#     for i in range(len(echipa_fotbal)):  # Identificam jucatorul
#         # Daca jucatorul se afla in echipa
#         if jucator_schimbat == echipa_fotbal[i]:
#             # Daca jucatorul se afla in teren
#             if teren.get(echipa_fotbal[i]):
#                 # Se efectueaza schimbarea
#                 # Scoaterea jucatorului din teren
#                 teren[echipa_fotbal[i]] = False
#                 # Eliminarea jucatorului din lista
#                 echipa_fotbal.remove(echipa_fotbal[i])
#                 # Adaugarea jucatorului nou in lista
#                 echipa_fotbal.insert(i, jucator_nou)
#                 # Intrarea in teren a jucatorului nou
#                 teren[echipa_fotbal[i]] = True
#                 # Contorizarea schimbarii
#                 nr_schimbari += 1
#                 # Afisaj
#                 print(f' A intrat {jucator_nou}, a iesit {jucator_schimbat}, mai ai {3 - nr_schimbari} schimbari.')
#             else:
#                 print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_schimbat} nu e in teren! ')
#                 print(f'Mai ai {3 - nr_schimbari} schimbari.')
#         else:
#             print(f' Jucatorul {jucator_schimbat} nu se afla in echipa. Prin urmare, nu se poate face schimbarea.')
#             print(f'Mai ai {3 - nr_schimbari} schimbari.')
# # Mesaj final
# print(f'Ati realizat numarul maxim de schimbari!')
