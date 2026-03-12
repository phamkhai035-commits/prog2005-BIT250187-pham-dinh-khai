import random

m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))

matrix = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(1,100))
    matrix.append(row)

print("Ma trận:")
for row in matrix:
    print(row)

h = int(input("Nhập hàng cần xem: "))
print("Hàng", h, ":", matrix[h-1])

c = int(input("Nhập cột cần xem: "))
for i in range(m):
    print(matrix[i][c-1])

max_value = max(max(row) for row in matrix)
print("Giá trị lớn nhất:", max_value)