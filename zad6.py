# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def polacz_i_przetworz(list1, list2):
    # Połącz listy
    polaczona_lista = list1 + list2

    # Usuń duplikaty
    unikalna_lista = list(set(polaczona_lista))

    # Podnieś każdy element do potęgi 3
    przetworzona_lista = [element ** 3 for element in unikalna_lista]

    return przetworzona_lista

# Przykładowe użycie funkcji
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
wynik = polacz_i_przetworz(lista1, lista2)

# Wyświetlenie wyniku
print(wynik)







