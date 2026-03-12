import math

n = float(input("Nhập số: "))

if n < 0:
    print("Lỗi: Không thể tính căn bậc hai số âm")
else:
    print("Căn bậc hai:", math.sqrt(n))
