#예산 구하기
def solution(d, budget):
    sum = 0
    i = 0
    while sum <= budget:       
        sum += min(d)
        if sum >= budget:
            if sum == budget:
                i += 1
            break
        d.remove(min(d))
        i += 1
    return i 
# 런타임 에러


def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

mon = [2,2,3,3]	
num = 9

print(solution(mon, num))