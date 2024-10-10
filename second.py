def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    prepis = str(cislo)
    return prepis

if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)