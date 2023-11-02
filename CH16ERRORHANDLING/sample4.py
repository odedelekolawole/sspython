def divide_number(number1, number2):
    try:
        quotient = number1 / number2
    except ZeroDivisionError  as ZDError:
        print(f"{ZDError}: None of the numbers should be Zero (0)")
    except TypeError as TE:
        print(f"{TE}: Please provide a valid integer")
    else:
        print(f"Quotient: {quotient}")
    finally:
        print("exiting")




divide_number(12, 3)
divide_number(12, 0)
divide_number("Kolawole", 23)