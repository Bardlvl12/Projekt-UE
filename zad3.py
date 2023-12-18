# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def czy_parzysta(liczba):
    wynik = liczba % 2 == 0
return wynik

liczba_do_sprawdzenia = 10
wynik_sprawdzenia = czy_parzysta(liczba_do_sprawdzenia)

if wynik_sprawdzenia:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")



