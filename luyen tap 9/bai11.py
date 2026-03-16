class animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("animal sound")


class Dog(animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("alo vũ à vũ,ờ anh chào vũ nhá")


dog1 = Dog("độ")
print("tên;", dog1.name)
dog1.sound()
