a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
c = int(input("nhập số c: "))

print("số lớn nhất là: ", max(a,b,c))
print("số nhỏ nhất là: ", min(a,b,c))

import math

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có 2 nghiệm:", x1, "và", x2)
elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:", x)
else:
    print("Phương trình vô nghiệm")