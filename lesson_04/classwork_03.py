"""
Ввести с клавиатуры целое число n.
Получить сумму кубов всех целых чисел от 1 до n (включая n) используя цикл while.
"""
n = int(input("Введите число: "))
result = 0
current = 1
while current <= n:
    result += current ** 3
    current += 1
print(result)

