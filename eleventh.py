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
