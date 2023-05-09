from itertools import combinations
def solution(sizes):
    list1 = []
    for size in sizes:
        mnumber = size[0] * size[1]
        list1.append(mnumber)
    
    return max(list1)

a = [[60, 50], [30, 70], [60, 30], [80, 40]]
b = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
print(solution(b))


#콤비네이션해서 조건에 맞는 값을 출력한다.
#조건의 값은....가로 세로가 모두 포함되는 값

