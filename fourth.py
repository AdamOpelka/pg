def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka["typ"]
    pozice = figurka["pozice"]

    # Kontrola, zda je cílová pozice na šachovnici
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # Kontrola, zda cílová pozice není obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # Pravidla pohybu jednotlivých figur
    if typ == "pěšec":
        smer = 1  # Směr pohybu pěšce (vpřed)
        if cilova_pozice == (pozice[0] + smer, pozice[1]):  # pohyb o 1
            return True
        elif pozice[0] == 1 and cilova_pozice == (pozice[0] + 2 * smer, pozice[1]):  # pohyb o 2 z výchozí pozice
            if (pozice[0] + smer, pozice[1]) not in obsazene_pozice:  # ověření, zda je mezilehlá pozice volná
                return True
        return False

    elif typ == "jezdec":
        row_diff = abs(cilova_pozice[0] - pozice[0])
        col_diff = abs(cilova_pozice[1] - pozice[1])
        # Jezdec se pohybuje ve tvaru "L"
        if (row_diff, col_diff) in [(2, 1), (1, 2)]:
            return True
        return False

    elif typ == "věž":
        if pozice[0] == cilova_pozice[0]:  # Stejné řádky
            # Kontrola, zda v cestě nestojí jiná figura
            for row in range(min(pozice[0], cilova_pozice[0]) + 1, max(pozice[0], cilova_pozice[0])):
                if (row, pozice[1]) in obsazene_pozice:
                    return False
            return True
        elif pozice[1] == cilova_pozice[1]:  # Stejné sloupce
            # Kontrola, zda v cestě nestojí jiná figura
            for col in range(min(pozice[1], cilova_pozice[1]) + 1, max(pozice[1], cilova_pozice[1])):
                if (pozice[0], col) in obsazene_pozice:
                    return False
            return True

    elif typ == "střelec":
        row_diff = abs(cilova_pozice[0] - pozice[0])
        col_diff = abs(cilova_pozice[1] - pozice[1])
        if row_diff == col_diff:  # Diagonální pohyb
            # Kontrola, zda v cestě nestojí jiná figura
            step_row = 1 if cilova_pozice[0] > pozice[0] else -1
            step_col = 1 if cilova_pozice[1] > pozice[1] else -1
            for i in range(1, row_diff):
                if (pozice[0] + i * step_row, pozice[1] + i * step_col) in obsazene_pozice:
                    return False
            return True

    elif typ == "dáma":
        row_diff = abs(cilova_pozice[0] - pozice[0])
        col_diff = abs(cilova_pozice[1] - pozice[1])
        if (pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1] or row_diff == col_diff):  # Horizontálně, vertikálně nebo diagonálně
            # Zde je třeba ověřit, zda není něco v cestě
            if pozice[0] == cilova_pozice[0]:  # Horizontální pohyb
                for col in range(min(pozice[1], cilova_pozice[1]) + 1, max(pozice[1], cilova_pozice[1])):
                    if (pozice[0], col) in obsazene_pozice:
                        return False
                return True
            elif pozice[1] == cilova_pozice[1]:  # Vertikální pohyb
                for row in range(min(pozice[0], cilova_pozice[0]) + 1, max(pozice[0], cilova_pozice[0])):
                    if (row, pozice[1]) in obsazene_pozice:
                        return False
                return True
            else:  # Diagonální pohyb
                step_row = 1 if cilova_pozice[0] > pozice[0] else -1
                step_col = 1 if cilova_pozice[1] > pozice[1] else -1
                for i in range(1, abs(cilova_pozice[0] - pozice[0])):
                    if (pozice[0] + i * step_row, pozice[1] + i * step_col) in obsazene_pozice:
                        return False
                return True

    elif typ == "král":
        row_diff = abs(cilova_pozice[0] - pozice[0])
        col_diff = abs(cilova_pozice[1] - pozice[1])
        if max(row_diff, col_diff) == 1:  # Král se pohybuje o jedno pole
            return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    # Testy
    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True


