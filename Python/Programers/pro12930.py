# 이상한 문자만들기
def solution(s):
    answer = []
    list1 = s.split(' ')
    for str in list1:
        str1 = ''
        for w, tmp in enumerate(str): #enumerate는 for문을 사용하는 것이며 , 앞은 상승하는 수를 뒤는 상승하는 요소를 뜻함
            if w % 2 == 0:
                str1 += tmp.upper()
            else :
                str1 += tmp.lower()
        answer.append(str1)
    return ' '.join(answer)



# def solution(s):
#     answer = []
#     list1 = s.split()
#     for str in list1:
#         str1 = ''
#         for j in range(0, len(str)):
#             if j % 2 == 0:
#                 str1 += str[j].upper()
#             else :
#                 str1 += str[j].lower()
#         answer.append(str1)

#     return ' '.join(answer)

asd = "try hello world"
print(solution(asd))