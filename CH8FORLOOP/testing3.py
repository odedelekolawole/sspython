print("Craate an account:   ")

first_name = input("Enter your first name:  ")
last_name = input("Enter your last name:  ")
middle_name = input("Enter middle name:  ")
email_address = input("Enter email address:  ")
phone_number = input("Enter your phone number:  ")
password = input("Enter your password:  ")
if len(phone_number) > 11 or len(phone_number) < 11:
    print("Your phone number does not meet the requeired length")
    password = input("Enter your password")
if len(password) < 8:
    print("Reset your password, Password too weak")
else:
    print("Account Created Successfully")