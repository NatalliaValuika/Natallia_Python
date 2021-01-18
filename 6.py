import random
n = int(input("ВВедите размер списка:\n"))
A =[]
for i in range(n):
    a = random.random(1,9)
    A.append(a)
s = sum(A)
l = len(A)
a = s/l
print("Элементы списка")
for i in range(n):
    print(A[i])