n = int(input("Nhập số người: "))
data = {}

for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    data[name] = age

avg = sum(data.values()) / len(data)
print("Tuổi trung bình:", avg)

items = list(data.items())

for i in range(len(items)):
    max_idx = i
    for j in range(i + 1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]

print("Sắp xếp giảm dần theo tuổi:")
for name, age in items:
    print(name, age)