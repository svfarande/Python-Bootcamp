def test_yield():
    yield "yield - abc"
    return "return - abc"  # this is not being returned because of yield in previous statement


print(test_yield())  # this will not print what is yielded but it will return generator object
# <generator object test_yield at 0x020B84F8>
# to print what is yielded we need to iterate over generator object as below -

for i in test_yield():
    print(i)  # yield - abc
