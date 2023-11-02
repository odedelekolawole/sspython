# names = ("Kolawole", "Ayodeji", "Odedele")

numbers = tuple([1, 2, 3, 4, 45, 56, 56])

letters = tuple("Kolawole")

print(letters)

names = "Bob", "Kolawole", "Ayodeji"
print(names)

surname = ("Odedele",)
surname2 = ("Odedele")
print(type(surname), surname)
print(type(surname2), surname2)


digits = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
for digit in digits:
    if digit % 3 == 0:
        print(digit)
print(digits[0])
print(digits[-1])

print(7 in digits)
print(11 in digits)

print(f"The length of the tupple {digits} is {len(digits)}")

print(digits.count(10))
print(f"The length {digits} is {len(digits)}")

print(digits)
print(digits.index(10))
print(digits.index(3))

number1 = (1, 2, 3)
number2 = (4, 5, 6)

number1a = [1, 2, 3]
number2a = [4, 5, 6]

numberss = number1 + number2
numbersa = number1a + number2a
print(numberss)
print(numbersa)
