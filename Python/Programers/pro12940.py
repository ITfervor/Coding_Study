# 최대 공약수와 최대 공배수
def solution(n, m):
    list1 = []
    for i in range(min(n,m) ,0 ,-1):
        if n % i == 0 and m % i == 0:
            list1.append(i)
            list1.append(i*(n//i)*(m//i))
            break

    return list1

print(solution(2, 5))