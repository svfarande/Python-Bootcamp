t1 = ('1', "Shubham", 1, 4.5, 1)
print(t1)  # ('1', 'Shubham', 1, 4.5, 1)

print(t1[::-1])  # (1, 4.5, 1, 'Shubham', '1')
print(t1.count(1) + t1.index("1") + t1.index(1))  # 2+0+2=4

t2 = (2, "Farande", 9.0, {'key1': 'value1', 'key2': 'value2'}, ['5', '4.5', 'hi'])
t = t1 + t2
print(t)  # ('1', 'Shubham', 1, 4.5, 1, 2, 'Farande', 9.0)

# t1[1] = "Shubham"  # 'tuple' object does not support item assignment

# myset = set(2,1,3,3,2,1)       # set expected at most 1 argument which is iterable, got 6
myset = set()
myset.add(5)
myset = {2, 3, 1, 3, 't'}
myset.add('t')
print(myset)  # {1, 2, 3, 't'}

list1 = [2, 2, 2, 2, 1, 1, 1, 4, 3, 4, 3]
myset = set(list1)
print(myset)  # {1, 2, 3, 4}

list2 = [2, 1, 1, 4, 3, 4, 78, 90, 98, 5]
myset = set(list2)
print(myset)  # {1, 2, 3, 4, 98, 5, 78, 90}

print(set('Mmississippi'))  # {'m', 'i', 'M', 's', 'p'}
