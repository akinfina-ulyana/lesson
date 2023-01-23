result = 0
current = 1
s = int(input())
q = s
m = int(input())
while current <= m:
    result += s
    s = s * 10 + q
    current += 1
    print(result)


