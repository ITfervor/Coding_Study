def solution(strings, n):
    
    return sorted(strings, key=lambda x: x[n])
    

#리스트화해서 n번째 순으로 정렬...?    
# s = ['2 A', '1 B', '4 C', '1 A']
# s.sorted(s, key=lambda x: (x.split()[1], x.split()[0]))




s = ["sun", "bed", "car"]
num = 1

print(solution(s, num))