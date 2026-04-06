class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Hoa: {self.name}, Màu sắc: {self.color}"

hoa_hong = Flower("Hoa Hồng", "Đỏ")
print(hoa_hong)