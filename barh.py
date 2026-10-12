# horizontal barchart

import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

plt.barh(students, marks)

plt.title("Student Marks - Horizontal Bar Graph")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()

