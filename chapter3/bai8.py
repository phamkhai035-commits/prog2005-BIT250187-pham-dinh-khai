arr = list(map(int, input("Nhập danh sách: ").split()))

for n in arr:
    if n > 10:
        print("Số đầu tiên >10:", n)
        break
else:
    print("Không có số >10")