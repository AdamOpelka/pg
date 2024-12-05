def nejvetsi(seznam_cisel):
    maximum = max(seznam_cisel)
    return maximum


def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([2,3,1,5,4]) == 5