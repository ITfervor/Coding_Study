#나머지가 1이 되는 수 찾기

# n = int(input())

# i = 1
# while i < n:
#     if n % i == 1:
#         print(i)
#         break
#     i += 1

def solution(n):
    n = int(n)
    i = 1
    while i < n:
        if n % i == 1:
            return i
        i += 1
    