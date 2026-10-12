# line graph

import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

plt.plot(students, marks, marker="o")

plt.title("Student Marks - Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.grid(True)
plt.show()
