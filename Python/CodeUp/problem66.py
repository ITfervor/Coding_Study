a, b, c =input().split()
a = int(a)
b = int(b)
c = int(c)

nums = []
nums.append(a)
nums.append(b)
nums.append(c)

for i in nums:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")