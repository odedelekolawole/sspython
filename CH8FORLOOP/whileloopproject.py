"""
Ask the user to enter a number and then enter another number. Add these two numbers together and then ask if they want to add another number. If they enter "y", ask them to enter another number and keep adding numbers until they do not answer "y". Once the loop has stopped, display the total
"""

number1 = int(input("Enter the first number of your choice: "))
number2 = int(input("Enter the second number of your choice:    "))

Total = number1 + number2
print(Total)
answer = "y"

while answer == "y":
    another_number = int(input("Enter another number:   "))
    Total = Total + another_number
    print(f"The total is {Total}")
    answer = input("Do you want to add another number? (y/n)    ")
    print(f"The total is {Total}")