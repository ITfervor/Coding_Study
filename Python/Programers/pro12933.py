arr = list(str(int(input()))) # 숫자 리스트화해서 리스트에 다 넣는것
# sum(map(int, str(x))) 합구하는것
arr.sort(reverse=True)
print(''.join(arr))
