"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так,
чтобы они не били друг друга (ферзь может ходить по горизонтали, вертикали и диагонали).
Вам дана расстановка двух ферзей на доске, определите могут ли ферзи бить друг друга.
Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали,
второе - координата по вертикали. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

Используя условие первой задачи из урока, проверить то же самое только для коней.
"""
first = [0, 0]
second = [1, 4]
if __name__ == "__main__":
    if second[0] == first[0] + 1 and second[1] == first[1] - 2:
        print("Yes")
    elif second[0] == first[0] + 2 and second[1] == first[1] - 1:
        print("Yes")
    elif second[0] == first[0] + 2 and second[1] == first[1] + 1:
        print("Yes")
    elif second[0] == first[0] + 1 and second[1] == first[1] + 2:
        print("Yes")
    elif second[0] == first[0] - 1 and second[1] == first[1] + 2:
        print("Yes")
    elif second[0] == first[0] - 2 and second[1] == first[1] + 1:
        print("Yes")
    elif second[0] == first[0] - 2 and second[1] == first[1] - 1:
        print("Yes")
    elif second[0] == first[0] - 1 and second[1] == first[1] - 2:
        print("Yes")
    else:
        print("No")


