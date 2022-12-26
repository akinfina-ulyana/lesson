"""
Получить сумму кубов натуральных чисел от n до m используя цикл for,
числа n и m вводятся с клавиатуры.
"""

n = int(input("Введите число n, (n < m): "))
m = int(input("Введите число m, (m > n): "))
accumulation = 0
current = n ** 3
for i in range(n, m):
    accumulation += i ** 3
print(accumulation)
