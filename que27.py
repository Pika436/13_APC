# 27.	Email Validator 
# •	Validate whether a given email address follows a valid format. 

email=input("enter a email : ")
if email.count("@")!=1:
    print("invalid format")
else:
    username,domain=email.split("@")
    if username=="":
        print("invalid format")
    elif " " in email:
        print("invalid format")
    elif ".." in email:
        print("invalid format")
    elif "." not in domain:
        print("invalid format")
    elif len(domain.split(".")[-1])<2:
        print("invalid format")    
    else:
        print("valid format")                        
 