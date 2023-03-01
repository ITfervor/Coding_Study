def solution(arr):
    arr = []
    a = list(map(int, input().split()))
    arr.append(a)
    s = 0
    for i in range(arr.length + 1):
        s += arr[i]
    answer = s / arr.length
    return answer