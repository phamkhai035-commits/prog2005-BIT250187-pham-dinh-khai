nums = list(map(int, input("Nhập danh sách số (cách nhau bởi dấu cách): ").split()))

even_nums = [x for x in nums if x % 2 == 0]
total = sum(even_nums)

print("Số chẵn:", even_nums)
print("Tổng số chẵn:", total)