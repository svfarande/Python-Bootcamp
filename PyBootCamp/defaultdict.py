from collections import defaultdict

name = 'shubham'

# assign default value as empty string '', int -> 0, list -> empty list, etc
# you can use any callable like function or lambda expression to give your own default value
d = defaultdict(str)    # d = {} # would lead to KeyError while accessing absent key

for i in name:
    d[i] = i.upper()

print(d)  # defaultdict(<class 'str'>, {'s': 'S', 'h': 'H', 'u': 'U', 'b': 'B', 'a': 'A', 'm': 'M'})
print(d['b'])   # B

print(d.items())
# dict_items([('s', 'S'), ('h', 'H'), ('u', 'U'), ('b', 'B'), ('a', 'A'), ('m', 'M')])

d1 = defaultdict(lambda: 'O')
print(d1['u'])  # O


def absent_key():
    print('Hi')
    return 'absent'


d3 = defaultdict(absent_key)
# d3 = defaultdict(absent_key()) -> TypeError: first argument must be callable or None
print(d3['WRONG KEY'])  # Hi \n absent
print(d3)   # defaultdict(<function absent_key at 0x01468028>, {'WRONG KEY': 'absent'})
