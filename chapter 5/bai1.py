import matplotlib.pyplot as plt

labels = ['xuất sắc', 'giỏi', 'trung bình', 'yếu', 'kém']
values = [6, 10, 12, 4, 1]

plt.figure()
plt.bar(labels, values)

plt.title('kết quả học tập của lớp')
plt.xlabel('xếp loại')
plt.ylabel('số lượng học sinh')
plt.show()