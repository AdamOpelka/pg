import sys
import requests
from bs4 import BeautifulSoup

def stahni_url_a_vrat_nadpisy(url):
    nadpisy = []
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print(f'nastala chyba, nepodařilo se připojit na (url)')
        return []
    if response.status_code !=200:
        print(f'nastala chyba, http code: (response.status_code)') 
        return []

    response.content

    return nadpisy

if __name__ == "__main__":
    url = sys.argv[1]
    nadpisy = stahni_url_a_vrat_nadpisy(url)
    print(nadpisy)