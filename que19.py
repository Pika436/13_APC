# 19.	Store names of students present in class.
'''Display:
•	Total students 
•	Search a student's attendance 
•	Add a new student 
•	Remove an absent student 
'''

student=['prachi','rahul','sneha','ram','gita','sita']
while True:
    print("\n-----Student attendance-----")
    print("1.Total student")
    print("2.Search a student's attendance ")
    print("3.Add a new student")
    print("4.Remove an absent student ")
    print("5.Display student")
    print("6.Exit")
    
    choice=int(input("enetr choice(1-6): "))
    if choice==1:
        print("total student :",len(student))
    elif choice==2:
        name=input("enter name to search :")
        if name in student:
            print(name,"is present")
        else:
            print(name,"is not present")
    elif choice==3:
        name=input("enter name to add :")
        student.append(name)
        print(name,"added successfully")
    elif choice==4:
        name=input("enter name to delete :")
        if name in student:
          student.remove(name)
          print(name,"removed successfully")
        else:
            print("student not found")  
    elif choice==5:
        print("presend student :",student)
    elif choice==6:
        print("program ended")
        break 
    else:
        print("invalid choice")                                