# count lines,words,and characters in a text file
file = open("sample.txt", "r")

lines = 0
words = 0
characters = 0

for line in file:
    lines += 1
    words += len(line.split())
    characters += len(line)

file.close()

print("Number of lines:", lines)
print("Number of words:", words)
print("Number of characters:", characters)


