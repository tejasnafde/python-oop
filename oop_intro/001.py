class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print('bark!!!!')

class Owner:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

tejas = Owner('tejas', 'blr', '123')
mitushi = Owner('mitushi', 'noida', '456')


dog1 = Dog("Tim", "Puppey", mitushi)
print(dog1.name, dog1.breed, dog1.owner.name)
print('='*20)
dog2 = Dog("Tom", "actually a cat", tejas)
print(dog2.name, dog2.breed, dog2.owner.name)

if dog1 == dog2:
    print("huh but you're a catto??")
else:
    print("i sniffed thru the lies of the jedi meowncil")