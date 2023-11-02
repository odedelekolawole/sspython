
first_number = int(input("Enter the first number:   "))
operator = input("Enter the operator for the operation: ")
second_number = int(input("Enter the second number:   "))

if operator == "+":
    result = first_number + second_number
    print(f"The result of your operation is: {result}")
    
elif operator == "-":
    result = first_number - second_number
    print(f"The result of your operation is: {result}")
    
elif operator == "*":
    result = first_number * second_number
    print(f"The result of your operation is: {result}")
    
elif operator == "/":
    result = first_number / second_number
    print(f"The result of your operation is: {result}")
    
elif operator == "**":
    result = first_number ** second_number
    print(f"The result of your operation is: {result}")
    
else:
    print("Operation ot recognise as a mathethematical operation")
    
    