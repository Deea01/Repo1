# TEMA 6  OOP - Clase & Obiecte

# Exercitii OBLIGATORII

"""
Exercitiul 1.
  Clasa Cerc
  Atribute: raza, culoare
  Constructor pentru ambele atribute
  Metode:
    ● descrie_cerc() - va PRINTA culoarea și raza
    ● aria() - va RETURNA aria
    ● diametru()
    ● circumferinta()
"""
print('\nExercitiul 1: ')


class Cerc:
    # Atribute
    raza = 0
    culoare = None

    # Constructor
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # Metode
    def descrie_cerc(self):
        print(f'Culoarea cercului este {self.culoare} si are raza de {self.raza} cm.')

    def aria(self):
        PI = 3.14
        return PI * (self.raza ** 2)

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        PI = 3.14
        return 2 * PI * self.raza


cerculet_1 = Cerc(3, 'galben')
print(f'Aria cercului 1: {cerculet_1.aria()}')
print(f'Diametrul cercului 1: {cerculet_1.diametru()}')
print(f'Circumferinta cercului 1: {cerculet_1.circumferinta()}')
cerculet_1.descrie_cerc()

print(' ')

cerculet_2 = Cerc(4, 'roz')
print(f'Aria cercului 2: {cerculet_2.aria()}')
print(f'Diametrul cercului 2: {cerculet_2.diametru()}')
print(f'Circumferinta cercului 2: {cerculet_2.circumferinta()}')
cerculet_2.descrie_cerc()

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 2.
  Clasa Dreptunghi
  Atribute: lungime, latime, culoare
  Constructor pentru toate atributele
  Metode:
    ● descrie()
    ● aria()
    ● perimetrul()
    ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
  Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
"""
print('\nExercitiul 2: ')


class Dreptunghi:
    # Atribute
    lungime = 0
    latime = 0
    culoare = None

    # Constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    # Metode
    def descrie(self):
        print(f'Dreptunghiul de lungime {self.lungime} cm, latime {self.latime} cm are culoarea {self.culoare}.')

    def aria(self):
        return float(self.latime) * float(self.lungime)

    def perimetru(self):
        return 2 * (float(self.latime) + float(self.lungime))

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


# Verificarea metodei schimba culoarea
rectangle_1 = Dreptunghi(3, 4, 'mov')
rectangle_1.descrie()
rectangle_1.schimba_culoarea('alb')
rectangle_1.descrie()
print(f'Perimetrul dreptunghiului 1 este: {rectangle_1.perimetru()}')
print(f'Aria dreptunghiului 1: {rectangle_1.aria()}')
print(' ')

rectangle_2 = Dreptunghi(4, 4, 'portocaliu')
rectangle_2.descrie()
rectangle_2.schimba_culoarea('alb')
rectangle_2.descrie()
print(f'Perimetrul dreptunghiului 2 este: {rectangle_2.perimetru()}')
print(f'Aria dreptunghiului 2: {rectangle_2.aria()}')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 3.
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
"""
print('\nExercitiul 3: ')


class Angajat:
    # Atribute
    nume = None
    prenume = None
    salariu = 0

    # Constructor
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    # Metode
    def descrie(self):
        print(f' Angajatul {self.nume} {self.prenume} are salariul de {self.salariu} lei.')

    def nume_complet(self):
        print(f'Numele complet al angajatului este: {self.nume} {self.prenume}.')

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return float(self.salariu) * 12

    def marire_salariu(self, procent):
        while procent < 0 or procent > 100:
            print('Eroare!!!Procent invalid!')
            procent = int(input('Introduceti din nou procentul: '))
            break
        self.salariu += procent / 100 * self.salariu


angajat_1 = Angajat('Domut', 'Andreea', 2000)
print('Angajatul nr. 1: ')
angajat_1.descrie()
angajat_1.nume_complet()
print(f'Salariul lunar al angajatului 1: {angajat_1.salariu_lunar()}')
print(f'Salariul anual al angajatului 1: {angajat_1.salariu_anual()}')
procent_marire_salar = int(input('Introduceti procentul de marire:'))
angajat_1.marire_salariu(procent_marire_salar)
angajat_1.descrie()

print(' ')

angajat_2 = Angajat('Pop', 'Calin', 3000)
print('Angajatul nr. 2: ')
angajat_2.descrie()
angajat_2.nume_complet()
print(f'Salariul lunar al angajatului 2: {angajat_2.salariu_lunar()}')
print(f'Salariul anual al angajatului 2: {angajat_2.salariu_anual()}')
procent_marire_salar = int(input('Introduceti procentul de marire:'))
angajat_2.marire_salariu(procent_marire_salar)
angajat_2.descrie()

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

"""
Exercitiul 4.
  Clasa Cont
  Atribute: iban, titular_cont, sold
  Constructor pentru toate atributele
  Metode:
    ● afisare_sold() - Titularul x are în contul y suma de n lei
    ● debitare_cont(suma)
    ● creditare_cont(suma)
"""
print('\nExercitiul 4: ')


class Cont:
    iban = None
    titular_cont = None
    sold = 0

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f' Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

    def debitare_cont(self, suma):
        while suma > self.sold:
            suma = int(input('Transfer bancar imposibil! Suma depaseste soldul contului curent! '
                             'Va rugam introduceti alta suma: '))
            break
        self.sold -= suma
        print(f'Transfer bancar realizat cu succes! Mai aveti in cont {self.sold} lei.')

    def creditare_cont(self, suma):
        self.sold += suma
        print(f'Suma de {suma} lei a fost adaugata cu succes! In prezent, aveti {self.sold} lei.')


cont_1 = Cont('ROBTRLRON000000000', 'Domut Andreea', 3000)
print('Contul nr. 1')
cont_1.afisare_sold()
transfer_bancar = int(input('Introduceti suma necesara pentru transferul bancar: '))
cont_1.debitare_cont(transfer_bancar)
cont_1.creditare_cont(350)

cont_2 = Cont('ROBTRLRON11111111', 'Dan Miruna', 3000)
print('Contul nr. 2')
cont_2.afisare_sold()
transfer_bancar = int(input('Introduceti suma necesara pentru transferul bancar: '))
cont_2.debitare_cont(transfer_bancar)
cont_2.creditare_cont(400)

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

# Exercitii OPTIONALE

"""
Exercitiul 1. - OPTIONAL
  Clasa Factura
  Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
            avea aceeași serie), număr, nume_produs, cantitate, pret_buc
  Constructor: toate atributele, fara serie
  Metode:
      ● schimbă_cantitatea(cantitate)
      ● schimbă_prețul(pret)
      ● schimbă_nume_produs(nume)
      ● generează_factura() - va printa tabelar dacă reușiți
  Factura seria x numar y
  Data: generați automat data de azi
  Produs | cantitate | preț bucată | Total
  Telefon | 7 | 700 | 49000
  Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/ """

print('\nExercitiul 1 - Optional:')
from datetime import date


class Factura:
    seria = 'SRL 020202'
    numar = 0
    nume_produs = None
    cantitate = 0
    pret_buc = 0

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self,nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        print(f'Factura seria {self.seria} numar {self.numar}')
        print(f'Data: {date.today()} ')
        print(f'Produs | Cantitate | Pret bucata | Total ')
        print(f'{self.nume_produs} |     {self.cantitate}     |     {self.pret_buc}     |  {self.numar*self.pret_buc}  ')


factura_1 = Factura(20, 'Masina', 2, 100)
print('Factura nr. 1 initiala: ')
factura_1.genereaza_factura()
print('--------------------- ')
factura_1.schimba_pretul(700)
factura_1.schimba_cantitatea(30)
factura_1.schimba_nume_produs('Laptop')
print('Factura 1 finala: ')
factura_1.genereaza_factura()

print(' ')

factura_2 = Factura(13, 'Perdea', 5, 200)
print('Factura nr. 2 initiala: ')
factura_2.genereaza_factura()
print('--------------------- ')
factura_2.schimba_pretul(340)
factura_2.schimba_cantitatea(7)
factura_2.schimba_nume_produs('Papusa')
print('Factura 2 finala: ')
factura_2.genereaza_factura()

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 2. - OPTIONAL
  Clasa Masina
  Atribute: marca, model, viteza maxima, viteza_actuala, culoare,
culori_disponibile (set), inmatriculata (bool)
    Culoare = gri - toate mașinile cand ies din fabrica sunt gri
    Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica
    Culori disponibile = alegeți voi 5-7 culori
    Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele
    Inmatriculata = False
  Constructor: model, viteza_maxima
  Metode:
    ● descrie() - se vor printa toate atributele, în afară de culori_disponibile
    ● înmatriculare() - va schimba atributul înmatriculată în True
    ● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua
      culoare e în opțiunea de culori disponibile, altfel afișați o eroare
    ● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e
      negativă-eroare, daca viteza e mai mare decat viteza_max - masina va
      accelera până la viteza maximă
    ● franeaza() - mașina se va opri și va avea viteza 0
'''
print('\nExercitiul 2 - Optional:')


class Masina:
    marca = 'Renault'
    model = None
    viteza_maxima = None
    viteza_actuala = 0
    culoare = 'gri'
    culori_disponibile = {'alb', 'negru', 'gri', 'rosu', 'albastru'}
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descrie(self):
        print(f'Masina {self.marca} {self.model} are culoarea {self.culoare}.'
              f'\nViteza actuala este {self.viteza_actuala} km/h, dar poate atinge viteza maxima de {self.viteza_maxima} km/h.'
              f'\nAceasta masina este inmatriculata({self.inmatriculata}).')

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        while culoare not in self.culori_disponibile:
            print('Eroare! Culoarea nu este disponibila.')
            culoare = input('Introduceti alta culoare:')
            break
        else:
            self.culoare = culoare

    def accelereaza(self, viteza):
        if viteza < 0:
            print('Eroare! Ati introdus o viteza negativa!')
            viteza = int(input('Introduceti alta viteza: '))
        elif viteza + self.viteza_actuala > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
        else:
            self.viteza_actuala += viteza

    def franeaza(self):
        print(f'Masina s-a oprit.')
        self.viteza_actuala = 0


masina_1 = Masina('Kadjar', 200)
masina_1.descrie()
print(' ')
masina_1.inmatriculare()
masina_1.vopseste('roz')
masina_1.accelereaza(50)
masina_1.descrie()
masina_1.franeaza()
masina_1.descrie()
print(' ')

masina_2 = Masina('Clio', 180)
masina_2.descrie()
print(' ')
masina_2.inmatriculare()
masina_2.vopseste('rosu')
masina_2.accelereaza(40)
masina_2.descrie()
masina_2.franeaza()
masina_2.descrie()

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------

'''
Exercitiul 3. - OPTIONAL
  Clasa TodoList
  Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
  La început nu avem taskuri, dict e gol și nu avem nevoie de constructor
  Metode:
    ● adauga_task(nume, descriere) - se va adauga in dict
    ● finalizează_task(nume) - se va sterge din dict
    ● afișează_todo_list() - doar cheile
    ● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului,
      printăm detalii suplimentare.
        ○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
          adauge.
        ○ Dacă acesta răspunde nu - la revedere
        ○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în
          dict
'''
print('\nExercitiul 3 - Optional:')


class TodoList:
    todo = {}

    def adauga_task(self,nume, descriere):
        self.todo[nume] = descriere

    def finalizeaza_task(self, nume):
        del self.todo[nume]

    def afiseaza_todo_list(self):
        print('Lista task-urilor: ', end=' ')
        for task in self.todo.keys():
            print(f'{task}', end=' ')

    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task not in self.todo.keys():
            rasp = input('\nTask-ul nu e in dict. Doresti sa-l adaugi?(da/nu): ')
            if rasp == 'da':
                detalii = input('Introduceti detaliile task-ului: ')
                self.adauga_task(nume_task, detalii)
            else:
                print('La revedere:))')
        else:
            print(f'\nDetalii suplimentare: {self.todo[nume_task]}')


task_1 = TodoList()
task_1.adauga_task('Gatit_M', 'Mic Dejun')
task_1.adauga_task('Gatit_P', 'Pranz')
task_1.adauga_task('Gatit_C', 'Cina')
print(f'Afisarea task-urilor initiale: {task_1.todo} ')
task_1.finalizeaza_task('Gatit_M')
print('Afisarea listei dupa stergerea unui task...')
task_1.afiseaza_todo_list()
task_1.afiseaza_detalii_suplimentare('Gatit_P')
print(f'Afisarea task-urilor finale: {task_1.todo} ')

print(' ')

task_2 = TodoList()
task_2.adauga_task('Bucatarie', 'Mobila alba')
task_2.adauga_task('Sufragerie', 'Mobila wenge')
task_2.adauga_task('Dormitor', 'Mobila crem')
print(f'Afisarea task-urilor initiale: {task_2.todo} ')
task_2.finalizeaza_task('Dormitor')
print('Afisarea listei dupa stergerea unui task...')
task_2.afiseaza_todo_list()
task_2.afiseaza_detalii_suplimentare('Camera de zi')
print(f'Afisarea task-urilor finale: {task_2.todo} ')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------
