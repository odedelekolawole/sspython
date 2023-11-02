guest = ["Adekunle", "Adebayo", "Adewale", "Adefemi"]

search = input("Enter the name of the guest you are searching for in the record: ")

if search in guest:
    print(f"{search} lodged in the hotel overnight")
else:
    print(f"{search} is did not lodge in our hotel today")