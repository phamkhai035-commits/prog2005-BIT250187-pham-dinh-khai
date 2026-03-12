def diem_trung_binh(ds):
    tong = sum(ds.values())
    return tong / len(ds)

sinh_vien = {
    "Nam": 8,
    "Lan": 7,
    "Huy": 9
}

print("Điểm trung bình:", diem_trung_binh(sinh_vien))