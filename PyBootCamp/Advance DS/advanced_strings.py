s = 'hellow world'

print(s.capitalize())       # Hellow world
print(s.lower())            # hellow world
print(s.upper())            # HELLOW WORLD
print(s)                    # hellow world
print(s.count('o'))         # 2
print(s.find('o'))          # 4 # 1st occurrence of that string
print(s.center(20, 'z'))    # zzzzhellow worldzzzz  #  places the string in center
print('hello world'.center(20, 'z'))    # zzzzhello worldzzzzz
print(s.center(10, 'z'))    # hellow world
print('hello\tworld'.expandtabs())  # hello   world
print('hello\tworld')   # hello   world

print(s.isnumeric())    # False
# A string is numeric if all characters in the string are numeric and
# there is at least one character in the string.

print(s.isalnum())  # False # because there is space(' ') in between 2 words
print('hellowworld'.isalnum())    # True
# A string is alpha-numeric if all characters in the string are alpha-numeric and
# there is at least one character in the string.

print(s.isalpha())  # False
# A string is alphabetic if all characters in the string are alphabetic and
# there is at least one character in the string.

print(s.islower())      # True
# A string is lowercase if all cased characters in the string are lowercase and
# there is at least one cased character in the string

print(s.isspace())      # False
# A string is whitespace if all characters in the string are whitespace and
# there is at least one character in the string.

print(s.endswith('d'))      # True
print(s[-1] == 'd')         # True

print(s.split('o'))         # ['hell', 'w w', 'rld']
print(s.partition('o'))     # ('hell', 'o', 'w world')  # divide string at 1st occurrence
