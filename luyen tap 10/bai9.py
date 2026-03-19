class Nguoi:
    so_luong = 0

    def __init__(self, ten, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi không hợp lệ")
        self._ten = ten
        self._tuoi = tuoi
        Nguoi.so_luong += 1

    def get_tuoi(self):
        return self._tuoi

    def set_tuoi(self, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi phải >= 0")
        self._tuoi = tuoi

    def __str__(self):
        return f"Tên: {self._ten}, Tuổi: {self._tuoi}"

    def chao(self):
        return f"Xin chào, tôi là {self._ten}"

    @classmethod
    def dem_so_luong(cls):
        return cls.so_luong

    @staticmethod
    def thong_bao():
        return "Đây là static method"

    def __eq__(self, other):
        return self._tuoi == other._tuoi


class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, diem):
        super().__init__(ten, tuoi)
        if diem < 0 or diem > 10:
            raise ValueError("Điểm không hợp lệ")
        self._diem = diem

    def __str__(self):
        return super().__str__() + f", Điểm: {self._diem}"


# Test
sv1 = SinhVien("khai", 20, 8)
sv2 = SinhVien("khanh", 20, 9)

print(sv1)
print(sv1.chao())
print("Số lượng:", Nguoi.dem_so_luong())
print("So sánh:", sv1 == sv2)
