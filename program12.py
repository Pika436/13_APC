# 12. Read a text file and count how many times each word occurs. Display the result using a dictionary.

with open("student.txt", "r") as file:
    content = file.read()

words = content.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
print(word_count)
    