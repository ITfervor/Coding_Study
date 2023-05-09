# 카카오 채용연계형 /숫자 문자열과 영단어

def solution(s):
    dic1 = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for dc in dic1:
        if s.find(dc) > -1:
            s = s.replace(dc, dic1.get(dc))
    s = int(s)
    return s


s = "123"	
print(solution(s))