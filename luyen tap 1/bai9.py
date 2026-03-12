class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")

sv1 = Student("khai", 10)
sv1.display()