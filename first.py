""""
def hello():
    print("Hello World!")
"""
def sudy_lichy(cislo):
    if (cislo%2 == 0):
        print("Číslo je sudé")
    elif (cislo%2 != 0):
        print("Číslo je liché")
    else:
        print("Nezadal jsi číslo")

cislo = input("Zadej číslo:")
sudy_lichy(cislo)