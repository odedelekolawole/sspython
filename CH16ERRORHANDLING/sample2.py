def add_two_numbers(number1, number2):
    if (type(number1) != int) or (type(number2) != int):
        raise TypeError("Numbers should be integers")
    elif (number1 < 0) or (number2 < 0):
        raise ValueError("Number should not be negative integer")
    else:
        return number1 + number2
# sum1 = add_two_numbers("Kolawole", "Odedele")
sum2 = add_two_numbers(12, 13)

# print(sum1)
print(sum2)





def multiply_number(number1, number2):
    if (type(number1) != int) or (type(number2) != int):
        raise TypeError("Number is not an integer")
    elif (number1 < 0) or (number2 < 0):
        raise ValueError("The number is not a positive interger")
    return number1 * number2
print(multiply_number("kolawole", 5))
    