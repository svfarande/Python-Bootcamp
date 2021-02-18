class Dog:
    species = "mammal"  # This will stay as it is regardless of instance of class

    def __init__(self, name="StreetDog", breed="Unknown"):  # defaulting breed & name if not passed
        self.breed = breed
        self.name = name

    def bark(self, num):
        print(f"Dog {num} - Bhow! My name is {self.name} and my breed is {self.breed}. I belong to {self.species}\n")


mydog1 = Dog("Kalu", "Lab")
mydog2 = Dog("Balu", "Pug")
mydog3 = Dog()

print(mydog1.name + "(" + mydog1.breed + ") - ")  # Kalu(Lab) -
mydog1.bark(1)  # Dog 1 - Bhow! My name is Kalu and my breed is Lab. I belong to mammal

print(mydog2.name + "(" + mydog2.breed + ") - ")  # Balu(Pug) -
mydog2.bark(2)  # Dog 2 - Bhow! My name is Balu and my breed is Pug. I belong to mammal

print(mydog3.name + "(" + mydog3.breed + ") - ")  # StreetDog(Unknown) -
mydog3.bark(2)  # Dog 2 - Bhow! My name is StreetDog and my breed is Unknown. I belong to mammal
