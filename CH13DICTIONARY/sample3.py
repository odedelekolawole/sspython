phone_book = {
    "Kolawole": 7065586331,
    "Ayodeji": 8012345678,
    "Odedele": 9012345678,
}

print("Kolawole" in phone_book)
print("Deji" in phone_book)

print(phone_book.get("Kolawole"))
print(phone_book["Kolawole"])

phone_book.update([("Bayo", 2345678)])
print(phone_book)

print(phone_book.pop("Bayo"))
print(phone_book)

del phone_book["Ayodeji"]  # This deletes an item from the dictionary
phone_book.clear() # This removes all the items from the dictionary
print(phone_book)   # This prints out the empty dictionary


