print("*************~~~WELCOME TO ATM~~~*************")

total = 20000

pin = int(input("Enter your pin: "))

if pin != 123:
    print("Invalid pin")
else:
    service= input("Enter the transaction:\nWithdraw\nBalance enquiry\nDeposit\n")

    if service.lower() == "withdraw":
        amount = int(input("Enter the amount: "))

        if amount > total:
            print("Insufficient balance")
        else:
            total = total - amount
            print("Transaction Successful!")
            print(f"Balance amount in your account ₹{total}")

    elif service.lower() == "deposit":
        deposit = int(input("Enter the amount to deposit: "))

        if deposit < 0:
            print("Enter a valid amount")
        else:
            total = total + deposit
            print("Transaction Successful!")
            print(f"Balance amount in your account ₹{total}")

    elif service.lower().rstrip() == "balanceenquiry":
        print(f"Account Balance ₹{total}")

    else:
        print("Please enter a valid transaction")