import math


def ilosc_opakowan(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panelu, szerokosc_panelu, ilosc_paneli_w_opakowaniu):
    powierzchnia = (dlugosc_podlogi * szerokosc_podlogi) * 1.1
    powierzchnia_panelu = dlugosc_panelu * szerokosc_panelu
    ilosc_paneli = math.ceil(powierzchnia / powierzchnia_panelu)
    ilosc_opakowan = math.ceil(ilosc_paneli / ilosc_paneli_w_opakowaniu)
    return ilosc_opakowan


print(ilosc_opakowan(5, 4, 1, 0.5, 10))
