def square(num):
    print("num-" + str(num))
    return num ** 2


nums = [1, 2, 3, 4, 5, 6]

print(list(map(square, nums)))  # [1, 4, 9, 16, 25, 36]
print(map(square, nums))  # <map object at 0x00CC1FE8>

print(list(filter(square, nums)))  # [1, 2, 3, 4, 5, 6]

print(list(filter(None, [1, 0, 4, 0, '0', '<-zero', False, 's', True])))


# [1, 4, '0', '<-zero', 's', True]


def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, nums)))  # [2, 4, 6]

lsquare = lambda num: num ** 2  # bad use of lambda as you are giving name to it (use def instead)
print(lsquare(15))

print(list(map(lambda num: num ** 2, nums)))  # [1, 4, 9, 16, 25, 36]
print(list(filter(lambda num: num % 2 == 0, nums)))  # [2, 4, 6]

names = ['Andy', 'Sandy', 'Mandy']

print(list(map(lambda name: name[0], names)))   # ['A', 'S', 'M']
print(list(map(lambda name: name[::-1], names)))    # ['ydnA', 'ydnaS', 'ydnaM']
