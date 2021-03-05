import re

# OR (|) operator
print(re.search(r'man | woman', 'This is man here'))
# <re.Match object; span=(8, 12), match='man '>
print(re.search(r'man | woman', "This is woman here"))
# <re.Match object; span=(7, 13), match=' woman'>

# Wildcard (.) operator
print(re.findall(r'ba.', 'I have bat and ball'))    # ['bat', 'bal']
print(re.findall(r'ba\S+', 'I have bat and ball'))  # ['bat', 'ball']

# Start with (^) operator
print(re.findall(r"^\d", '1 is a number.\n2 is also a number.'))    # ['1']
print(re.findall(r'^\d', 'The number is 1\n2 is also a number'))    # []

# End with ($) operator
print(re.findall(r'\d$', 'The number is 1\nNow the number is 2'))   # ['2']

# Note that this is for the entire string, not individual words!

# Exclusion
# To exclude characters, we can use the ^ symbol in conjunction with a set of brackets [].
# Anything inside the brackets is excluded.
print(re.findall(r'[^\d]', '65This sentence 42 contains 3 random numbers'))
# ['T', 'h', 'i', 's', ' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', ' ', ' ', 'c', 'o', 'n', 't',
# 'a', 'i', 'n', 's', ' ', ' ', 'r', 'a', 'n', 'd', 'o', 'm', ' ', 'n', 'u', 'm', 'b', 'e', 'r',
# 's']
print(re.findall(r'[^\d]+', '65This sentence 42 contains 3 random numbers'))
# ['This sentence ', ' contains ', ' random numbers']
print(re.findall(r'[^\d ]+', '65This sentence 42 contains 3 random numbers'))
# ['This', 'sentence', 'contains', 'random', 'numbers']
print(re.findall(r'[^!.? ]+', 'This is a string! It has punctuation. Can we remove it?'))
# ['This', 'is', 'a', 'string', 'It', 'has', 'punctuation', 'Can', 'we', 'remove', 'it']
print(' '.join(re.findall(r'[^!.? ]+', 'This is a string! It has punctuation. Can we remove it?')))
# This is a string It has punctuation Can we remove it

print(re.findall(r'\w-\w', 'This sentence-contains false hyphen in-words. Find-them.'))
# ['e-c', 'n-w', 'd-t']
print(re.findall(r'\w+-\w+', 'This sentence-contains false hyphen in-words. Find-them.'))
# ['sentence-contains', 'in-words', 'Find-them']
# Inclusion
# Remember brackets can be used for inclusion as well as exclusion
print(re.findall(r'[\w+]-[\w+]', 'This sentence-contains false hyphen in-words. Find-them.'))
# ['e-c', 'n-w', 'd-t']

text = "Hi! Is this catfish ?"
text2 = "Hi! Do you want to take catnap ?"
text3 = "Hi! Is this caterpillar ?"

print(re.search(r'cat(fish|nap|claw)', text))   # <re.Match object; span=(12, 19), match='catfish'>
print(re.search(r'cat(fish|nap|claw)', text2))  # <re.Match object; span=(24, 30), match='catnap'>
print(re.search(r'cat(fish|nap|claw)', text3))  # None
print(re.search(r'cat(fish|nap|erpillar)', text3))
# <re.Match object; span=(12, 23), match='caterpillar'>
