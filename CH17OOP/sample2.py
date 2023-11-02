class Person:
    species = "Human"
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
    def talk(self):
        print(f"Hello, I am a {self.name} and I am a {self.species}")
    
print(Person.species)

person1 = Person(name="Kolawole", age=20)
print(type(person1))
print(person1.species)
print(person1.talk())