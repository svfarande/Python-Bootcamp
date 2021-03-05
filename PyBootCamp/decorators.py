def new_decorator(orignal_func):
    def wrap():
        print("Code before orignal_func()")

        orignal_func()

        print("Code after orignal_func()")

    return wrap


@new_decorator
def i_need_decoration():
    print("Main Code")


i_need_decoration()

'''
Either add @<decorator_name> (@new_decorator) syntax before function definition 
which needs decoration and then call that function as shown above.
--OR--
pass the function which needs decoration (i_need_decoration) to decorator function 
(new_decorator(i_need_decoration)) and get it assigned to some variable and then call the 
decorated function using that variable as shown below.
'''

# remember to only pass function pointer and not call the actual function
# decorated = new_decorator(i_need_decoration)
# decorated()

# ------------------------- If function takes & return's something -----------------------------


def decoration(original_func):
    def inner(num):
        print('Code Before Function')

        squared = original_func(num)

        print('Code After Function')
        return squared

    return inner


@decoration
def i_need_decoration(num):
    print(f'This function calculates square')
    return num * num


print(i_need_decoration(5))

'''
Code Before Function
This function calculates square
Code After Function
25
'''

# ------------------------- Generic version using *args & **kwargs ----------------------------


def decoration(original_func):
    def inner(*args, **kwargs):
        print('Code Before Function')

        squared = original_func(*args, **kwargs)

        print('Code After Function')
        return squared

    return inner


@decoration
def i_need_decoration1(num):
    print(f'This function calculates square')
    return num * num


@decoration     # using same decoration as above function
def i_need_decoration2(num, power):
    print(f'This function calculates power of number')
    return num ** power


print(i_need_decoration1(5))
print(i_need_decoration2(5, 3))

'''
Code Before Function
This function calculates square
Code After Function
25
Code Before Function
This function calculates power of number
Code After Function
125
'''

