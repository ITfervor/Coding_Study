number = 123

a =sum(map(int, str(number)))

s = []
for i in str(number):
    s.append(i)

print(s)
sum = 0
for i in range(len(s)):
    sum += int(s[i])

print(sum)
print(a)