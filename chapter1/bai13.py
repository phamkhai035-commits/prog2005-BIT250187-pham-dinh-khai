try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    print("Kết quả:", a / b)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0")
except ValueError:
    print("Lỗi: Dữ liệu không hợp lệ")
