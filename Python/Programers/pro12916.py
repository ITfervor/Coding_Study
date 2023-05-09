# 문자열 갯수 세는것
def solution(s):
    answer = True

    if s.count("P").lower() == s.count("Y").lower():
        return True
    elif s.count("p").lower() == 0 and s.count("y").lower == 0:
        return True
    else: 
        return False
    return s.lower().count('p') == s.lower().count('y')

solution()



