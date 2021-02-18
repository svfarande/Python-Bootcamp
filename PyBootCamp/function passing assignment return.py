print("\n-------------------- Function Assignment and Deletion  --------------------")


def heloo():
    return "Hi"


print("heloo() defined - ")
print(type(heloo))  # <class 'function'>
print(heloo)    # <function heloo at 0x00ED7FA0>
print(heloo())  # Hi

greet = heloo

print("\ngreet = heloo -")
print(type(greet))  # <class 'function'>
print(greet)    # <function heloo at 0x00ED7FA0>
print(greet())  # Hi

del heloo

# print(type(heloo)) # NameError: name 'heloo' is not defined
# print(heloo)  # NameError: name 'heloo' is not defined
# print(heloo())    # NameError: name 'heloo' is not defined

print("\ndel heloo -")
print(type(greet))  # <class 'function'>
print(greet)    # <function heloo at 0x00ED7FA0>
print(greet())  # Hi

print("\n-------------------- Function Within Function --------------------")


def hello(name):
    print(f"\nhello(\"{name}\") - ")

    def greetings():
        return "\t greetings()"

    def welcome():
        print("\t welcome()")

    print(greetings())
    welcome()

    if name == "Shubham":
        return greetings
    elif name == "Python":
        return welcome

    print("hello() ended")


print(hello("Shubham"))
'''
hello("Shubham") - 
	 greetings()
	 welcome()
<function hello.<locals>.greetings at 0x00EE7148>
'''

# greetings()   # NameError: name 'greetings' is not defined
# welcome() # NameError: name 'welcome' is not defined
print(hello("Python"))
'''
hello("Python") - 
	 greetings()
	 welcome()
<function hello.<locals>.welcome at 0x00EE7100>
'''
print(hello("Foo"))
'''
hello("Foo") - 
	 greetings()
	 welcome()
hello() ended
None
'''

print("\n-------------------- Function Return & Assignment --------------------")

outside_greetings = hello("Shubham")
print(outside_greetings)
print(outside_greetings())

'''
hello("Shubham") - 
	 greetings()
	 welcome()
<function hello.<locals>.greetings at 0x00EE7148>
	 greetings()
'''

outside_welcome = hello("Python")
print(outside_welcome)
print(outside_welcome())

'''
hello("Python") - 
	 greetings()
	 welcome()
<function hello.<locals>.welcome at 0x00EE70B8>
	 welcome()
None
'''

print("\n-------------------- Function Passing --------------------")


def hellow():
    return "Hellow there"


def hi(my_func):
    print("Hi there")
    print(my_func())


hi(hellow)  # Note - its not hi(hellow())
'''
Hi there
Hellow there
'''