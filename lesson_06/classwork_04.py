"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается,
достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

import random

def card_random():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "D", "K", "A"]
   # test_list_2 = ["Hearts", "Diamonds", "Clubs", "Spades"]

    #return print(random.choice(test_list) + "-" + random.choice(test_list_2))
    return print(random.choice(test_list))


summa = 0
while summa < 21:
    card = card_random()
    print(card)
    if card == range(1, 11):
        summa += card
    elif card == "J" or "D" or "K":
        summa += 10
    else:
        if summa >= 21:
            summa += 1
        else:
            summa += 11
            print(summa)
if summa >= 21:
    print(summa)
    print("Игра закончена")
