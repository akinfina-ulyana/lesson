dict = {
    "apple": "яблоко",
    "car": "Машина"
}

def eng_rus(word):
    return dict.get(word, "ERROR")


print(eng_rus("apple"))
print(eng_rus("Машина"))
