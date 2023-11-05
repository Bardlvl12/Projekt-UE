# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def wyswietl_co_drugi(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

liczby = list(range(1, 11))
wyswietl_co_drugi(liczby)
