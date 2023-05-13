def solution(nums):
    set1 = set(nums)
    types = len(set1)   #폰켓몬 종류 개수
    N = len(nums)   #폰켓몬 수
    
    if types < N//2:
        return types
    else:
        return N//2

print(solution([3,1,2,3]))