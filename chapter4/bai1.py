def thong_ke(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat

t = (3, 7, 1, 9, 5)

tong, max_val, min_val = thong_ke(t)
print("Tổng:", tong)
print("Lớn nhất:", max_val)
print("Nhỏ nhất:", min_val)
