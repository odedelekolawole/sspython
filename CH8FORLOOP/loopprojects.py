"""
USING WHILE LOOP

SIMPLE BANKING PROGRAM:
    1. User should deposit cash
    2. User should withdral cash
    3. User should check balance
    4. Quit program
    
    User should tell program to stop when they want
"""

current_balance = 0

while True:
    prompt = int(input("Enter any number to continue or zero to quit:  "))
    
    if prompt != 0:
        
        print("Here are options you have to perform transactions:",[
            {
            "Deposit": 1,
            "Witdrawal": 2,
            "Balance": 3,
            "Quit Program": 4,
        }
        ])
        
        option = int(input("Enter option    "))
        
        if option == 1:
            deposit = int(input("Enter the amount to deposit:   "))
            current_balance = current_balance + deposit
            print("Your current balnce is", current_balance)
            
        elif option == 2:
            withdrwal = int(input("Enter the amount to withdraw:    "))
            current_balance = current_balance - withdrwal
            if withdrwal > current_balance:
                print(f"Your current balance is {current_balance}, You cannot withdraw from this account, kindly deposit into your bank account")
                
            else:
                print(f"Your current balance is {current_balance}")
        
            
        elif option == 3:
            print(f"Cuurent balance is {current_balance}")
            
        elif option == 4:
            print(f"Bye! Thank you for banking with us you are having N{current_balance} remaining in your bank accountt")
            break
        
        else:
            print("""
                  Invalid Option, Kindly
                    "Deposit": 1,
                    "Witdrawal": 2,
                    "Balance": 3,
                    "Quit Program": 4,
                  """)
        
    else:
        print("Be encouraged to bank with us")
        break
        