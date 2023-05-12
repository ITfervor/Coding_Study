# def solution(a, b, n):
#     answer = 0
#     m = 0 
#     while n >= a:
#         n = n//a
#         answer = answer + (n * b)
#         print("n의 값")
#         print(n)

#         if (n % a != 0):
#             if((n + ( n % a)) % a == 0 ):
#                 m = (n + (n % a)) // a 
#                 if (m < a):
#                     break
#                 answer = answer + m
#                 n = m
#             else:
#                 n = n + (n % a) 
#         else:
#             continue
#         print("answer의 값")
#         print(answer)
#     return answer





def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer


print(solution(2,1,20))