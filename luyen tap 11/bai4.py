import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lst = [1, 3, 5, 7, 9]

x = int(input("Nhập số cần thêm: "))
lst.append(x)

k = int(input("Nhập k: "))
print("Số lần xuất hiện:", lst.count(k))

prime_sum = sum(i for i in lst if is_prime(i))
print("Tổng số nguyên tố:", prime_sum)

lst.sort()
print("Danh sách sau khi sắp xếp:", lst)

lst.clear()
print("Danh sách sau khi xóa:", lst)