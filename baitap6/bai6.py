import random
n = int(input())
print("nhap n",n)
def ngaunhien():
    return 40*random.random()
for i in range(n):
    print(ngaunhien())
