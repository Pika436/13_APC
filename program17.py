with open("student.txt", "r") as file:
    lines = file.readlines()

print("All Records:")

for line in lines:
    print(line, end="")

highest_marks = 0
highest_student = ""
total_marks = 0
count = 0

print("\nStudents who scored more than 80:")

for line in lines[1:]:
    data = line.strip().split(",")

    if len(data) == 3:
        roll_no = data[0]
        name = data[1]
        marks = int(data[2])

        total_marks = total_marks + marks
        count = count + 1

        if marks > highest_marks:
            highest_marks = marks
            highest_student = name

        if marks > 80:
            print(name)

if count > 0:
    average = total_marks / count

    print("\nHighest Marks:", highest_marks)
    print("Student with highest marks:", highest_student)
    print("Average Marks:", average)
else:
    print("\nNo student records found.")