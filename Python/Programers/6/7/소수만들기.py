import itertools, math

def solution(nums):
    answer = 0
    combi = itertools.combinations(nums, 3)
    combi = list(combi)
    for i in combi:
        result = sum(i)
        for i in range(2, result-1):
            if result % i == 0:
                break
        else:
            answer += 1
            
    return answer

print(solution([1,2,3,4]))


# import itertools
# import math

# def is_prime(num):
#     """
#     주어진 수가 소수인지 확인하는 함수
#     """
#     if num < 2:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             return False
#     return True

# def solution(nums):
#     answer = 0
#     combi = itertools.combinations(nums, 3)
#     combi = list(combi)
    
#     for i in combi:
#         result = sum(i)
#         print("result 값:", result)
        
#         if is_prime(result):
#             answer += 1

#     return answer

# print(solution([1, 2, 3, 4]))
