# 18. Store employee ID, name, department, and salary in a file. Write functions to:  • Display all employees.  • Find the highest-paid employee.  • Calculate average salary.  • Display employees earning above a given salary. 

with open("employee.txt", "w") as file:
    file.write("101,Amit,IT,50000\n")
    file.write("102,Priya,HR,60000\n")
    file.write("103,Rahul,Finance,45000\n")
    file.write("104,Neha,IT,75000\n")


def display():
    with open("employee.txt", "r") as file:
        print(file.read())


def highest():
    with open("employee.txt", "r") as file:
        high = 0
        name = ""

        for line in file:
            data = line.strip().split(",")

            salary = int(data[3])

            if salary > high:
                high = salary
                name = data[1]

        print("Highest Paid:", name)
        print("Salary:", high)


def average():
    with open("employee.txt", "r") as file:
        total = 0
        count = 0

        for line in file:
            data = line.strip().split(",")

            total = total + int(data[3])
            count = count + 1

        print("Average Salary:", total / count)

def above():
    salary = int(input("Enter salary: "))

    with open("employee.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if int(data[3]) > salary:
                print(data[1], data[3])


print("All Employees:")
display()

print("\nHighest Paid Employee:")
highest()

print("\nAverage Salary:")
average()

print("\nEmployees above salary:")
above()