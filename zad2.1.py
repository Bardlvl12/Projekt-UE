# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def pomnoz_elementy_v1(lista):
    nowa_lista = []
    for element in lista:
        nowa_lista.append(element * 2)
    return nowa_lista

liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_elementy_v1(liczby)
print(wynik)
