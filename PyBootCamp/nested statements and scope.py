x = 10


def func(x):
    print(f'2 X is {x}')  # 2 X is 10
    x = 20
    print(f'3 X is {x}')  # 3 X is 20

    def func2(x):
        print(f'4 X is {x}')  # 4 X is 20
        x = 30
        print(f'5 X is {x}')  # 5 X is 30

    func2(x)


print(f'1 X is {x}')  # 1 X is 10
func(x)
print(f'6 X is {x}')  # 6 X is 10
