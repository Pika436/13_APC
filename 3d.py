
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D


hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 75, 90]
practice = [2, 3, 4, 5, 6]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Create 3D scatter graph
ax.scatter(hours, marks, practice)

# Add labels and title
ax.set_xlabel("Study Hours")
ax.set_ylabel("Marks")
ax.set_zlabel("Practice Tests")
ax.set_title("3D Student Performance Graph")

plt.show()

