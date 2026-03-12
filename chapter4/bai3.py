sinh_vien = {
    "Nam": 8,
    "Lan": 7,
    "Huy": 9
}

key = input("Nhập tên cần kiểm tra: ")

if key in sinh_vien:
    print("Key tồn tại")
else:
    print("Key không tồn tại")