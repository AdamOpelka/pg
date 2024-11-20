import sys
import requests
from bs4 import BeautifulSoup


def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne obsah zadané URL a vrátí seznam všech odkazů (href) na stránce.
    """
    try:
        # Validace a doplnění "https://" pro špatně zadané URL
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        # Stažení obsahu stránky
        response = requests.get(url)
        response.raise_for_status()  # Kontrola úspěšnosti HTTP požadavku

        # Parsování HTML obsahu
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extrakce všech odkazů
        hrefs = []
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            if not link.startswith('http'):  # Převod relativní URL na absolutní
                link = requests.compat.urljoin(url, link)
            hrefs.append(link)

        return hrefs

    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování URL: {e}")
        return []
    except Exception as e:
        print(f"Obecná chyba: {e}")
        return []


if __name__ == "__main__":
    try:
        # Načtení URL z příkazové řádky
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)

        # Vrácení seznamu nalezených odkazů
        print(odkazy)

    except IndexError:
        print("Chyba: Je třeba zadat URL jako argument programu.")
    except Exception as e:
        print(f"Program skončil chybou: {e}")

