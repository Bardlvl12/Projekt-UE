# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sprawdz_czy_zawiera(lista, szukana_wartosc):
    wynik = szukana_wartosc in lista
    return wynik


moja_lista = [1, 3, 5, 7, 9]
wartosc_do_sprawdzenia = 5
wynik_sprawdzenia = sprawdz_czy_zawiera(moja_lista, wartosc_do_sprawdzenia)

print(wynik_sprawdzenia)






