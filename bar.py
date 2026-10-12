
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

plt.bar(students, marks)

plt.title("Student Marks - Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
