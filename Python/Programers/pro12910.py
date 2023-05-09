# def solution(arr, divisor):
#     answer = []
#     divisor = int(divisor)
#     for i in range(len(arr)):
#         if arr[i] % divisor == 0:
#             answer.append(arr[i])
#         elif len(answer) == 0:
#             return [-1]
#     answer.sort()
#     return answer

# if문을 통해서 나머지가 0인 경우 append
# append된 리스트 값을 출력
# answer 값이 없으면 -1을 리턴

def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]


