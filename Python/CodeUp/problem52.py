
# a, b = input().split()

# print(bool(int(a)) and bool(int(b))) 


a, b = input().split()
if bool(int(a)) | bool(int(b)):
    print("True")
else:
    print("False")