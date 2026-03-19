ds = []
for i in range(5):
    ds.append(input(f"Nhập chuỗi {i+1}: "))

n = len(ds)

for i in range(n):
    for j in range(n - i - 1):
        if len(ds[j]) < len(ds[j + 1]):
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
        print("Bước:", ds)