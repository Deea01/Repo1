# TEMA 7  OOP - Cei 4 Piloni

# Exercitii OBLIGATORII

"""
Exercitiul 2.
  Rezolvă exercițiul după ce ai urcat proiectul (tot ce am facut până acum
împreună).
ABSTRACTION
    Clasa abstractă FormaGeometrica
    Conține un field PI=3.14
    Conține o metodă abstractă aria (opțional)
    Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
    probabil am colturi’

INHERITANCE
    Clasa Pătrat - moștenește FormaGeometrica
    constructor pentru latură

ENCAPSULATION
    latura este proprietate privată
    Implementează getter, setter, deleter pentru latură
    Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
    implementezi metoda abstractă aria)
Clasa Cerc - moștenește FormaGeometrica
    constructor pentru rază
    raza este proprietate privată
    Implementează getter, setter, deleter pentru rază
    Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)

POLYMORPHISM
    Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
    Creează un obiect de tip Patrat și joacă-te cu metodele lui
    Creează un obiect de tip Cerc și joacă-te cu metodele lui
"""
from abc import ABC, abstractmethod

print('\nExercitiul 2: ')


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    @classmethod
    def descrie(cls):
        print('Cel mai probabil am colturi')


#  ------------------------------------------


class Patrat(FormaGeometrica):
    __latura = 0

    def __init__(self, latura):
        self.__latura = latura

    def get_latura(self):
        return self.__latura

    def set_latura(self, latura):
        self.__latura = latura

    def del_latura(self):
        del self.__latura

    def aria(self):
        return float(self.__latura) ** 2


#  ------------------------------------------


class Cerc(FormaGeometrica):
    __raza = 0

    # Constructor
    def __init__(self, raza):
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, raza):
        self.__raza = raza

    def del_raza(self):
        del self.__raza

    def aria(self):
        return self.PI * float(self.__raza) ** 2

    def descrie(self):
        print('Eu nu am colturi.')


#  ------------------------------------------

patrat = Patrat(4)
print(f'Descrierea formei geometrice 1: ')
patrat.descrie()
print(f'Latura patratului initial: {patrat.get_latura()} cm.')
patrat.set_latura(5)
print(f' Latura patratului dupa modificare: {patrat.get_latura()} cm.')
print(f'Aria patratului: {patrat.aria()} cm^2.')
patrat.del_latura()
print(f' Latura patratului dupa stergere: {patrat.get_latura()} cm.')


print(' ')

cerc = Cerc(4)
print(f'Descrierea formei geometrice 2: ')
cerc.descrie()
print(f'Raza cercului initial: {cerc.get_raza()} cm.')
cerc.set_raza(6)
print(f'Raza cercului dupa modificare: {cerc.get_raza()} cm.')
print(f'Aria cercului: {cerc.aria()} cm^2.')
cerc.del_raza()
print(f' Raza cercului dupa stergere: {cerc.get_raza()} cm.')

print('--------------------------------------------- ')

# ------------------------------------------------------------------------------
