class sinhvien:
    dem = 0

    def __init__(self, ten):
        self.ten = ten
        sinhvien.dem += 1

    @classmethod
    def so_luong(cls):
        return cls.dem


sv1 = sinhvien("lu bo")
sv2 = sinhvien("trieu van")
sv3 = sinhvien("quan vu")

print("số sinh viên:", sinhvien.so_luong())