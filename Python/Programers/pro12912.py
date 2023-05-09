def solution(a, b):
    list = []
    sum = 0
    while True :
        list.append(a)
        a += 1
        if a == b:
            break
    for num in list:
        sum += num
    return sum

# a b 값 입력받기
# a 에서 b까지 하나씩 더하면서
# 모든 값 하나씩 값 리스트에 삽입
# 리스트 값 전체 더하기
