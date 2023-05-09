def solution(numbers):
    sum = 0
    
    for i in range(10): 
        if i not in numbers:
            sum += i
            print(i)
    return sum

s = [1,2,3,4,6,7,8,0]

print(solution(s))


# if 'k' not in 'python':
#     print(True)
# else:
#     print(False)
# -------------------------
# True