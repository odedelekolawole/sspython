import math
# Volume of a cylinder = PI x (radius ** 2) * height

number1 = int(input("Enter first number:    "))
number2 = int(input("Enter second number:    "))
def calculator(number1, number2):
    total = number1 + number2
    product = number1 * number2
    quotient = number1 / number2
    subtract = number1 - number2

    return total, product, quotient, subtract

total, product, quotient, subtract = calculator(number1, number2) 

print(f"{number1} + {number2} = {total}")
print(f"{number1} * {number2} = {product}")
print(f"{number1} / {number2} = {quotient}")
print(f"{number1} - {number2} = {subtract}")