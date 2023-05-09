# 배열 뒤집어서 출력
n = input()

answer = []
list =[]
for i in str(n):
    list.append(i)
for i in range(int(len(list)), 0 ,-1):
    answer.append(i)

print(answer)