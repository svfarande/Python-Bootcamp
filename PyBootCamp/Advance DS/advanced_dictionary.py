# dictionary comprehension

d = {x: x * x for x in range(10)}
print(d)    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

'''The purpose of zip() is to map the similar index of multiple containers so that 
they can be used just using as single entity.'''

d = {k: v * v for k, v in zip(['a', 'b', 'c', 'd'], range(1, 5))}
print(d)    # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

d = {k: v * v for k, v in zip(['a', 'b', 'c', 'd'], range(1, 6))}
print(d)    # {'a': 1, 'b': 4, 'c': 9, 'd': 16}

print(d.items())    # dict_items([('a', 1), ('b', 4), ('c', 9), ('d', 16)])
for i in d.items():
    print(i)

print(d.keys())     # dict_keys(['a', 'b', 'c', 'd'])
print(d.values())   # dict_values([1, 4, 9, 16])
