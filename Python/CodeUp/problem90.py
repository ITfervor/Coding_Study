a, m, d, n = map(int, input().split())

list = []
i = 0
while True:
    list.append(a)
    i += 1
    a *= m 
    a += d
    if i >= n:
        a -= d
        a //= m
        break
print(a)
