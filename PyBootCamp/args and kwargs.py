def add(*args):
    print(args)  # prints tuple of arguments ex. (5,5)
    print(*args)  # prints arguments separated by space
    return sum(args)


print(add(5, 5))  # 10
print(add(5, 5, 5))  # 15


def myfunc(**kwargs):
    print(kwargs)  # {'a': 'A', 'b': 'B', 'c': 'C'}
    # print(**kwargs) gives Error
    print(kwargs['b'])  # B


myfunc(a="A", b="B", c="C")


# note args and kwargs are variables and can have any name as variable


def myfunc(m, *args, a, **kwargs):
    print(args)  # ('shubham', 'farande')
    print(kwargs)  # {'firstname': 'shubham', 'lastname': 'farande'}
    print(f"{m} name {a} {args[0]} {kwargs['lastname']}")  # My name - shubham farande


myfunc("My", "shubham", "farande", a="-", firstname="shubham", lastname="farande")
