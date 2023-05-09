# 별찍기 문제

# a, b = map(int, input().strip().split(' '))
a, b = map(int, input().split())
str = "*"
for i in range(1,a):
    str += "*"
for i in range(b):
    print(str)
    i += 1
