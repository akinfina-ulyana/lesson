# 7.1.4
#include <stdio.h>

for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")

# 7.1.5

n = int(input())
for i in range(n):
    print("*******************")

#7.1.7
a = input()
    for i in range(10):
        print(i, a)

# 7.1.8
n = int(input())
for i in range(n + 1):
    print("Квадрат числа", i, "равен", i ** 2)

#7.1.9
n = int(input())
for i in range(n):
    print("*" * (n-i))

# 7.1.10
"""
На вход программе подается три натуральных числа m, p, nm,p,n:

    m: стартовое количество организмов;
    p: среднесуточное увеличение в %;
    n: количество дней для размножения.

Напишите программу, которая предсказывает размер популяции организмов.
Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.
"""

m = int(input())
p = int(input())
n = int(input())
for i in range(n):
    print(m)
    m = ((m * p)/100) + m

#7.2.1
m = int(input())
n = int(input())
for i in range(m, n+1):
    print(i)

#7.2.2
"""
Даны два целых числа mm и nn. Напишите программу, которая выводит все числа от m до n включительно в порядке
возрастания, если m<n, или в порядке убывания в противном случае.
"""
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n-1, -1):
        print(i)