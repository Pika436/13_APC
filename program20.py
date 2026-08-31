# 20. Store deposits and withdrawals in a file. Read the file and calculate:  • Total deposits  • Total withdrawals  • Final balance  • Largest transaction 
def calculate():
    total_deposit = 0
    total_withdraw = 0
    largest = 0

    with open("bank.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            type = data[0]
            amount = int(data[1])

            if type == "D":
                total_deposit += amount
            elif type == "W":
                total_withdraw += amount

            if amount > largest:
                largest = amount

    balance = total_deposit - total_withdraw

    print("Total Deposits:", total_deposit)
    print("Total Withdrawals:", total_withdraw)
    print("Final Balance:", balance)
    print("Largest Transaction:", largest)


calculate()