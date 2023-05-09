#카카오 비밀지도
def solution(n, arr1, arr2):
    answer = []
    answer1 = []
    answer2 = []
        #십진수 이진수로 변경
    for value in arr1:
        value = format(value, 'b').zfill(n)
        answer1.append(value)
    
    for value in arr2:
        value = format(value, 'b').zfill(n)
        answer2.append(value)

    for i in range(n) :
        value = ""
        for j in range(n) :
            if answer1[i][j] == '0' and answer2[i][j] == '0' :
                value += " "
            else :
                value += "#"
        answer.append(value)
    return answer



# 다른 사람 풀이
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer



n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))