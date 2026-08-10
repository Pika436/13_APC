# 26.	Caesar Cipher 
# •	Encrypt and decrypt a message using the Caesar Cipher algorithm. 

text=input("enetr message : ")
shift=int(input("enetr shift : "))
encrypted=""
for ch in text:
    if ch.isalpha():
        encrypted+=chr(ord(ch)+shift)
    else:
        encrypted+=ch
print("encrypted msg : ",encrypted)            