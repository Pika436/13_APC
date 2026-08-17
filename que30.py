# 30.	Store patient names and ages using lists.
'''Perform:
•	Add a patient 
•	Delete a patient 
•	Search a patient 
•	Display all patients 
•	Count total patients
'''

names=[]
ages=[]
while True:
    print("\n-----patient record----")
    print("1.Add a patient")
    print("2.Delete a patient")
    print("3.search a petient")
    print("4.Display all petients")
    print("5.count total petient")
    print("6.Exit")
    
    choice=int(input("enter choice (1-6):"))
    
    if choice==1:
        name=input("Enter petient name :")
        age=int(input("Enter age :"))
        names.append(name)
        ages.append(age)
        print("patient added successfully")
        
    elif choice==2:
         name=input("enter name to delete :")
         if name in names:
             index=names.index(name)
             names.pop(index)
             ages.pop(index)
             print("patient removed successfully")
         else:
             print("patient not found") 
    
    elif choice==3:
        name=input("enter patient name :")
        if name in names:
            index=names.index(name)
            print("petient found ")
            print("Name :",names[index])
            print("Age :",ages[index])
        else:
            print("petient not found") 
        
    elif choice==4:
        print("All petients :")
        for i in range(len(names)):
            print("name :",names[i],"Age :",ages[i])
      
    elif choice==5:
        print("Total petients:",len(names))
    
    elif choice==6:
        print("program ended")
        break
        
    else:
        print("invalid input")                                       
          