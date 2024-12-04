from cviceni8 import obsah_ctverce, obvod_ctverce, pocet_pismen



def test_obsah_ctverce():
    assert obsah_ctverce(4) == 16
    assert obsah_ctverce(5) ==25


def test_obvod_ctverce():
    assert obsah_ctverce(4) == 16
    assert obsah_ctverce(5) ==25

#def test_pocet_pismen():
   # assert pocet_pismen("ahoj, jak se mas?", "a") == 3
    #assert pocet_pismen("ahoj, jak se mas?", "a") == 2