# 13. Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears. 
word = input("Enter word: ")

count = 0
line_no = 0

with open("student.txt", "r") as file:
    for line in file:
        line_no += 1
        
        if word in line:
            count += line.count(word)
            print("Found in line:", line_no)

print("Total occurrences:", count)