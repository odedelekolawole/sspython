"""
Print the even numbers from 0 to a number entered in a keyboard, make sure the number supplied is not less than 50
"""

random_number = int(input("Enter a randon number greaer than or qual to 50:   "))
if random_number >= 50:
    for number in range(0, random_number, 2):
        print(number)       
else:
    print("You have supplied an invalid number")
    
"""
Another Method 
"""

# random_number2 = int(input("Enter a randon number greaer than or qual to 50:   "))
# for number2 in range(random_number2):
#     if (number2 % 2 == 0):
#         print(number2)