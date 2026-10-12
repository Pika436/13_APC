
import matplotlib.pyplot as plt

marks = [35, 45, 50, 55, 60, 65, 70, 75, 80, 90, 100]

plt.boxplot(marks)

plt.title("Student Marks - Box Plot")
plt.ylabel("Marks")

plt.show()
