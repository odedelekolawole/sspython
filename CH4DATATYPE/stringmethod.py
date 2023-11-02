sentence1 = "I am travelling to the space"
sentence2 = "I AM TRAVELLING TO THE SPACE"
sentence3 = "i am travelling to the space"
print(sentence1.upper())
print(sentence2.lower())
print(sentence3.capitalize())


"""
Replace Method
"""
print(sentence1.replace("I", "We"))

"""
String formatting
"""
# Method1
sentence4 = "My name is {} and I am {}".format("Kolawole", 25)
print(sentence4)

# Method2
name = "Ayodeji"
age = 24
sentence4 = "My name is {} and I am {}".format(name, age)
print(sentence4)

# Method3
name = "Emmanuel"
age = 23
sentence4 = f"My name is {name} and I am {age}"
print(sentence4)  