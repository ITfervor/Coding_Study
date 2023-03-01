ant = []
for i in range(10):
    ant.append([])
    for j in range(10):
        ant[i].append(0)
for i in range(10):
    ant[i]=list(map(int, input().split()))

a = 1
b = 1
while True:
    if ant[a][b] == 0:
        ant[a][b] = 9
    elif ant[a][b] == 2:
        ant[a][b] = 9
        break

    if(ant[a][b+1] == 1 and ant[a+1][b] ==1) or (a == 9 and b ==9):
        break

    if ant[a][b+1] != 1:
        b += 1 
    elif ant[a+1][b] != 1:
        a += 1
       


for i in range(10):
    for j in range(10):
        print(ant[i][j], end=" ")
    print()
        
