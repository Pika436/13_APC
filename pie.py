
import matplotlib.pyplot as plt

subjects = ["Python", "Java", "C++", "DBMS"]
marks = [30, 25, 20, 25]

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Subject Marks Distribution")
plt.show()
