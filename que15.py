# 15.	Create a nested tuple containing student details and display each record.
students=(
    ("ram",101,85),
    ("shyam",102,90),
    ("seeta",103,95)
)
for student in students:
    print("name :",student[0])
    print("roll no :",student[1])
    print("marks :",student[2])
    print()