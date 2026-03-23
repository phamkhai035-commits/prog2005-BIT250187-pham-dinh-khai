def insertion_sort_strings(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and len(arr[j]) < len(key):  # giảm dần theo độ dài
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        print(f"Bước {i}: {arr}")

arr = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    arr.append(s)

print("Ban đầu:", arr)
insertion_sort_strings(arr)
print("Sau khi sắp xếp:", arr)