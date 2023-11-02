current_balance = 0
while True:
    prompt = int(input("Enter 0 to exit or any other number to carry out transactions or open an account:   "))
    
    if prompt != 0:
        print(["Here are options for you to carry out transactions: ", {
            
            "1": "Deposit",
            "2": "Withdrawal",
            "3": "Check Balance",
            "4": "Open An Account",
            "5": "Quit Programe",
        }])
        
        option = int(input("Enter an option:    "))
        
        if option == 1:
            deposit = int(input("Enter an amount to deposit:    "))
            current_balance = current_balance + deposit
            print(f"Your current balance is {current_balance}")
            
        
        if option == 2:
            withdrawal = int(input("Enter an amount to withdraw:    "))
            if withdrawal > current_balance:
                print("Insufficient balanace, kindly make a deposit to your bank account")
            current_balance = current_balance - withdrawal
            print(f"Your current balance is {current_balance}")
        
        if option == 3:
            print(f"Your current balance {current_balance}")
        
        
        if option == 4:
            user_name = input("Enter your full name:    ")
            phone_number = int(input("Enter your phone number:  "))
            email_address = input("Enter your email address:    ")
            password = input("Enter your password:  ")
       
            print(f"Account Created Succesffully, details: Username: {user_name}, Email: {phone_number} with {email_address} as your email address")
            
        if option == 5:
            print("Bye thank you for banking with us")
            break
    else:
        print("Kindly be reminded that we offer the best banking services")
        break