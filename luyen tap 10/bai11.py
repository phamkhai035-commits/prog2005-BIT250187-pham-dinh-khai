while True:
    print("\n--- MENU ---")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        p = input("Nhập đường dẫn: ")
        print(lay_ten_file(p))
        print(lay_ten_khong_duoi(p))

    elif chon == "2":
        chuoi = input("Nhập chuỗi: ")
        ky_tu = input("Nhập ký tự: ")
        print(chuoi.count(ky_tu))

    elif chon == "3":
        break

    else:
        print("Chọn sai!")