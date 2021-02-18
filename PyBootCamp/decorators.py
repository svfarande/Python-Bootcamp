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
