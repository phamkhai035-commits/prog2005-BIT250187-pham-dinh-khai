arr = list(map(int, input("Nhập số: ").split()))
count = 0

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            count += 1

print("Danh sách sau sắp xếp:", arr)
print("Số lần hoán đổi:", count)