for i in range(1, 4):
    print(f"\nSinh viên {i}")
    name = input("Tên: ")
    toan = float(input("Toán: "))
    ly = float(input("Lý: "))
    hoa = float(input("Hóa: "))

    avg = (toan + ly + hoa) / 3
    print(f"Điểm trung bình của {name}: {avg:.2f}")
