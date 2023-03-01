h, w = map(int, input().split())

s = []
for i in range(h):
    s.append([])
    for j in range(w):
        s.append(0)

n = int(input())

l = [list(map()) for i in range(5)]
for i in range(n):
    l = list(map(int, input().split())) # d가 0이면 가로모양 1 이면 세로 모양, L은 길이
    for _ in range(l) :
        if d == 0 : 
            s[x - 1][y - 1] = 1
            y += 1
        elif d == 1 : 
            s[x - 1][y - 1] = 1
            x += 1
for i in range(h):
    for j in range(w):
        print(s[i][h], end=" ")    
    print()


# h,w = input().split()
# h = int(h)
# w = int(w)

# m = []
# for i in range(h+1) :
#   m.append([])
#   for j in range(w+1) :
#     m[i].append(0)

# n = int(input())
# for i in range(n) :
#   l,d,x,y = input().split()
#   if int(d)==0 :
#     for j in range(int(l)) :
#       m[int(x)][int(y)+j] = 1
#   else :
#     for j in range(int(l)) :
#       m[int(x)+j][int(y)] = 1

# for i in range(1, h+1) :
#   for j in range(1, w+1) :
#     print(m[i][j], end=' ')
#   print()