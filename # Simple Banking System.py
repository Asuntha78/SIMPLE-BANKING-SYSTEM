 # Simple Banking System

accounts = {    1001:{'name' : "Alice",  'balance' : 8000},
                1002:{'name' : "Zoey", 'balance' : 10000}
            }


print("Welcome")
print()

while True:
    print()
    print("Main Menu")
    print()
    print("1. Create an account")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. Balance Enquiry")
    print("5. Exit")
    print()

    activity = int(input("Choose an option : "))
    print()

    # Creating new account numbers
    highest = max(accounts.keys())
    new_account_number = highest + 1

    if activity == 1:
        name = str(input("Enter your name : "))
        print("New account created")
        print(f"Your account number is : {new_account_number}")
        print()
        accounts[new_account_number] = {'name':name , 'balance':0}

    elif activity == 2:
        acc_no = int(input("Enter your account number:"))
        if acc_no in accounts:
            print("Account found")
            amount = float(input("How much do you want to withdraw? " ))
            if amount <= 0:
                print("Invalid amount!")
            else:
                if amount > accounts[acc_no]['balance']:
                    print("Available balance is less than the requested amount!")
                    print("Please check your current balance and try again!")
                else:
                    accounts[acc_no]['balance'] -= amount
                    print(f"Withdrawal successful")
                    print(F"Your current balance is {accounts[acc_no]['balance']}")
        else:
            print("Account not found!")


    elif activity == 3:
        acc_no = int(input("Enter your account number:"))
        if acc_no in accounts:
            print("Account found")
            deposit = float(input("How much do you want to deposit? "))
            if deposit <= 0:
                print("Invalid amount!")
            else:
                accounts[acc_no]['balance'] += deposit 
                print("Deposit successful")
                print(f"Your current balance is : {accounts[acc_no]['balance']}")           
        else:
            print("Account not found!")
 

    elif activity == 4:
        acc_no = int(input("Enter your account number:"))
        if acc_no in accounts:
            print("Account found")
            print(f"Your available balance is : {accounts[acc_no]['balance']} ")
        else:
            print("Account not found!")

    elif activity == 5:
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid option. Please select a number between 1 and 5.")