def solution(num):
    i = 0
    while num != 1:
        if i > 500 :
            return -1
        
        if num % 2 == 0:
            num //= 2
        
        elif num % 2 == 1:
            num = num * 3 + 1
        i += 1

    return i
    


# 입력된 수가 짝수이면 if문으로 while를 통해 계속 2로 나누기 
# 주어진 수가 1인경우 0을 리턴
# 작업을 500번 해도 1이 안되면 -1을 리턴