# 21.	Password Validator
'''•	Validate a password based on these conditions: 
o	Minimum 8 characters 
o	At least one uppercase letter 
o	One lowercase letter 
o	One digit 
o	One special character'''

password=input("Enter a password : ")
lower=False
digit=False
special=False
upper=False
for ch in password:
    if ch.isupper():
        upper=True
    elif ch.islower():   
        lower=True
    elif ch.isdigit():
        digit=True
    else:
        special=True
if len(password)>=8 and lower and upper  and digit and special:
    print("valid password")
else:
    print("invalid password")                     