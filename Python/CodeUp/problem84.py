h, b, c, s = map(int, input().split())

# h*b*c*s/8/1024/1024
car = (h*b*c*s)/8/1024/1024
print("{:.1f} MB" .format(car))

