phone_book =  {
    "Kolawole": 7065586331,
    "Ayodeji": 8012345678,
    "Odedele": 9012345678,
}
print(phone_book["Kolawole"])

phone_book["Donald"] = 123456
print(phone_book)
print(type(phone_book))

print(phone_book.items())



for key, value in phone_book.items():
    print(f"name: {key} => phone number: {value}")
    
print(phone_book.keys())
print(phone_book.values())


for keys in phone_book.keys():
    print(keys)
    
for values in phone_book.values():
    print(values)