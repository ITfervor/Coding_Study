#핸드폰 가리기
def solution(phone_number):

    return "*"*(len(phone_number)-4)+phone_number[-4:] #파이썬은 문자열 곱셈이 가능하다.

print(solution("01033334444"))

