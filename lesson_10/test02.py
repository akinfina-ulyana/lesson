"""
Даны два целых числа mm и nn (m>nm>n). Напишите программу,
которая выводит все нечетные числа от mm до nn включительно в порядке убывания.

m = int(input())
n = int(input())
for i in range(m, n, -1):
    if i % 2 != 0:
        print(i)
"""
"""Даны два натуральных числа mm и nn ( m≤nm≤n). Напишите программу, которая выводит 
   все числа от mm до nn включительно удовлетворяющие хотя бы одному из условий:

    число кратно 17;
    число оканчивается на 9;
    число кратно 3 и 5 одновременно.
"""
m = int(input())
n = int(input())
for i in range(m, n):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)

# 7.3.5
a = int(input())
b = int(input())
count = 0
for i in range(a, b):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        count += 1
print(count)


