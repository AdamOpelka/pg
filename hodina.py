""""
def my_range(min, max, step=1):
    
    vysledek = []
    hodnota = min
    while (hodnota) < max:
        vysledek.append(hodnota)
        hodnota = hodnota + step 
        

    return vysledek
"""
seznam = ["jablko", "banan", "tresen", "strasnedlouhyslovo"]

def my_enumarate(x):
    vysledek = []
    pismeno = [x for x in seznam[x]]
    y = len(seznam[x])
    z = 0
    k = 0
    
    
    while k < y:     
        funkce = (f"Index {k}: {pismeno[k]}")
        vysledek.append(funkce)
        k += 1
    
    return vysledek

if __name__ == "__main__":
    #min = int(input("Zadej min: "))
    #max = int(input("Zadej max: "))
    #step = int(input("Zadej step: ")) 
    x = int(input("Zadej cislo slova: "))
    #text = my_range(min, max, step)
    text = my_enumarate(x)
    #print(text)
    for hodnota in text:
        print(hodnota)