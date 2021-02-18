from collections import Counter

# most occurred comes 1st and added as per their occurrence

my_list = [1, 'a', 2, 3, 4, 2, 2, 3, 4, 1, 2, 3, 4]
print(Counter(my_list))  # Counter({2: 4, 3: 3, 4: 3, 1: 2, 'a': 1})

print(Counter('Shu6hAm farande'))
# Counter({'h': 2, 'a': 2, 'S': 1, 'u': 1, '6': 1, 'A': 1, 'm': 1, ' ': 1, 'f': 1, 'r': 1,
# 'n': 1, 'd': 1, 'e': 1})

sentence = 'Count words in this sentence. It should have 5 words .'
l_sentence = list(sentence.split())
print(Counter(l_sentence))  # Counter({'words': 2, 'Count': 1, 'in': 1, 'this': 1, 'sentence.': 1,
# 'It': 1, 'should': 1, 'have': 1, '5': 1, '.': 1})

c = Counter('fajkekqwjNFRNGKJNAenvjkefkjn')

print(c)  # Counter({'j': 4, 'k': 4, 'e': 3, 'N': 3, 'f': 2, 'n': 2, 'a': 1, 'x': 1, 'w': 1,
# 'F': 1, 'R': 1, 'G': 1, 'K': 1, 'J': 1, 'A': 1, 'v': 1})
print(type(c))  # <class 'collections.Counter'>

# n most common entries - print(c.most_common(n))
print(c.most_common(3))  # [('j', 4), ('k', 4), ('e', 3)]

# n least common entries - print(c.most_common()[:-n-1:-1])
print(c.most_common())  # [('j', 4), ('k', 4), ('e', 3), ('N', 3), ('f', 2), ('n', 2), ('a', 1),
# ('x', 1), ('w', 1), ('F', 1), ('R', 1), ('G', 1), ('K', 1), ('J', 1), ('A', 1), ('v', 1)]
print(c.most_common()[:-4:-1])  # 3 least common    # [('v', 1), ('A', 1), ('J', 1)]

print(c.values())  # dict_values([2, 1, 4, 4, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1])
print(sum(c.values()))  # 28

print(list(c))  # ['f', 'a', 'j', 'k', 'e', 'x', 'w', 'N', 'F', 'R', 'G', 'K', 'J', 'A', 'n', 'v']
print(set(c))  # {'v', 'G', 'x', 'a', 'w', 'N', 'j', 'J', 'A', 'n', 'K', 'F', 'f', 'R', 'e', 'k'}
print(dict(c))  # {'f': 2, 'a': 1, 'j': 4, 'k': 4, 'e': 3, 'x': 1, 'w': 1, 'N': 3, 'F': 1, 'R': 1,
# 'G': 1, 'K': 1, 'J': 1, 'A': 1, 'n': 2, 'v': 1}

print(c.items())    # dict_items([('f', 2), ('a', 1), ('j', 4), ('k', 4), ('e', 3), ('x', 1),
# ('w', 1), ('N', 3), ('F', 1), ('R', 1), ('G', 1), ('K', 1), ('J', 1), ('A', 1), ('n', 2), ('v',
# 1)])
print(Counter(dict(c.items())))  # Counter({'j': 4, 'k': 4, 'e': 3, 'N': 3, 'f': 2, 'n': 2, 'a': 1,
# 'x': 1, 'w': 1, 'F': 1, 'R': 1, 'G': 1, 'K': 1, 'J': 1, 'A': 1, 'v': 1})

'''
Common patterns when using the Counter() object
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''
