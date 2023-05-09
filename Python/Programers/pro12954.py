# x만큼 간격이 있는 n개의 숫자

# def solution(x, n):
#     if x != 0:
#         x = int(x)
#         n = int(n)
#         answer = []
#         for i in range(n):
#             answer.append(x)      
#         return answer
#     else:
#         return [0]

x, n = input().split()
a = int(x)
n = int(n)
answer = []
for i in range(n):
    answer.append(x)
    x += a

print(answer)
