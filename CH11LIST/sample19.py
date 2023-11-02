table = [
    ["Kolawole", 25, ["gaming", "coding"]],
    ["Ayodeji", 20, ["swimming"]],
    ["Odedele", 26, ["designing", "gaming"]],
    ["Emmanuel", 12, ["piano"]],
    ["Joseph", 14, ["movies"]],
]
hobbies = []
for user in table:
    hobby = user[2]
    hobbies.append(hobby)
print(hobbies)