# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `process_strings`, která přijme seznam řetězců. 
# Funkce vrátí nový seznam, který obsahuje pouze řetězce delší než 3 znaky, převedené na velká písmena.
# Pokud seznam obsahuje řetězec "STOP", ukončete zpracování seznamu a vraťte dosud vytvořený seznam.
#print("Zadejte řetězce oddělené čárkou (např. abc,abcd,STOP,efgh):")
#user_input = input()  # Uživatel zadá vstup jako řetězec
#strings = user_input.split(",")  # Rozdělíme vstup na seznam řetězců



def process_strings(strings):
    result = []
    for string in strings:
        if string == "STOP":
            break
        if len(string) > 3:
            result.append(string.upper())
    return result

#result = process_strings(strings)

#print("Výsledek:", result)


# Pytest testy pro Příklad 2
def test_process_strings():
    assert process_strings(["abc", "abcd", "STOP", "efgh"]) == ["ABCD"]
    assert process_strings(["hello", "world", "STOP", "python"]) == ["HELLO", "WORLD"]
    assert process_strings(["hi", "ok", "go"]) == []
    assert process_strings(["code", "test", "debug"]) == ["CODE", "TEST", "DEBUG"]