def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    teeny = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    # Pokud je číslo mimo rozsah
    if cislo < 0 or cislo > 100:
        return "Číslo je mimo rozsah 0-100"
    
    # Zpracuj 100
    if cislo == 100:
        return "sto"
    
    vysledek = ""
    
    # Zpracuj desítky a jednotky
    if cislo >= 20:
        desitky_cast = desitky[cislo // 10]
        jednotky_cast = jednotky[cislo % 10]
        vysledek = desitky_cast
        if cislo % 10 != 0:
            vysledek += " " + jednotky_cast
    elif 10 <= cislo < 20:
        vysledek = teeny[cislo - 10]
    else:
        vysledek = jednotky[cislo]
    
    return vysledek

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)