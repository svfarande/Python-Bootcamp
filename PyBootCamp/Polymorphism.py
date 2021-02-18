class Animal:
    # is abstract class is that class which we never expect to be instantiated as it has 1 or more abstract method
    # the child class which inherits this parent class should implement abstract method declared in parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass should implement this abstract method")


class Dog(Animal):
    def speak(self):
        print(self.name + " says Bhow!")


class Cat(Animal):
    def speak(self):
        print(self.name + " says Meow!")


def pet_speak(obj):
    obj.speak()     # obj demonstrates Polymorphism using speak() function


kutta = Dog("Kuttu")
billi = Cat("Billu")

for pet in [kutta, billi]:
    print(type(pet))
    pet_speak(pet)
