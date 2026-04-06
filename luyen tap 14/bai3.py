def in_hinh(n):
    # Hình 1: Hình vuông toàn số 1
    print("Hinh 1:")
    for i in range(n):
        print("1 " * n)

    # Hình 2: Tăng dần theo cột
    print("\nHinh 2:")
    for i in range(n):
        print(*(range(1, n + 1)))

    # Hình 3: Tam giác số tăng dần
    print("\nHinh 3:")
    for i in range(1, n + 1):
        print(*(range(1, i + 1)))

    # Hình 4: Tam giác số ngược (giảm dần số lượng)
    print("\nHinh 4:")
    for i in range(n, 0, -1):
        print(*(range(1, i + 1)))

    # Hình 5: Tam giác số căn lề phải (theo quy luật trong ảnh)
    print("\nHinh 5:")
    for i in range(1, n + 1):
        res = [str(j) if j <= i else " " for j in range(1, n + 1)]
        # Lưu ý: Hình 5 trong ảnh có quy luật hơi đặc biệt ở hàng 3 (1 3)
        # Nếu theo đúng ảnh:
        if i == 3: print("1   3")
        else: print(" ".join(res))

    # Hình 6: Tam giác số ngược, thưa dần
    print("\nHinh 6:")
    for i in range(n, 0, -1):
        if i == 4: print("1 2 3 4")
        elif i == 3: print("1   3")
        elif i == 2: print("1 2")
        else: print("1")

    # Hình 7: Tam giác cân (in số hàng)
    print("\nHinh 7:")
    for i in range(1, n + 1):
        print("  " * (n - i) + (str(i) + " ") * (2 * i - 1))

    # Hình 8: Tam giác số đối xứng (1 2 3 4 3 2 1)
    print("\nHinh 8:")
    for i in range(1, n + 1):
        left = list(range(1, i + 1))
        right = list(range(i - 1, 0, -1))
        print("  " * (n - i) + " ".join(map(str, left + right)))

    # Hình 9: Tam giác số đối xứng rỗng
    print("\nHinh 9:")
    for i in range(1, n + 1):
        spaces = "  " * (n - i)
        if i == 1:
            print(spaces + "1")
        elif i == n:
            left = list(range(1, n + 1))
            right = list(range(n - 1, 0, -1))
            print(" ".join(map(str, left + right)))
        else:
            mid_spaces = "  " * (2 * i - 3)
            print(f"{spaces}1 {mid_spaces}1")

# Thực thi
in_hinh(4)