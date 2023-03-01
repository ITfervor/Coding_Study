a, r, n = map(int, input().split())

list = []
i = 0
while True:
    if r == 0:
        print(0)
        break
    else:
        list.append(a)
        i += 1
        a *= r
        if i >= n:
            a //= r
            print(a)
            break
    

