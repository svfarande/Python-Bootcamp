# Python code to demonstrate the working of zip and unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

print(mapped)   # <zip object at 0x0160FE08>
print(type(mapped))  # <class 'zip'>

print(*mapped)    # unzipping
# ('Manjeet', 4, 40) ('Nikhil', 1, 50) ('Shambhavi', 3, 60) ('Astha', 2, 70)
# it will lead to - ValueError if we further try to unzip it again using *mapped
# ValueError: not enough values to unpack (expected 3, got 0) Hence zipping it again
mapped = zip(name, roll_no, marks)

# converting values to print as list # can be converted to set or tuples also
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)
# The zipped result is : [('Manjeet', 4, 40), ('Nikhil', 1, 50), ('Shambhavi', 3, 60),
# ('Astha', 2, 70)]

print("\n")

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)     # The name list is : ('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')

print("The roll_no list is : ", end="")
print(roll_noz)     # The roll_no list is : (4, 1, 3, 2)

print("The marks list is : ", end="")
print(marksz)       # The marks list is : (40, 50, 60, 70)

# NOTE -
# ZIP will not error out if there are less elements in any container
# Return a zip object whose .__next__() method returns a tuple where the i-th element comes
# from the i-th iterable argument. The .__next__() method continues until the shortest iterable in
# the argument sequence is exhausted and then it raises StopIteration.
print(*zip(['a', 'b', 'c', 'd'], range(1, 4)))  # ('a', 1) ('b', 2) ('c', 3)
