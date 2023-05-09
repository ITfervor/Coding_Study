def solution(n):
    list1 = []
    a = 0
    b = 1
    cat = 0
    sum = 0
    while n//3 != 0:
        a = n % 3
        list1.append(a)
        n //= 3
    a = n % 3
    list1.append(a)
    for i in range(len(list1)):
        cat = list1[len(list1)-1 - i] * b
        sum += cat
        b *= 3
    return sum

num = int(45)
print(solution(num))