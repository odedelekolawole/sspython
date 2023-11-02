def add(x, y, *values):
    total = x + y
    for value in values:
        total = total + value
    return total
print(add(12, 23, 45, 56, 78, 90, 45.3))
