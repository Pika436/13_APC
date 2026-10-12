
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

# Create a figure
plt.figure(figsize=(10, 8))

# 1. Line graph
plt.subplot(2, 2, 1)
plt.plot(students, marks, marker="o")
plt.title("Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

# 2. Bar graph
plt.subplot(2, 2, 2)
plt.bar(students, marks)
plt.title("Bar Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

# 3. Scatter plot
plt.subplot(2, 2, 3)
plt.scatter(students, marks)
plt.title("Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Marks")

# 4. Pie chart
plt.subplot(2, 2, 4)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Pie Chart")

# Adjust spacing
plt.tight_layout()

# Display all graphs
plt.show()
