#9.	Design an ATM class that allows a user to:
'''
a)	Check balance 
b)	Deposit money 
c)	Withdraw money 
d)	Display account details
Create an object of the class and implement the operations through a menu-driven program.
'''

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited successfully.")
        print("Updated Balance: Rs.", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Please collect your cash.")
            print("Remaining Balance: Rs.", self.balance)
        else:
            print("Insufficient balance.")

    def display_account(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance: Rs.", self.balance)


# Creating object
obj = ATM(12345, "Prachi", 10000)

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        obj.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        obj.withdraw(amount)

    elif choice == 4:
        obj.display_account()

    elif choice == 5:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")
        