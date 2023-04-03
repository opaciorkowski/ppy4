def szyfr_cezara(wiadomosc, klucz, alfabet="abcdefghijklmnopqrstuvwxyz"):
    wiadomosc = wiadomosc.lower()
    zaszyfrowana_wiadomosc = ""
    for znak in wiadomosc:
        if znak in alfabet:
            indeks = alfabet.index(znak)
            nowy_indeks = (indeks + klucz) % len(alfabet)
            zaszyfrowana_wiadomosc += alfabet[nowy_indeks]
        else:
            zaszyfrowana_wiadomosc += znak
    return zaszyfrowana_wiadomosc


print(szyfr_cezara("Test szyfru 00 Cezara zzzzz", 3))
