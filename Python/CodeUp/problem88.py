a, d, n = map(int, input().split())

list = []
i = 0
while True:
    list.append(a)
    i += 1
    a += d
    if i >= n:
        a -= d
        break
print(a)

