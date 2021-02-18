def what_i_do():
    print("I eat & sleep")


class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I'm animal")


class Dog(Animal):
    def __init__(self):
        print("Dog created")

    def who_am_i(self):
        print("I'm Dog")


myanimal = Animal()
myanimal.who_am_i()
what_i_do()

mydog = Dog()
mydog.who_am_i()
what_i_do()
