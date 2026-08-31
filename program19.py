# 19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%. 
def attendance():
    with open("attendance.txt", "r") as file:

        for line in file:
            data = line.strip().split(",")

            roll_no = data[0]
            name = data[1]
            present = int(data[2])
            total = int(data[3])

            percentage = (present / total) * 100

            print(name, "Attendance:", percentage, "%")

            if percentage < 75:
                print("Below 75%:", name)


attendance()