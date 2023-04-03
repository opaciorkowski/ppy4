def czy_liczba_pierwsza(*liczby):
    wynik = []
    for liczba in liczby:
        if liczba < 2:
            wynik.append(False)
        else:
            czy_pierwsza = True
            for i in range(2, int(liczba ** 0.5) + 1):
                if liczba % i == 0:
                    czy_pierwsza = False
                    break
            wynik.append(czy_pierwsza)
    return wynik


print(czy_liczba_pierwsza(2, 3, 4, 5, 6, 7, 8, 9, 10))
