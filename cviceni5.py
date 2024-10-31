import sys
import csv

def nacti_csv(soubor):
    data = []
    with open(soubor, "r") as fp:
        reader = csv.reader(fp)
        for row in reader:
            data.append(row)
    return data


def spoj_data(*data):
    vysledek = {}
    keys = []
    for d in data:
        for v in zip(*d):
            print(v)
    
    
    return vysledek


def zapis_csv(soubor, data):
    pass


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        zapis_csv(vysledna_data)
    except IndexError:
        print("Zadej 2 vtuspni soubory typu csv")