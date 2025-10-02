class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello! My name is {self.name} and i'm {self.age} years old")

person1 = Person("tejas", 3)
person2 = Person('mitushi', 1)
people = [person1, person2]

for idx, person in enumerate(people):
    if people[idx-1] and people[idx-1] != people[idx]:
        person.greet()
        print("="*30)  