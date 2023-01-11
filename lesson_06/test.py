import random

def card_random():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "k", "D"]
   # test_list_2 = ["Hearts", "Diamonds", "Clubs", "Spades"]

    #return print(random.choice(test_list) + "-" + random.choice(test_list_2))
    return print(random.choice(test_list))


summa = 0
while True:
    input("Достать карту: Y/N")
    if "N":
        break
    elif "Y":






"""card = card_random()
   if card == range(1, 11):
        summa += card
    elif card == "J" or "D" or "K":
        summa += 10
    else:
        if summa >= 21:
            summa += 1
        else:
            summa += 11
            print(summa)"""