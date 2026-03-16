class inhvien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        return self.diem == other.diem




sv1 = (8)
sv2 = (9)
sv3 = (9)

print(sv1 == sv2)
print(sv2 == sv3)

