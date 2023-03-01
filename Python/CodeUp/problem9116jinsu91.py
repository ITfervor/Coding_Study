# a = input()
# a = int(a, 16)

# for i in range(1, a+1):
#     print('{}'.format(a,16), '*{}'.format(i,16), '={}'.format((a*i), 16), sep='')


a = input()
a = int(a, 16)

for i in range(1, 16):
    print('%X'%a, '*%X'%i, '=%X'%(a*i), sep='')

