# Příklad 3: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.

import requests

def convert_to_czk(amount, currency):
    # URL kurzovního lístku
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

    # Stažení kurzovního lístku
    response = requests.get(url)
    if not response.ok:
        raise ConnectionError("Chyba při stahování kurzovního lístku.")

    # Načtení dat a zpracování řádků
    lines = response.text.splitlines()

    # Procházení dat pro hledání kurzu měny
    for line in lines[2:]:  # Přeskakujeme hlavičku
        parts = line.split("|")
        if len(parts) < 5:
            continue  # Přeskočíme nevalidní řádky

        country, currency_name, amount_in_currency, code, exchange_rate = parts

        if code == currency:
            # Výpočet výsledné částky
            rate = float(exchange_rate.replace(",", "."))
            amount_in_currency = int(amount_in_currency)
            return round(amount * rate / amount_in_currency, 2)

    # Pokud měna nebyla nalezena, vyhoďte výjimku
    raise ValueError(f"Měna {currency} nebyla nalezena v kurzovním lístku.")

print(convert_to_czk(100, "USD"))
print(convert_to_czk(50, "EUR"))
#print(convert_to_czk(100, "ZEN"))
