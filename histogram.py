
import matplotlib.pyplot as plt

marks = [35, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90]

plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
