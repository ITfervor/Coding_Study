n = int(input())
list = []
for i in range(1, n+1):
    if n % i == 0:
        list.append(i)
s = 0
print(list)
for i in range(len(list)):
    s += list[i]
print(s)
