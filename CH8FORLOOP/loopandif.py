"""
Getting the sum if even numbers 0 to 100
"""


total = 0

start_value = int(input("Enter the start value: "))
stop_value = int(input("Enter the stop value:   "))


for number in range(start_value, stop_value):
    if (number % 2 == 0):
        print(number)
        print(f"Total: {total}")
        if number == 100:
            continue
        total += number
print(f"Total of even numbers: {total}")