def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif len(arr[mid]) < len(target):
            right = mid - 1
        else:
            left = mid + 1

    return -1

target = input("Nhập chuỗi cần tìm: ")
pos = binary_search(arr, target)

if pos != -1:
    print(f"Tìm thấy tại vị trí {pos}")
else:
    print("Không tìm thấy")