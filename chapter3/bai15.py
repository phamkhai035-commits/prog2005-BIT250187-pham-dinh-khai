s = input("Nhập chuỗi: ")

# Cách 1: Slicing
print("Đảo bằng slicing:", s[::-1])

# Cách 2: Không slicing
rev = ""
for c in s:
    rev = c + rev

print("Đảo không slicing:", rev)