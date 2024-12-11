def dec_to_bin(cislo):
    # Funkce převede číslo na binární reprezentaci (číslo může být str i int)
    # Pokud je vstup typu str, převedeme jej na int
    if isinstance(cislo, str):
        cislo = int(cislo)
    # Vrátíme binární reprezentaci čísla (bez prefixu '0b')
    return bin(cislo)[2:]

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"


