# Python inheritance

class intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(f"My Name is {self.name}. And My age is {self.age}")    

# Initialise

person1 = intro("Ashu Sagar", 23)
person2 = intro("Karan Aujla", 25)


# Access

person1.printName()
person2.printName()




class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
       pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def make_sound(self):
        return "Meow!"


my_dog = Dog("Buddy", "Golden Retriever")
my_cat = Cat("Whiskers", "Gray")

print(my_dog.name)   # Output: Buddy
print(my_cat.name)  # Output: Cat
