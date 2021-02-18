print(list(range(0, 12, 2)))  # [0, 2, 4, 6, 8, 10]
# note start is by default 0 only when stop is given ex. range(10) will go from 0 to 9
# also step is optional and by default its 1
# in actual stop is skipped and range acts from start to step - 1
for n in range(0, 12, 2):  # range(start,stop,step)
    print(n)  # prints even no. from 0 to 10

print(list(enumerate("Hello")))  # indexing for each letter ; [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

for i, l in enumerate("Hello"):
    print(str(i) + " -> " + l)

print(list(
    zip([1, 2, 3], ["a", "b", "c"], [100, 200, 300])))  # combines lists ; [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

for x, y, z in zip([1, 2, 3], ["a", "b", "c"], [100, 200, 300]):
    print(str(x) + " <-> " + y + " <-> " + str(z))

print('x' in ['y', 'eq', 'x'])  # True
print('1' in [5, 6, 7])  # False
print('H' in 'Hello')  # True
print('mykey' in {'mykey': 99})  # True
d = {'mykey': 99}
print(99 in d.values())  # True

num = [5, 5, 2, 4, 1]
print(min(num))  # 1
print(max(num))  # 5

from random import shuffle  # shuffle is function from random library which mix elements inplace

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle(mylist))  # None
print(mylist)  # [1, 6, 7, 9, 3, 4, 10, 2, 5, 8]
shuffle(mylist)
print(mylist)  # [4, 7, 10, 5, 2, 1, 9, 8, 6, 3]

from random import randint

print(randint(1, 6))  # gives random integer from 1 to 6 including start and stop

result = input("Enter anything : ")  # takes input from user in format of string    # Enter anything : 6
print(result)  # 6
print(type(result))  # <class 'str'>

i = float(input("Enter Integer : "))  # type cast it to specific data type which you want   # Enter Integer : 6
print(i)  # 6.0
#####################################################################################################
# instead of using append() and for loop to create list we can go with below statement which flattens for loop
# basically what goes in append() is kept before for loop
mylist = [letter for letter in "Shubham"]
print(mylist)  # ['S', 'h', 'u', 'b', 'h', 'a', 'm']

mylist = [num ** 2 for num in range(0, 10) if num % 2 == 0]
print(mylist)  # [0, 4, 16, 36, 64]

mylist = [x if x % 2 == 0 else "Odd" for x in range(0, 11)]
print(mylist)  # [0, 'Odd', 2, 'Odd', 4, 'Odd', 6, 'Odd', 8, 'Odd', 10]

celcius = [0, 10, 35, 100]
fahrenhite = [((9 / 5) * temp + 32) for temp in celcius]
print(fahrenhite)  # [32.0, 50.0, 95.0, 212.0]

nested = []
for x in [2, 4, 6]:
    for y in [1, 10, 100]:
        nested.append(x * y)
print(nested)   # [2, 20, 200, 4, 40, 400, 6, 60, 600]

# above nested loop can be done in 1 statement as below

nested = [x * y for x in [2, 4, 6] for y in [1, 10, 100]]
print(nested)   # [2, 20, 200, 4, 40, 400, 6, 60, 600]
