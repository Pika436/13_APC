# 17.	Take marks of 20 students, calculate the class average and display the marks of students who scored above the average.

import numpy as np

marks = np.array([75, 80, 65, 90, 85, 70, 95, 60, 88, 82,
                  78, 92, 55, 68, 84, 73, 89, 96, 62, 77])

average = np.mean(marks)

above_average = marks[marks > average]

print("Marks of students:", marks)
print("Class Average:", average)
print("Marks above average:", above_average)