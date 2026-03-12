import math

s = input("Nhập chuỗi số: ")

numbers = [int(x.strip()) for x in s.split(";")]

for num in numbers:
    print(num)

even = sum(1 for x in numbers if x % 2 == 0)

negative = sum(1 for x in numbers if x < 0)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

prime = sum(1 for x in numbers if is_prime(x))

avg = sum(numbers) / len(numbers)

print("Số chẵn:", even)
print("Số âm:", negative)
print("Số nguyên tố:", prime)
print("Trung bình:", avg)
