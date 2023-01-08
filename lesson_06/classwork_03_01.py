"""
Написать функцию которая возвращают случайным образом одну
карту из стандартной колоды в 36 карт, где на первом месте номинал карты номинал
(6 - 10, J, D, K, A), а на втором название масти (Hearts, Diamonds, Clubs, Spades).
"""

import random

def card_random():
    test_list = ["6", "7", "8", "9", "10", "J", "D", "K", "A"]
    test_list_2 = ["Hearts", "Diamonds", "Clubs", "Spades"]

    return print(random.choice(test_list) + "-" + random.choice(test_list_2))

card_random()