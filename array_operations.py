from array import array

a = array('i', [3, 5, 8, 9, 2])

# 1. append()
a.append(20)
print("1. After append:", a)


# 2. buffer_info()
print("2. Buffer info:", a.buffer_info())


# 3. byteswap()
'''
a.byteswap()
print("3. After byteswap:", a)
'''

# 4. count()
print("4. Count of 3:", a.count(3))


# 5. extend()
a.extend([10, 30])
print("5. After extend:", a)


# 6. frombytes()
b = array('i')
b.frombytes(a.tobytes())
print("6. After frombytes:", b)


# 7. fromfile()
# First create a binary file
with open("data.bin", "wb") as f:
    a.tofile(f)

c = array('i')
with open("data.bin", "rb") as f:
    c.fromfile(f, len(a))

print("7. After fromfile:", c)


# 8. fromlist()
d = array('i')
d.fromlist([10, 20, 30])
print("8. After fromlist:", d)


# 9. fromunicode()
u = array('u')
u.fromunicode("Python")
print("9. After fromunicode:", u)


# 10. index()
print("10. Index of 8:", a.index(8))


# 11. insert()
a.insert(1, 100)
print("11. After insert:", a)


# 12. pop()
x = a.pop()
print("12. Popped element:", x)
print("    Array after pop:", a)


# 13. remove()
a.remove(100)
print("13. After remove:", a)


# 14. reverse()
a.reverse()
print("14. After reverse:", a)


# 15. tobytes()
byte_data = a.tobytes()
print("15. Tobytes:", byte_data)


# 16. tofile()
with open("output.bin", "wb") as f:
    a.tofile(f)
print("16. Array written to file")


# 17. tolist()
list_data = a.tolist()
print("17. To list:", list_data)


# 18. tounicode()
print("18. To unicode:", u.tounicode())