"""
Дан словарь, где в качестве ключей английские слова,
а значений - их перевод на русский язык. Написать две функции,
одна переводит слово с английского на русский, где слово - это входной параметр,
вторая функция - с русского на английский.
"""

diction = {
    "apple": "яблоко",
    "car": "Машина"
}

def eng_rus(word):
    return diction.get(word, "ERROR")


def rus_eng(word):
    new_diction = {
        value: key
        for key, value in diction.items()
    }
    return  new_diction.get(word, "ERROR")



def rus_eng_2(word):
    for eng, rus in diction.items():
        if rus == word:
            return eng


print(eng_rus("apple"))
print(eng_rus("Машина"))



