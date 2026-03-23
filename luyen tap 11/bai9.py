def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = input(f"Nhập hàng {i+1}: ").split()
        if len(row) != cols:
            raise ValueError("Nhập thiếu hoặc thừa phần tử!")
        matrix.append(list(map(int, row)))
    return matrix

# Nhập kích thước
r = int(input("Số hàng: "))
c = int(input("Số cột: "))

try:
    print("Ma trận A:")
    A = input_matrix(r, c)

    print("Ma trận B:")
    B = input_matrix(r, c)

    # Cộng ma trận
    C = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    print("Ma trận tổng:")
    for row in C:
        print(row)

except:
    print("Lỗi: dữ liệu nhập không hợp lệ!")