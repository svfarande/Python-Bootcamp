'''

Basic Practice:
http://codingbat.com/python

More Mathematical (and Harder) Practice:
https://projecteuler.net/archives

List of Practice Problems:
http://www.codeabbey.com/index/task_list

A SubReddit Devoted to Daily Practice Problems:
https://www.reddit.com/r/dailyprogrammer

A very tricky website with very few hints and touch problems (Not for beginners but still interesting)
http://www.pythonchallenge.com/

'''

########### Section 3: Python Object and Data Structure Basics
########### 10. Introduction to Python Data Types

'''
int - Integers
Whole Numbers such as 10, 3, 2

float - Floating Point
Numbers with decimal point 10.2, 3.3, 4.2

str - String
Ordered sequence of characters "hello" , 'Shubham'

list - Lists
Ordered sequence of objects: [10,"hello", 200.3] 

dict - Dictionaries
Unordered Key:Value pairs:{"mykey":"value","name":"shubham"} 

tup - Tuples
Ordered immutable sequence of objects: (10,"hello"200.3)

set - Sets
Unordered collection of unique objects: {"a","b"}

bool - Booleans
Logical value indicating True or False
'''

########### 11. Python Numbers
#Numbers - FAQ
'''
Why doesn't 0.1+0.2-0.3 equal 0.0 ?
This has to do with floating point accuracy and computer's abilities to represent numbers in memory. For a full breakdown, check out: https://docs.python.org/2/tutorial/floatingpoint.html
'''

#Python uses Dynamic Typing


########### 15. Indexing and Slicing with Strings
#Strings
'''strings are ordered sequences it means we can using indexing and slicing to grab sub-sections of the string.
Indexing allows you to just "grab" a single character from the string'''

'''variable_name[start:stop:step]
stop - is upto but not including it'''

mystr = "Shubham"
print(mystr[:4])	# Shub
print(mystr[::2])	# Suhm
print(mystr[::-1])	# mahbuhS (string reversed)

'''in above examples mystr can be replaced by actual string'''
print("Shubham"[2])	# u	

########### 16. String Properties and Methods
'''Strings are immutable -> doesn't support item assignment based on index
Ex. mystr[3] = "B" #will give error. But same can be achieved as below'''

mystr = mystr[:3] + "B" + mystr[4:]
print(mystr)	# ShuBham

'''So let say you have to replace N number of index with particular character in string, then it can be done as -
mystr = mystr[:N] + "B" + mystr[N+1:]'''

letter = "S"
print(letter*5)	# SSSSS

'''split()'''
mystr = "Shubham Farande"
print(mystr.split())	# ['Shubham', 'Farande']
print(mystr.split("a"))	# ['Shubh', 'm F', 'r', 'nde']
print(len(mystr))		# 7

########### 18. Print Formatting with Strings
#.format()

print("{0} {1}".format("shubham", "farande"))	# shubham farande
print("{s} {f}".format(s="shubham",f="farande"))# shubham farande

'''either indexing or keyword will work , both wont work
print("{0} {1}".format(s="shubham",f="farande"))# will error out'''

'''Also positional argument follows keyword argument
print("{0} {1}".format(s="shubham",f="farande","shubham","farande"))	#error'''

print("{0} {1}".format("shubham","farande",s="shubham",f="farande",))	# shubham farande (last extra comma will not give error)

# float formatting

'''syntax - 
print("Your text {value:width.precisionf}".format(value=variable_name))'''

print("Answer is {s:}".format(s=100/777))       # Answer is 0.1287001287001287
print("Answer is {s:.2}".format(s=100/777))     # Answer is 0.13
print("Answer is {s:10}".format(s=100/777))     # Answer is 0.1287001287001287
print("Answer is {s:10.0}".format(s=100/777))   # Answer is        0.1
print("Answer is {s:10.1}".format(s=100/777))   # Answer is        0.1
print("Answer is {s:10.2}".format(s=100/777))   # Answer is       0.13
print("Answer is {s:10.3}".format(s=100/777))   # Answer is      0.129

# f strings or formatted strings (new feature in Python 3.6)

'''syntax - 
print(f"My name is {variable_name}")'''

print(f"My name is {mystr}. Hi {mystr[0]}{mystr[8]}")	# My name is Shubham Farande. Hi SF

########### 20. Lists in Python

'''ordered sequences that can hold a variety of object types
support indexing and slicing
can be nested
Similar to strings it supports indexing, slicing, concatenations
Except it can mutate - support index assignment
list.pop() returns and removes last element from list by default its -1
list.sort() sort the list in place without returning anything
sort() & reverse() doesn't work in different data types such as int and string'''

########### 21. Lists - FAQ

''' How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?
You would just add another set of brackets for indexing the nested list, for example: my_list[2][1]'''

mylist = ['Shubham', 'Vasant', 'Farande', 6, 12, 1996, 75.9]
print(mylist)  # ['Shubham', 'Vasant', 'Farande', 6, 12, 1996, 75.9]
nlist = ['3', '4.5', '1', '-36']
print(nlist)  # ['3', '4.5', '1', '-36']

# sorted() returns new list and don't change original list & sort() do in-place sorting by changing original list
print(sorted(nlist)) # ['-36', '1', '3', '4.5']
print(nlist.sort())  # None

print(nlist)  # ['-36', '1', '3', '4.5']
nlist = ['3', '4.5', '1', ['67', 'Shubham', '7.6'], '-36']
print(nlist)  # ['3', '4.5', '1', ['67', 'Shubham', '7.6'], '-36']
print(nlist[::-1]) # ['-36', ['67', 'Shubham', '7.6'], '1', '4.5', '3']
newlist = mylist + nlist
newlist[1]="V."
print(newlist)  # ['Shubham', 'V.', 'Farande', 6, 12, 1996, 75.9, '3', '4.5', '1', ['67', 'Shubham', '7.6'], '-36']


########### 22. Dictionaries in Python

'''unordered mutable mappings hence they cannot be sorted
key-value pairing instead of indexing
{'key1':'value1','key2':'value2'}
ordereddict object are dictionary in order
An OrderedDict is a dictionary subclass that remembers the order that keys were first inserted. The only difference between dict() and OrderedDict() is that:
OrderedDict preserves the order in which the keys are inserted. A regular dict doesn’t track the insertion order, and iterating it gives the values in an arbitrary order. By contrast, the order the items are inserted is remembered by OrderedDict.
'''

mydict = {"key": 'value', 'Shubham': "Farande"}
print(mydict)   # {'key': 'value', 'Shubham': 'Farande'}
print(mydict['Shubham'])    # Farande

cmpxdict = {'keys': 'values', 'list': [34, 'Shubham', 4.5], 'dict': {5.5: 'five point five', 'five': 5}}
print(cmpxdict)     #{'keys': 'values', 'list': [34, 'Shubham', 4.5], 'dict': {5.5: 'five point five', 'five': 5}}

print(cmpxdict['list'][1][::-1].upper())    # MAHBUHS
print(cmpxdict['dict'][5.5])    # five point five

cmpxdict['list'][1] = "Hi"
cmpxdict['dict'][6] = 'Six'
cmpxdict['Six'] = 6
print(cmpxdict)     # {'keys': 'values', 'list': [34, 'Hi', 4.5], 'dict': {5.5: 'five point five', 'five': 5, 6: 'Six'}, 'Six': 6}

# newdict = mydict + cmpxdict # error - unsupported operand type(s) for +: 'dict' and 'dict'

print(cmpxdict.keys())  # dict_keys(['keys', 'list', 'dict', 'Six'])
print(cmpxdict.values())    # dict_values(['values', [34, 'Hi', 4.5], {5.5: 'five point five', 'five': 5, 6: 'Six'}, 6])
print(cmpxdict.items())     # dict_items([('keys', 'values'), ('list', [34, 'Hi', 4.5]), ('dict', {5.5: 'five point five', 'five': 5, 6: 'Six'}), ('Six', 6)])

# Note below overwrite of value when same key is used
dictionary = {"key1": "value2", "key2": "value2", "key1": "value1"}
print(dictionary)   # {'key1': 'value1', 'key2': 'value2'}

########### 24. Tuples with Python

'''similar to list but immutable
Once an element is inside a tuple, it can not be reassigned'''

t1 = ('1', "Shubham", 1, 4.5, 1)
print(t1)  # ('1', 'Shubham', 1, 4.5, 1)

print(t1[::-1])  # (1, 4.5, 1, 'Shubham', '1')
print(t1.count(1) + t1.index("1") + t1.index(1))  # 2+0+2=4

t2 = (2, "Farande", 9.0, {'key1': 'value1', 'key2': 'value2'}, ['5', '4.5', 'hi'])
t = t1 + t2
print(t)  # ('1', 'Shubham', 1, 4.5, 1, 2, 'Farande', 9.0)

# t1[1] = "Shubham"  # error - 'tuple' object does not support item assignment

########### 25. Sets in Python

'''unordered collections of unique elements'''

# myset = set(2,1,3,3,2,1)       # set expected at most 1 argument which is iterable, got 6
myset = set()
myset.add(5)
myset = {2, 3, 1, 3, 't'}
myset.add('t')
print(myset)  # {1, 2, 3, 't'}

lists = [2, 2, 2, 2, 1, 1, 1, 4, 3, 4, 3]
myset = set(lists)
print(myset)  # {1, 2, 3, 4}

lists = [2, 1, 1, 4, 3, 4, 78, 90, 98, 5]
myset = set(lists)
print(myset)  # {1, 2, 3, 4, 98, 5, 78, 90}

print(set('Mmississippi'))  # {'m', 'i', 'M', 's', 'p'}

########### 26. Booleans in Python

true = True
print(str(true) + " - " + str(type(true)))      # True - <class 'bool'>

false = False
print(str(false) + " - " + str(type(false)))      # False - <class 'bool'>

print(1 > 2)    # False
print(1 == 1)   # True

'''a variable declared must be defined immediately at least with None
none #error - name 'none' is not defined'''
none = None
print(str(none) + " - " + str(type(none)))      # None - <class 'NoneType'>

########### 27. I/O with Basic Files in Python

'''Contents of text.txt before performing file operations. text.txt - 
Hello There
This is 1st line.
This is 2nd line.
This is 3rd line.
'''

myfile = open('text.txt')  # same as open('text.txt', mode='r') or same as open('text.txt', 'r')
print(myfile.read())  # outputs all the contents of file
print(myfile.read())  # will print blank line because cursor was placed at end because of previous print statement
print(myfile.seek(11))  # will output index given in seek() and place cursor to that index of file (note at 11 index there is '\n' of 1st line)
print(myfile.read())  # outputs all the contents of file starting from the index in seek()
myfile.seek(0)
print(myfile.readlines())  # outputs each line in list format
myfile.close()  # close the file, if you don't do this and try to delete the file it will give error python is using it

#File location
'''For Windows - myfile = open("C:\\Users\\Username\\Folder\\filename.txt")
For MacOS or Linux - myfile = open("/Users/Username/Folder/filename.txt")
For Windows extra \ is required because if given single \ it might treat it as escape sequence'''

# using below with statement you need not to close the file manually, it will close immediately after block ends

with open('C:\\Users\\A711929\\OneDrive - Atos\\Documents\\Study MAterial\\Python\\PyCharm Projects\\PyBootCamp\\text.txt', mode='r') as myfile:  # by default mode is 'r'
    contents = myfile.read()
    print(contents)

# also remember with specific mode you can only use functions for that mode for ex. with mode='w' you can't use read()

'''
'r' is read only
'w' is write only (will always overwrite or create new file)
'a' is append only (if file don't exists it will create new file and append content to that file)
'r+' is reading and writing
'w+' is writing and reading
> Opening a file with 'w' or 'w+' truncates the original, meaning that anything that was in the original file is deleted!'''

with open('text.txt', mode='w+') as myfile:
    print(myfile.read())  # contents of text.txt are now vanished as mode='w+'

with open('text.txt', mode='w') as myfile:
    myfile.write("Shubham")     # Shubham is in now in text.txt

with open('text.txt', mode='a') as myfile:
    myfile.write("\n"+contents)
	
for line in open('text.txt'):	# printing each line without read()
	print(line)

'''Contents of text.txt before performing file operations. text.txt - 
Shubham
Hello There
This is 1st line.
This is 2nd line.
This is 3rd line.
'''

########### 28 Resources for More Basic Practice
'''Basic Practice: http://codingbat.com/python
More Mathematical (and Harder) Practice: https://projecteuler.net/archives
List of Practice Problems: http://www.codeabbey.com/index/task_list
A SubReddit Devoted to Daily Practice Problems: https://www.reddit.com/r/dailyprogrammer
A very tricky website with very few hints and touch problems (Not for beginners but still interesting): http://www.pythonchallenge.com/'''

########### 29. Python Objects and Data Structures Assessment Test
'''
Answer the following questions
Write a brief description of all the following Object Types and Data Structures we've learned about:
Numbers: Float(number with decimal point) & Integers(whole numbers)
Strings: these are immutable ordered characters in sequence ; indexing and slicing works
Lists: ordered sequence of objects ; these are mutable ; can be nested; indexing and slicing works; support multiple data type in same list
Tuples: ordered sequence of objects ; these are similar to list but immutable ; can be nested; indexing and slicing works; support multiple data type in same tuple
Dictionaries: unordered key-value pairs ; can be nested; mutable; indexing and slicing don't work; support multiple data type in same dictionary

Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
-> (10*10*10/10 + 0.5**2) + (10*10*10/10 + 0.5**2) - (10*10*10/10 + 0.5**2)
Answer these 3 questions without typing code. Then type code to check your answer.
What is the value of the expression 4 * (6 + 5) -> 44
What is the value of the expression 4 * 6 + 5  -> 29
What is the value of the expression 4 + 6 * 5 -> 34
What is the type of the result of the expression 3 + 1.5 + 4? -> float
What would you use to find a number’s square root, as well as its square?
Square root-> number**0.5 Square-> number**2

Strings
Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello' 
Print out 'e' using indexing -> print(s[1])
Reverse the string using slicing -> print(s[::-1])
Given the string hello, give two methods of producing the letter 'o' using indexing.
Print out the 'o' -> print(s[4]); print(s[-1])

Lists
Build this list [0,0,0] two separate ways.
Method 1 -> myzerolist = [0]*3
Method 2 -> myzerolist = [0,0,0]
Reassign 'hello' in this nested list to say 'goodbye' instead: list3 = [1,2,[3,4,'hello']]
-> list3[-1][-1]='goodbye'
Sort the list below: list4 = [5,3,4,6,1]
-> list4.sort()		# changes the original list4
-> sorted(list4)	# returns new list maintaining list4 as it was

Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries: 
d = {'simple_key':'hello'} -> d['simple_key']
d = {'k1':{'k2':'hello'}} -> d['k1']['k2']
d = {'k1':[{'nest_key':['this is deep',['hello']]}]} -> d['k1'][0]['nest_key'][1][0]
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]} -> 
Can you sort a dictionary? Why or why not? -> no, because these are mappings of key-value pairs and sequence

Sets
What is unique about a set? -> that it holds unique elements only
Use a set to find the unique values of the list below: list5 = [1,2,2,33,4,4,11,22,3,3,2]
-> set5 = set(list5)

Tuples
What is the major difference between tuples and lists? -> tuples are immutable & lists are mutable
How do you create a tuple? -> mytuple = ('Shubham' , '6')

Booleans
What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)
2 > 3 -> False
3 <= 2 -> False
3 == 2.0 -> False
3.0 == 3 -> True
4**0.5 != 2 -> False
Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
# True or False? -> False
l_one[2][0] >= l_two[2]['k1']
'''

########### Section 4: Python Comparison Operators
########### 32. Chaining Comparison Operators in Python with Logical Operators

print(1 < 2 < 3)  # True
print(1 < 2 and 2 < 3)  # True
print(1 < 2 > 3)  # False

print(3.0 == 3)  # True

# logical operator - and , or , not / !

print(not(1 == 1))  # False

########### Section 5: Python Statements
########### 33. If Elif and Else Statements in Python

loc = "Bank"

if loc == "Auto Shop":
    print("Cars")
elif loc == "Bank":
    print("Money")		#prints this
elif loc == "Gym":
    print("Fitness")
else:
    print("Don't know")
	
########### 35. For Loops in Python

for element in loc:
    print(element)      # prints "Bank" each letter on new line

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for (a, a) in mylist:  # (a,b) or a,b
    print(a + a)  # will print 2nd element + 2nd element

mydict = {'k1': 1, 'k2': 2, 'k3': 3}
print(mydict.items())   # dict_items([('k1', 1), ('k2', 2), ('k3', 3)])
print(mydict.keys())    # dict_keys(['k1', 'k2', 'k3'])
print(mydict.values())  # dict_values([1, 2, 3])
for i in mydict:
    print("{key} -> {value}".format(key=i, value=mydict[i]))
for k, v in mydict.items():
    print(k + " : " + str(v))   # note v is type casted to str
for k in mydict.keys():
    print(k)
for v in mydict.values():
    print(v)
# please note as this is small dictionary you will see output in order but its not guaranteed

########### 36. While Loops in Python

x = 0
while x <= 3:
    print(f'x={x}')     # prints x = 0 to 3
    x = x + 1
else:
    print(f'in else x={x}')     # when x = 4 it goes to else and print "in else x=4"

# break = Ends loop ; continue = goes to next condition/iteration ; pass = Does nothing at all

x = [1, 2, 3]
for i in x:
    # comment    #if for loop is kept empty it will give error in such case pass is useful
    pass  # it means do nothing just pass

myname = "Shubham"

for ll in myname:
    if ll == "h":
        continue
    print(ll)       # print S u b a m each letter on new line

for ll in myname:
    if ll == "h":
        break
    print(ll)       # print S and loop terminates

x = 0
while x <= 5:
    print(f'x={x}') # prints x = 0 to 2
    if x == 2:
        break
    x = x + 1
print("final x = {z}".format(z=x))  # final x = 2

########### 37. Useful Operators in Python

print(list(range(0, 12, 2)))  # [0, 2, 4, 6, 8, 10]
# note start is by default 0 only when stop is given ex. range(10) will go from 0 to 9
# also step is optional and by default its 1
# in actual stop is skipped and range acts from start to stop - 1
for n in range(0, 12, 2):  # range(start,stop,step)
    print(n)  # prints even no. from 0 to 11

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

########## 38. List Comprehensions in Python

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

########## 39. Python Statements Test Overview
'''
Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
Code:
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0] == 's':
        print(word)
Output:
start
s
sentence
		
Use range() to print all the even numbers from 0 to 10.
Code:
for op in range(0,11):
    if op%2 == 0:
        print(op)
Optimized Code:
for op in range(0,11,2):
        print(op)

Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
Code:
d3 = [num for num in range(1, 51) if num % 3 == 0]

Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
Code:
st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
for word in words:
    if len(word)%2 == 0:
        print(word+" - even - "+str(len(word)))
Output:
word - even - 4
in - even - 2
this - even - 4
sentence - even - 8
that - even - 4
an - even - 2
even - even - 4
number - even - 6
of - even - 2

Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".		
Code:
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz - {num}")
    elif num % 5 == 0:
        print(f"Buzz - {num}")
    elif num % 3 == 0:
        print(f"Fizz - {num}")
Output:
Fizz - 3
Buzz - 5
Fizz - 6
Fizz - 9
Buzz - 10
Fizz - 12
FizzBuzz - 15
Fizz - 18
Buzz - 20
Fizz - 21
Fizz - 24
Buzz - 25
Fizz - 27
FizzBuzz - 30
Fizz - 33
Buzz - 35
Fizz - 36
Fizz - 39
Buzz - 40
Fizz - 42
FizzBuzz - 45
Fizz - 48
Buzz - 50
Fizz - 51
Fizz - 54
Buzz - 55
Fizz - 57
FizzBuzz - 60
Fizz - 63
Buzz - 65
Fizz - 66
Fizz - 69
Buzz - 70
Fizz - 72
FizzBuzz - 75
Fizz - 78
Buzz - 80
Fizz - 81
Fizz - 84
Buzz - 85
Fizz - 87
FizzBuzz - 90
Fizz - 93
Buzz - 95
Fizz - 96
Fizz - 99
Buzz - 100

Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
Code:
f = [word[0] for word in st.split()]
'''

########### Section 6: Methods and Functions

########### 42. Functions in Python

#Functions allow us to create block of code that can be easily executed many times without needing to constantly rewrite the entire block of code

#"def" keyword instructs python that after this keyword there is definition of a function

#Funtion use snake_case in their definition of name while class use camelCase

#typical def of function - 
'''

def name_of_funct():
	###
	Docstring explains function
	###
	.	C
	.	O
	.	D
	.	E
	
	return <variable name>
'''

def hi_name(name="shubham"):
    return "Hi " + name


print(hi_name("Shubham"))  # Hi Shubham
print(hi_name())  # Hi shubham


def pig_latin(word):
    if word[0] in "aeiouAEIOU":
        word = word + "ay"
    else:
        word = word[1:] + word[0] + "ay"
    return word


print(pig_latin("apple"))  # appleay
print(pig_latin("word"))  # ordway
print(pig_latin("Apple"))  # Appleay
print(pig_latin("Word"))  # ordWay

########### 46. Tuple Unpacking in Python

def max_quantity(fruits_quantity):
    fruit = ""
    quantity = 0;

    for f, q in fruits_quantity:
        if q > quantity:
            fruit = f;
            quantity = q;

    return (fruit, quantity)


print(max_quantity([("apple", 4), ("mango", 5), ("orange", 2)]))  # ('mango', 5)
fruit, quantity = max_quantity([("apple", 4), ("mango", 5), ("orange", 2)])
print(f"{fruit} - {quantity}")  # mango - 5

t = ("Python", 3, "Education")    # tuple packing
(language, version, profile) = t    # tuple unpacking
print(language) # Python
print(version)  # 3
print(profile)  # Education

########### 47. Interactions between Python Functions.

from random import shuffle


def shuffle_(mylist):
    shuffle(mylist)
    return mylist


def guess():
    no = ""
    while no not in ["0", "1", "2"]:
        no = input("Pick a guess 0 , 1 or 2 : ")
    return int(no)


def check(mylist, place):
    if mylist[place] == 'O':
        print("Correct Guess !")
        print(mylist)
    else:
        print("Wrong Guess !")
        print(mylist)


mylist = [' ', 'O', ' ']
mylist = shuffle_(mylist)
place = guess()
check(mylist, place)

##Output : 
Pick a guess 0 , 1 or 2 : 
Pick a guess 0 , 1 or 2 : 3
Pick a guess 0 , 1 or 2 : a
Pick a guess 0 , 1 or 2 : 0
Correct Guess !
['O', ' ', ' ']


########### 49. *args and **kwargs in Python

#args -> Tuples
#kwargs -> Dictionary

def add(*args):
    print(args)  # prints tuple of arguments ex. (5,5)
    print(*args)  # prints arguments separated by space ex. 5 5
    return sum(args)


print(add(5, 5))  # 10
print(add(5, 5, 5))  # 15


def myfunc(**kwargs):
    print(kwargs)  # {'a': 'A', 'b': 'B', 'c': 'C'}
    # print(**kwargs) gives Error
    print(kwargs['b'])  # B


myfunc(a="A", b="B", c="C")


# note args and kwargs are varibales and can have any name as variable


def myfunc(*args, **kwargs):
    print(args)  # ('shubham', 'farande')
    print(kwargs)  # {'firstname': 'shubham', 'lastname': 'farande'}
    print(f"My name is {args[0]} {kwargs['lastname']}")     # My name is shubham farande


myfunc("shubham", "farande", firstname="shubham", lastname="farande")

# note keyword argument has to come after arguments

def myfunc(m, *args, a, **kwargs):
    print(args)  # ('shubham', 'farande')
    print(kwargs)  # {'firstname': 'shubham', 'lastname': 'farande'}
    print(f"{m} name {a} {args[0]} {kwargs['lastname']}")  # My name - shubham farande


myfunc("My", "shubham", "farande", a="-", firstname="shubham", lastname="farande")

########### 50. Function Practice Exercises
'''

WARMUP SECTION:
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
Code:
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:           #return min(a,b)
            return a
        else:
            return b
    else:
        if a > b:           #return max(a,b)
            return a
        else:
            return b

ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def animal_crackers(text):
    words = text.split(" ")             #words = text.lower().split()
    if words[0][0] == words[1][0]:      #return words[0][0] == words[1][0]
        return True
    else:
        return False
        
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
    if a+b == 20 or a == 20 or b == 20:     #return (a+b) == 20 or a == 20 or b == 20
        return True
    else:
        return False
        
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶

def old_macdonald(name):
    op = name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return op   # return name[:3].capitalize() + name[3:].capitalize()

MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    words = text.split()
    reverse_text = " ".join(words[::-1])
    return reverse_text
    
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):    #return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)
    if (89 < n < 111) or (189 < n < 211):
        return True
    else:
        return False
        

FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:       # nums[i:i+2] == [3,3]
            return True
    return False

PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(text):
    three = ''
    for i in text:
        three = three + i + i + i       # three += i*3
    return three
    
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a, b, c):
    if a + b + c < 22:      # sum([a,b,c])
        return a + b + c
    else:
        if a == 11 or b == 11 or c == 11:       # 11 in [a,b,c]
            if (a + b + c) - 10 < 22:
                return (a + b + c) - 10
            else:
                return 'BUST'
        else:
            return 'BUST'

SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    f = 0
    for i in arr:
        if i == 6 or f == 1:
            f = 1
            if i == 9:
                f = 0
        else:
            total = total + i
    return total

SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    f0 = 0
    s0 = 0
    for i in nums:
        if i == 0 and f0 == 0:
            f0 = 1
            continue
        if i == 0 and f0 == 1 and s0 == 0:
            s0 = 1
            continue
        if i == 7 and f0 == 1 and s0 == 1:
            return True
    return False

def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num = code[0]:
            code.pop(0)
    return len(code) == 1
 
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

import math


def count_primes(n):
    nums = [True for i in range(n+1)]
    nums[0] = False
    nums[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if nums[i]:
            j = 2
            while i * j <= n:
                nums[i * j] = False
                j = j + 1

    count = 0
    for i in range(0, len(nums)):
        if nums[i]:
            count = count + 1

    return count

GIVEN IN LECTURES - 

def count_primes(n):
    if n < 2:
        return 0

    primes = [2]
    x = 3

    for i in range(x, n + 1, 2):
        for y in primes:
            if i % y == 0:
                break
        else:
            primes.append(i)

    print(primes)
    return len(primes)

PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter


def print_big(letter):
    p5_5 = {'a': ["  *  ", " * * ", "*****", "*   *", "*   *"],
            'b': ["**** ", "*   *", "**** ", "*   *", "**** "],
            'c': ["*****", "*    ", "*    ", "*    ", "*****"],
            'd': ["**** ", "*   *", "*   *", "*   *", "**** "],
            'e': ["*****", "*    ", "*****", "*    ", "*****"]}
    for i in range(0, 5):
        print(p5_5[letter][i])


'''

########### 55. Lambda Expressions, Map, and Filter Functions

'''
 map() function is used to apply a function on all the elements of specified iterable and return map object. Python map object is an iterator, so we can iterate over its elements. We can also convert map object to sequence objects such as list, tuple etc. using their factory functions.
 syntax - map(function, sequence[,sequence, ....]) 
 
 The filter() method constructs an iterator from elements of an iterable for which a function returns true. In simple words, filter() method filters the given iterable with the help of a function that tests each element in the iterable to be true or not. 
 syntax - filter(function or None, sequence)
 if function is None then it will return iterable from sequence which returns only true elements
 
 A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. 
 
'''

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



########### 56. Nested Statements and Scope
'''
LEGB Rule:
L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that
function.
E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from
inner to outer.
G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...
'''

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

# global <variable_name> will allow you to use global variable

########### 57. Methods and Functions Homework Overview


'''
Write a function that computes the volume of a sphere given its radius.

import math
def vol(r):
    return (4 / 3) * math.pi * r * r * r
print(vol(2))

Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    return low <= num <= high
print(ran_check(7, 6, 7))

Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            u = u + 1
        if i.islower():
            l = l + 1
    print(f'No. of Upper case characters :  {u} \nNo. of Lower case characters :  {l}')
up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list(set(lst))
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))

Write a Python function to multiply all the numbers in a list.

def multiply(lst):
    pro = 1
    for i in lst:
        pro = pro * i
    return pro
print(multiply([1, 2, 0, -4]))

Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    s = s.replace(" ", "")
    return s == s[::-1]
print(palindrome('nurses run'))

Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

def is_panagram(str1):
    return "".join(sorted(set(str1.replace(" ", "").lower()))) == "abcdefghijklmnopqrstuvwxyz"
print(is_panagram("The quick brown fox jumps over the lazzy dog"))

'''

########### Section 7: Milestone Project - 1 (TIC TAC TOE)

########### Section 8: Object Oriented Programming
########### 68. Object Oriented Programming - Introduction

class NameOfClass():

    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2
        
    def some_method(self):
        #perform some action
        print(self.param1)

########### 69. Object Oriented Programming - Attributes, Methods and Class Keyword

class Dog:
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, num):
        print(f"Dog {num} - Bhow! My name is {self.name} and I'm a {self.breed}. I belong to {self.species}\n")


mydog1 = Dog("Lab", "Kalu")
mydog2 = Dog("Pug", "Balu")

print(mydog1.name + "(" + mydog1.breed + ") - ")    #Kalu(Lab) -
mydog1.bark(1)  #Dog 1 - Bhow! My name is Kalu and I'm a Lab. I belong to mammal

print(mydog2.name + "(" + mydog2.breed + ") - ")    #Balu(Pug) -
mydog2.bark(2)  #Dog 2 - Bhow! My name is Balu and I'm a Pug. I belong to mammal


########### 71. Object Oriented Programming - Inheritance -

def what_i_do():
    print("I eat & sleep")


class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I'm animal")


class Dog(Animal):
    def __init__(self):
        print("Dog created")

    def who_am_i(self):
        print("I'm Dog")


myanimal = Animal()
myanimal.who_am_i()
what_i_do()

mydog = Dog()
mydog.who_am_i()
what_i_do()

########### 71. Object Oriented Programming - Polymorphism -

class Animal:
    # is abstract class is that class which we never expect to be instantiated as it has 1 or more abstract method
    # the child class which inherits this parent class should implement abstract method declared in parent class
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass should implement this abstract method")


class Dog(Animal):
    def speak(self):
        print(self.name + " says Bhow!")


class Cat(Animal):
    def speak(self):
        print(self.name + " says Meow!")


def pet_speak(obj):
    obj.speak()     # obj demonstrates Polymorphism using speak() function


kutta = Dog("Kuttu")
billi = Cat("Billu")

for pet in [kutta, billi]:
    print(type(pet))
    pet_speak(pet)

########### 72. Object Oriented Programming - Special (Magic/Dunder) Methods

class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # overriding inbuilt str method
        return f"{self.title} by {self.author}"

    def __len__(self):  # overriding inbuilt len method
        return self.pages

    def __del__(self):  # overriding inbuilt del method
        print("Book - " + self.title + " deleted")


b = Book("P for Python", "Shubham", 50)

print(b)
print(str(b))
print(len(b))
del b


########### 73. Object Oriented Programming - Homework
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        print(pow(pow(self.coor2[1] - self.coor1[1], 2) + pow(self.coor2[0] - self.coor1[0], 2), 0.5))
        # tuple-unpacking
        # x1,y1 = self.coor1
        # x2,y2 = self.coor2
        # print(((y2-y1)**2+(x2-x1)**2)**0.5)

    def slope(self):
        print((self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]))
        # tuple-unpacking
        # x1,y1 = self.coor1
        # x2,y2 = self.coor2
        # print((y2-y1)/(x2-x1))


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
li.distance()
li.slope()


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.raidus = radius

    def volume(self):
        print((22 / 7) * self.raidus * self.raidus * self.height)

    def surface(self):
        print((2 * (22 / 7) * self.raidus * self.height) + (2 * (22 / 7) * self.raidus * self.raidus))


c = Cylinder(2, 3)
c.volume()
c.surface()


###########  75. Object Oriented Programming - Challenge Overview
class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"{amount} Money deposited. Now balance is : {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"{amount} Money withdraw. Now balance is : {self.balance}")
        else:
            print(f"You don't have enough balance to withdraw {amount} money. Your balance is : {self.balance}")

    def __str__(self):
        return f"Account Owner : {self.owner}\nAccount Balance : {self.balance}"


acct1 = Account("Shubham", 1000)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(500)
acct1.withdraw(750)
acct1.withdraw(5000)

########### Section 9: Modules and Packages
########### 77. Pip Install and PyPi

'''

PIP is python package manager and is recursive acronym for PIP Installs Packages
PyPi stands for Python Package Index and is a repository for open-source 3rd party packages

To install package type -
pip install <package name>

> pip install colorama
Collecting colorama
  Downloading colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Installing collected packages: colorama
Successfully installed colorama-0.4.4

>python
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from colorama import init
>>> init()
>>> from colorama import Fore
>>> print(Fore.RED+"red text")
red text    #red colour text
>>> print(Fore.GREEN+"green text")
green text    #green color text
>>>exit()

'''

###########  78. Modules and Packages
#Modules - are just .py scripts that you can call in another .py script
#Packages - are collection of modules

#Note - Modules are interpreted at time of import. Hence, if a funtion is being called in module itself then it will be called at import also. To avoid this go through next lecture

#modules and packages.py - 
from same_dir import begin  # Start\nEnd
from MyPackage.main_script import main_function
from MyPackage.MySubPackage.sub_script import sub_function

sub_function()  # sub script function in MyPackage/MySubPackage/sub_script.py
main_function()  # main script function in MyPackage/main_script.py
begin()  # start

#same_dir.py - (it is located in same directory as modules and packages.py)
def begin():
    print("Start")


begin()
print("End")

#main_script.py -
def main_function():
    print("main script function in MyPackage/main_script.py")

#sub_script.py -
def sub_function():
    print("sub script function in MyPackage/MySubPackage/sub_script.py")
    
###########  79. __name__ and "__main__"

#Every code with intendation level 0 gets run in your script as there is no main() function like other programming languages

#When a code is being interpreted directly a inbuilt variable __name__ is given value as __main__ This can be used to check if program / script is imported or interpreted directly by using - if __name__ == "__main__":

#Replace same_dir.py - (it is located in same directory as modules and packages.py) in previous lecture files by below code -
def begin():
    print("Start")


def begin1():
    print("Start1")

def end1():
    print("End1")

begin()

if __name__ == "__main__":
    begin1()

end1()
print("End")

#Now when same_dir.py is imported in #modules and packages.py begin1() won't be called while importing (unless its imported explicitly and then called). On the other hand if same_dir.py is interpreted directly __name__ == "__main__" will be true and begin1() will be called.

########### Section 10: Errors and Exceptions Handling
########### 80. Errors and Exception Handling

while True:
    try:  # any code which is likely to give error is inserted in try
        number1 = float(input("Enter Dividend (number1) for division : "))
        number2 = float(input("Enter Divisor (number2) for division : "))
        result = number1 / number2
    except ValueError:  # it will run when ValueError occurs in try block
        print("Looks like you didn't enter number. Try again.")
        continue
    except ZeroDivisionError:  # it will run ZeroDivisionError occurs in try block
        print("Looks like your divisor is 0. Try again.")
        continue
    except:  # it will run when error occur but doesn't belong to above expected errors
        print("Something is wrong. Try again.")
        continue
    else:  # It will only run when either of the expect don't run
        print("Division is = " + str(result))
        break
    finally:  # Whatever may be the case this will run for sure
        print("Great Learning !!")

########### 81. Errors and Exceptions Homework
'''
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    print(i**2)

Answer 1
for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print("I can't square - "+i)

Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'

x = 5
y = 0

z = x/y

Answer 2
x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("Division by 0 don't exists")
finally:
    print("All Done!")

Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

Answer 3
def ask():
    while True:
        try:
            a = int(input("Input an integer - "))
        except ValueError:
            print("An error occurred! Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is: {a ** 2}")
            break


ask()
'''

########### 84. Pylint Overview
#Pylint is a source-code, bug and quality checker for the Python programming language.
#in windows cmd type below to install pylint - 
#pip install pylint
#pylint <filename>.py -r y in cmd will give you detail report along with code rating
#in the newest version of PyLint you need to add -r y (report yes) at the end of the command, so the full command should be: pylint myexample.py -r y

########### 85. Running tests with the Unittest Library
#The unittest is unit testing framework by which individual units of source code are put under various tests to determine whether they are fit for use.

#unittest_cap.py:
def MyFunc(text):
    return text.title()

#unittest_test_cap.py:
import unittest
import unittest_cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = unittest_cap.MyFunc(text)
        self.assertEqual('Python', result)  # self.assertEqual(<expected>, <actual>)

    def test_multi_word(self):
        text = 'many python words'
        result = unittest_cap.MyFunc(text)
        self.assertEqual('Many Python Words', result)   # self.assertEqual(<expected>, <actual>)


if __name__ == '__main__':
    unittest.main()

########### Section 11: Milestone Project - 2

########### Section 12: Python Decorators

########### 98. Decorators with Python Overview

'''
A programming language is said to have First-class functions when functions in that language are treated like any other variable.

First Class functions in Python

First class objects in a language are handled uniformly throughout. They may be stored in data structures, passed as arguments, or used in control structures. A programming language is said to support first-class functions if it treats functions as first-class objects. Python supports the concept of First Class functions.

Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
'''

print("\n-------------------- Function Assignment and Deletion  --------------------")


def heloo():
    return "Hi"


print("heloo() defined - ")
print(type(heloo))  # <class 'function'>
print(heloo)    # <function heloo at 0x00ED7FA0>
print(heloo())  # Hi

greet = heloo

print("\ngreet = heloo -")
print(type(greet))  # <class 'function'>
print(greet)    # <function heloo at 0x00ED7FA0>
print(greet())  # Hi

del heloo

# print(type(heloo)) # NameError: name 'heloo' is not defined
# print(heloo)  # NameError: name 'heloo' is not defined
# print(heloo())    # NameError: name 'heloo' is not defined

print("\ndel heloo -")
print(type(greet))  # <class 'function'>
print(greet)    # <function heloo at 0x00ED7FA0>
print(greet())  # Hi

print("\n-------------------- Function Within Function --------------------")


def hello(name):
    print(f"\nhello(\"{name}\") - ")

    def greetings():
        return "\t greetings()"

    def welcome():
        print("\t welcome()")

    print(greetings())
    welcome()

    if name == "Shubham":
        return greetings
    elif name == "Python":
        return welcome

    print("hello() ended")


print(hello("Shubham"))
'''
hello("Shubham") - 
	 greetings()
	 welcome()
<function hello.<locals>.greetings at 0x00EE7148>
'''

# greetings()   # NameError: name 'greetings' is not defined
# welcome() # NameError: name 'welcome' is not defined

print(hello("Python"))
'''
hello("Python") - 
	 greetings()
	 welcome()
<function hello.<locals>.welcome at 0x00EE7100>
'''

print(hello("Foo"))
'''
hello("Foo") - 
	 greetings()
	 welcome()
hello() ended
None
'''

print("\n-------------------- Function Return & Assignment --------------------")

outside_greetings = hello("Shubham")
print(outside_greetings)
print(outside_greetings())
'''
hello("Shubham") - 
	 greetings()
	 welcome()
<function hello.<locals>.greetings at 0x00EE7148>
	 greetings()
'''

outside_welcome = hello("Python")
print(outside_welcome)
print(outside_welcome())
'''
hello("Python") - 
	 greetings()
	 welcome()
<function hello.<locals>.welcome at 0x00EE70B8>
	 welcome()
None
'''

print("\n-------------------- Function Passing --------------------")


def hellow():
    return "Hellow there"


def hi(my_func):
    print("Hi there")
    print(my_func())


hi(hellow)  # Note - its not hi(hellow())
'''
Hi there
Hellow there
'''
##################################################################################
def new_decorator(orignal_func):
    def wrap():
        print("Code before orignal_func()")

        orignal_func()

        print("Code after orignal_func()")

    return wrap


@new_decorator
def i_need_decoration():
    print("Main Code")


i_need_decoration()

'''
Either add @<decorator_name> (@new_decorator) syntax before function definition 
which needs decoration and then call that function as shown above.
--OR--
pass the function which needs decoration (i_need_decoration) to decorator function 
(new_decorator(i_need_decoration)) and get it assigned to some variable and then call the 
decorated function using that variable as shown below.
'''

# remember to only pass function pointer and not call the actual function
# decorated = new_decorator(i_need_decoration)
# decorated()

# ------------------------- If function takes & return's something -----------------------------


def decoration(original_func):
    def inner(num):
        print('Code Before Function')

        squared = original_func(num)

        print('Code After Function')
        return squared

    return inner


@decoration
def i_need_decoration(num):
    print(f'This function calculates square')
    return num * num


print(i_need_decoration(5))

'''
Code Before Function
This function calculates square
Code After Function
25
'''

# ----------------------- Generic version decorator using *args & **kwargs --------------------------


def decoration(original_func):
    def inner(*args, **kwargs):
        print('Code Before Function')
        
        squared = original_func(*args, **kwargs)
        
        print('Code After Function')
        return squared

    return inner


@decoration
def i_need_decoration1(num):
    print(f'This function calculates square')
    return num * num


@decoration     # using same decoration as above function
def i_need_decoration2(num, power):
    print(f'This function calculates power of number')
    return num ** power


print(i_need_decoration1(5))
print(i_need_decoration2(5, 3))

'''
Code Before Function
This function calculates square
Code After Function
25
Code Before Function
This function calculates power of number
Code After Function
125
'''

########### Section 13: Python Generators
########### 100. Generators with Python

# Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off. When a generator function is compiled they become an object that supports an iteration protocol. That means when they are called in your code they don't actually return a value and then exit. Generator functions will automatically suspend and resume their execution and state around the last point of value generation. This is being done by yield keyword. The advantage is that instead of having to compute an entire series of values up front, the generator computes one value waits until the next value is called for. For example, the range() function doesn’t produce an list in memory for all the values from start to stop. Instead it just keeps track of the last number and the step size, to provide a flow of numbers. 
#yield - The yield keyword in python works like a return with the only difference is that instead of returning a value, it gives back a generator object to the caller. When a function is called and the thread of execution finds a yield keyword in the function, the function execution stops at that line itself and it returns a generator object back to the caller.

def test_yield():
    yield "yield - abc"
    return "return - abc"  # this is not being returned because of yield in previous statement


print(test_yield())  # this will not print what is yielded but it will return generator object
# <generator object test_yield at 0x020B84F8>
# to print what is yielded we need to iterate over generator object as below -

for i in test_yield():
    print(i)  # yield - abc

##################################################################################

def cube(n):
    for ii in range(n):
        yield ii ** 3


for i in cube(5):  # iterating through generator object
    print(i)

print(list(cube(10)))  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]


def fibo(n):
    a = 1
    b = 1
    for ii in range(n):
        yield a
        a, b = b, a + b  # tuple matching


print(list(fibo(10)))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# for internally calls next() to get next generated value and
# stops iteration when it gets StopIteration as shown below -


def simple_gen(n):
    for ii in range(n):
        yield ii


g = simple_gen(3)
print(g)    # <generator object simple_gen at 0x00CD84F8>
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
# print(next(g))  # StopIteration

# iter - it helps to iterate over non iterable object.
# for ex - str object is not iterable lets check on how to iterate over it

s = "hi"
for i in s:
    print(i)

# next(s) # TypeError: 'str' object is not an iterator

s_iter = iter(s)
print(next(s_iter))    # h
print(next(s_iter))   # i


########### 101. Generators Homework

'''
Problem 1
Create a generator that generates the squares of numbers up to some number N.

def gensquares(N):

    for i in range(N):
        yield i*i


for x in gensquares(10):
    print(x)
    
Problem 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:

import random


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low ,high)


for num in rand_num(1, 10, 12):
    print(num)
    
Problem 3
Use the iter() function to convert the string below into an iterator:
s = 'hello'
s_iter = iter(s)
print(next(s_iter))


Problem 4
Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.



Extra Credit -
Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator comprehensions use circular brackets whereas list comprehensions use square brackets. The major difference between them is that generators don’t allocate memory for the whole list. Instead, they generate each value one by one which is why they are memory efficient.

my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)  # 4\n5

print(type(gencomp))  # <class 'generator'>

t_gencomp = tuple(item for item in my_list if item > 3)

for item in t_gencomp:
    print(item)  # 4\n5

print(type(t_gencomp))  # <class 'tuple'>
'''

########### Section 14: Advanced Python Modules
########### 104. Python Collections Module

# Counter is subclass of dictionary

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

print(c)  # Counter({'j': 4, 'k': 4, 'e': 3, 'N': 3, 'f': 2, 'n': 2, 'a': 1, 'q': 1, 'w': 1,
# 'F': 1, 'R': 1, 'G': 1, 'K': 1, 'J': 1, 'A': 1, 'v': 1})
print(type(c))  # <class 'collections.Counter'>

# n most common entries - print(c.most_common(n))
print(c.most_common(3))  # [('j', 4), ('k', 4), ('e', 3)]

# n least common entries - print(c.most_common()[:-n-1:-1])
print(c.most_common())  # [('j', 4), ('k', 4), ('e', 3), ('N', 3), ('f', 2), ('n', 2), ('a', 1),
# ('q', 1), ('w', 1), ('F', 1), ('R', 1), ('G', 1), ('K', 1), ('J', 1), ('A', 1), ('v', 1)]
print(c.most_common()[:-4:-1])  # 3 least common    # [('v', 1), ('A', 1), ('J', 1)]

print(c.values())  # dict_values([2, 1, 4, 4, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1])
print(sum(c.values()))  # 28

print(list(c))  # ['f', 'a', 'j', 'k', 'e', 'q', 'w', 'N', 'F', 'R', 'G', 'K', 'J', 'A', 'n', 'v']
print(set(c))  # {'v', 'G', 'q', 'a', 'w', 'N', 'j', 'J', 'A', 'n', 'K', 'F', 'f', 'R', 'e', 'k'}
print(dict(c))  # {'f': 2, 'a': 1, 'j': 4, 'k': 4, 'e': 3, 'q': 1, 'w': 1, 'N': 3, 'F': 1, 'R': 1,
# 'G': 1, 'K': 1, 'J': 1, 'A': 1, 'n': 2, 'v': 1}

print(c.items())    # dict_items([('f', 2), ('a', 1), ('j', 4), ('k', 4), ('e', 3), ('q', 1),
# ('w', 1), ('N', 3), ('F', 1), ('R', 1), ('G', 1), ('K', 1), ('J', 1), ('A', 1), ('n', 2), ('v',
# 1)])
print(Counter(dict(c.items())))  # Counter({'j': 4, 'k': 4, 'e': 3, 'N': 3, 'f': 2, 'n': 2, 'a': 1,
# 'q': 1, 'w': 1, 'F': 1, 'R': 1, 'G': 1, 'K': 1, 'J': 1, 'A': 1, 'v': 1})

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

# Default dictionary - is used to avoid keyerror for absent keys
# d = defaultdict(callable_function)

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

# NamedTuple like dictionaries they contain keys that are hashed to a particular value. But on contrary, it supports both access from key value and iteration, the functionality that dictionaries lack.
# Syntax - namedtuple(typename, fieldname[])

from collections import namedtuple

Car = namedtuple('Car', ['name', 'company', 'CNG', 'PriceStart'])
nexon = Car('Nexon', 'TATA', False, 7)
baleno = Car(company='Suzuki', name='Baleno', PriceStart=5.5, CNG=True)

print(Car)  # <class '__main__.Car'>
print(nexon)    # Car(name='Nexon', company='TATA', CNG=False, PriceStart=7)
print(baleno)   # Car(name='Baleno', company='Suzuki', CNG=True, PriceStart=5.5)

# Accessing via fieldname
print(f"{nexon.name}({nexon.company}) price start is {nexon.PriceStart}L. CNG Present -"
      f" {nexon.CNG}")  # Nexon(TATA) price start is 7L. CNG Present - False

# Accessing via index
print(f"{baleno[0]}({baleno[1]}) price start is {baleno[3]}L. CNG Present - {baleno[2]}")
# Baleno(Suzuki) price start is 5.5L. CNG Present - True

########### 105. Opening and Reading Files and Folders (OS & Shell Utilities Module)

import os
import shutil

f = open('practice.txt', 'w+')
f.write('This is a test text')
f.close()

udemy_path = 'C:\\Users\\A711929\\OneDrive - Atos\\Documents' \
             '\\Study MAterial\\Python\\PyCharm Projects\\PyBootCamp'

# os.listdir("Path\\of\\Directory")
print(f"Contents in '{os.getcwd()}' are - {os.listdir()}")
# Contents in 'C:\Users\A711929\OneDrive - Atos\Documents\Study MAterial\Python\PyCharm Projects\
# Udemy\OS and Shutil' are -
# ['Delete', 'move.html', 'os_and_shutil.py', 'practice.txt', 'Root', 'SubDir']

print(os.listdir(udemy_path + "\\Milestone Project 2"))
# ['BLACKJACK.py', 'BLACKJACK_share.py', 'WAR of CARDS.py']

'''
shutil.move('source\\path', 'destination\\path')
if file with same name is already there then
shutil.Error: "Destination path '%s' already exists" is raised
'''

print(f"Before Move contents in CWD - {os.listdir(os.getcwd())}")
# Before Move contents in CWD -
# ['Delete', 'move.html', 'os_and_shutil.py', 'practice.txt', 'Root', 'SubDir']

shutil.move('move.html', udemy_path + '\\OS and Shutil\\SubDir')

print(f"After Move contents in CWD - {os.listdir(os.getcwd())}")
# After Move contents in CWD - ['Delete', 'os_and_shutil.py', 'practice.txt', 'Root', 'SubDir']

print("After Move contents in SubDir - ", end='')
print(os.listdir(os.getcwd() + '\\SubDir'))
# After Move contents in SubDir - ['move.html']

print('move.html is moved back to its original location - ')

print(shutil.move(udemy_path + '\\OS and Shutil\\SubDir\\move.html', os.getcwd()))
# C:\Users\A711929\OneDrive - Atos\Documents\Study MAterial\Python\
# PyCharm Projects\Udemy\OS and Shutil\move.html

'''
Deleting Files

NOTE: The os module provides 3 methods for deleting files:
1) os.unlink(path) which deletes a file at the path your provide
2) os.rmdir(path) which deletes a root (root must be empty) at the path your provide
3) shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders 
contained in the path. 

All of these methods can NOT be reversed! Which means if you make a 
mistake you won't be able to recover the file. Instead we will use the send2trash module. 
A safer alternative that sends deleted files to the trash bin instead of permanent removal.
'''


# Send2Trash
import send2trash

print("Before Delete contents in Delete - ", end='')
print(os.listdir(os.getcwd() + "\\Delete"))
# Before Delete contents in Delete - ['delete.html']

send2trash.send2trash(os.getcwd() + '\\Delete\\delete.html')

print("After Delete contents in Delete - ", end='')
print(os.listdir(os.getcwd() + "\\Delete"))
# After Delete contents in Delete - []

print(f"Before Delete contents in CWD - {os.listdir(os.getcwd())}")
# Before Delete contents in CWD - ['Delete', 'move.html', 'os_and_shutil.py', 'practice.txt',
# 'SubDir']

send2trash.send2trash(os.getcwd() + '\\Delete')

print(f"After Delete contents in CWD - {os.listdir(os.getcwd())}")
# After Delete contents in CWD - ['move.html', 'os_and_shutil.py', 'practice.txt', 'SubDir']


print(os.walk(os.getcwd()))  # <generator object walk at 0x01C0B6B8>

for root, folders, files in os.walk(os.getcwd() + "\\Root"):

    print(f"-------------------------------------------------------------------\n"
          f"Currently looking at Folder - {root}")
    print('\nThe Subfolders are - ')

    for sf in folders:
        print(f"\tSubfolder - {sf}")

    print("\nThe Files are - ")

    for f in files:
        print(f"\tFile - {f}")

    print('-------------------------------------------------------------------\n')

    # OR

    '''
    print(root)     # Path of root
    print(folders)  # list
    print(files)    # list
    '''

########### 106. Python Datetime Module

import datetime

my_time = datetime.time(15, 46, 53, 999999)  # ValueError: microsecond must be in 0..999999
print(f"{my_time.hour}H : {my_time.minute}M : {my_time.second}S ({my_time.microsecond}MS)")
# 15H : 46M : 53S (999999MS)
print(my_time)  # 15:46:53.999999

today = datetime.date.today()
print(today)    # 2021-02-14
print(f"{today.day}/{today.month}/{today.year} ({today.isoweekday()})") # 14/2/2021 (7)

date_time = datetime.datetime(2021, 12, 6, 14, 36, 45, 986)
print(date_time)    # 2021-12-06 14:36:45.000986
print(date_time.replace(day=26))  # original object stays unchanged # 2021-12-26 14:36:45.000986
print(date_time)    # 2021-12-06 14:36:45.000986
date_time = date_time.replace(day=26)
print(f"{date_time} ({date_time.timestamp()}) ({date_time.ctime()})")
# 2021-12-26 14:36:45.000986 (1640509605.000986) (Sun Dec 26 14:36:45 2021)

dt1 = datetime.datetime(2021, 11, 26, 15)
dt2 = datetime.datetime(2022, 11, 26, 16)

diff = dt2 - dt1
print(diff) # 365 days, 1:00:00

########### 107. Python Math and Random Modules

# MATH MODULE
import math

print(math.ceil(1.1))  # 2
print(math.ceil(1.5))  # 2
print(math.ceil(1.9))  # 2

print(math.floor(1.1))  # 1
print(math.floor(1.5))  # 1
print(math.floor(1.9))  # 1

print(round(1.5))  # 2
print(round(2.5))  # 2

print(math.ceil(-1.1))  # -1
print(math.ceil(-1.5))  # -1
print(math.ceil(-1.9))  # -1

print(math.floor(-1.1))  # -2
print(math.floor(-1.5))  # -2
print(math.floor(-1.9))  # -2

print(round(-1.5))  # -2
print(round(-2.5))  # -2

print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math.nan)  # nan # not an number
print(math.inf)  # inf # infinity

# math.log() is natural log to base e i.e. ln
print(math.log(math.e))  # 1.0
print((math.log(100, 10)))  # 2.0 # log(x, base) # log of 100 to base 10

# 360° = 2π radians and
# 180° = π radians
print(math.degrees(math.pi/180))  # 1.0 # convert input to degrees
print(math.radians(180))    # 3.141592653589793 # pi    # convert input to radians

# input in radian
print(math.sin(math.pi/6))     # 0.49999999999999994    # 0.5
print(math.sin(math.radians(30)))   # 0.49999999999999994   # 0.5

# RANDOM MODULE
import random

# randint(a, b) # range from a to b & includes a and b as well
print(random.randint(1, 5))

# SEED
# random.seed(3)
print(f"Random no. with seed 3 - {random.randint(1, 5)}")  # will generate a random number

# if you want to use the same random number (or same sequence of random numbers) once again in your
# program use the same seed you used before
# random.seed(3)
print(f"Random no. with seed 3 - {random.randint(1, 5)}")  # same random number as before

'''
A random number is generated by some operation on previous value. If there is no previous 
value then the current time is taken as previous value automatically. We can provide this 
previous value by own using random.seed(x) where x could be any number or string etc. 
random.randint() is not actually perfect random number, it could be predicted via random.seed(x). 
Hence, generating a random number is not actually random, because it runs on algorithms. 
Algorithms always give the same output based on the same input. This means, it depends on the 
value of the seed. So, in order to make it more random, time is automatically assigned to seed(). 
'''

mylist = list(range(1, 20))
print(mylist)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# random.choices(sequence) return list by default k = 1
print(random.choices(mylist))   # [7]

# CHOICES WITH REPLACEMENT
# though duplication is not guaranteed
print(random.choices(population=mylist, k=10))  # [18, 6, 4, 16, 8, 3, 9, 14, 12, 2]

# SAMPLE WITHOUT REPLACEMENT
print(random.sample(population=mylist, k=10))  # [3, 15, 18, 14, 9, 5, 4, 2, 7, 19]

random.shuffle(mylist)  # it returns nothing but original sequence is affected
print(mylist)  # [8, 11, 6, 14, 19, 18, 4, 12, 16, 5, 17, 15, 3, 2, 9, 1, 13, 10, 7]
# random.shuffle() works only on mutable sequences ; ex. - random.shuffle() will not work on tuple
# To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.

# UNIFORM & GAUSS DISTRIBUTION
print(random.uniform(1.5, 100))  # 93.091505177311
print(random.gauss(mu=0, sigma=1))  # -0.31585904714252705

########### 108. Python Debugger

import pdb  # py debugger

x = 2
y = 3
z = [3, 5, 7]

result1 = x + y
pdb.set_trace()
result2 = z + x

'''

Output -

> c:\users\a711929\onedrive - atos\documents\study material\python\pycharm projects\udemy\py_debugger.py(9)<module>()
-> result2 = z + x
(Pdb) z
[3, 5, 7]
(Pdb) x
2
(Pdb) result2
*** NameError: name 'result2' is not defined
(Pdb) result1
5
(Pdb) n
TypeError: can only concatenate list (not "int") to list
> c:\users\a711929\onedrive - atos\documents\study material\python\pycharm projects\udemy\py_debugger.py(9)<module>()
-> result2 = z + x
(Pdb) n
--Return--
> c:\users\a711929\onedrive - atos\documents\study material\python\pycharm projects\udemy\py_debugger.py(9)<module>()->None
-> result2 = z + x
(Pdb) n
--Call--
Traceback (most recent call last):
  File "C:/Users/A711929/OneDrive - Atos/Documents/Study MAterial/Python/PyCharm Projects/Udemy/py_debugger.py", line 9, in <module>
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(309)__init__()
-> def __init__(self, errors='strict'):
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(310)__init__()
-> IncrementalDecoder.__init__(self, errors)
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(312)__init__()
-> self.buffer = b""
(Pdb) n
--Return--
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(312)__init__()->None
-> self.buffer = b""
(Pdb) n
--Call--
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(331)getstate()
-> def getstate(self):
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(333)getstate()
-> return (self.buffer, 0)
(Pdb) n
--Return--
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(333)getstate()->(b'', 0)
-> return (self.buffer, 0)
(Pdb) n
--Call--
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(319)decode()
-> def decode(self, input, final=False):
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(321)decode()
-> data = self.buffer + input
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(322)decode()
-> (result, consumed) = self._buffer_decode(data, self.errors, final)
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(324)decode()
-> self.buffer = data[consumed:]
(Pdb) n
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(325)decode()
-> return result
(Pdb) n
--Return--
> c:\users\a711929\appdata\local\programs\python\python38-32\lib\codecs.py(325)decode()->
'import pdb  ...2 = z + x\r\n'
-> return result
(Pdb) n
    result2 = z + x
TypeError: can only concatenate list (not "int") to list

'''

########### 109. Python Regular Expressions Part One

import re

text = "I have mobile. And my mobile no. is 1234567890"
pattern = "mobile"

print(pattern in text)  # True
# re.search(pattern, text) will always give span of 1st match
print(re.search(pattern, text))  # <re.Match object; span=(7, 13), match='mobile'>
print(re.search(pattern + "garbage", text))  # None # as that is not in text

search_result = re.search(pattern, text)
print(f"Pattern - \"{pattern}\" in Text - \"{text}\" is at {search_result.span()} -> from index"
      f" {search_result.start()} to {search_result.end()}")
# Pattern - "mobile" in Text - "I have mobile. And my mobile no. is 1234567890" is at
# (7, 13) -> from index 7 to 13

print(re.findall(pattern, text))   # ['mobile', 'mobile']

# finditer returns re.Match objects with span() for all matches
for i in re.finditer(pattern, text):
    print(f"{i} '{i.group()}'-> {i.span()} -> {i.start()} to {i.end()}")

########### 110. Python Regular Expressions Part Two

import re

'''
Character Identifier

Character	Description         Pattern Code	Example Match
\d	        A digit	            file_\d\d	    file_25
\w	        Alphanumeric	    \w-\w\w\w	    A-b_1
\s	        White space	        a\sb\sc	        a b c
\D	        A non digit	        \D\D\D	        ABC
\W	        Non-alphanumeric	\W\W\W\W\W	    *-+=)
\S	        Non-whitespace	    \S\S\S\S	    Yoyo
'''

text = "I have mobile. My 1st mobile number is 123-456-7898. My 2nd mobile number is 321-654-8987"
# phones = re.finditer(r'\d{3}-\d{3}-\d{4}', text)
phones = re.finditer(r'\d\d\d-\d\d\d-\d\d\d\d', text)
for i in phones:
    print(f"{i}'{i.group()}'->{i.span()} from index {i.start()} to {i.end()}")

# <re.Match object; span=(39, 51), match='123-456-7898'>'123-456-7898'->(39, 51) from index 39 to 51
# <re.Match object; span=(77, 89), match='321-654-8987'>'321-654-8987'->(77, 89) from index 77 to 89

'''
Quantifier

Character	Description	                Pattern Code	Example Match
+	        Occurs one or more times	Version \w-\w+	Version A-b1_1
{3}	        Occurs exactly 3 times	    \D{3}	        abc
{2,4}	    Occurs 2 to 4 times	        \d{2,4}	        123
{3,}	    Occurs 3 or more	        \w{3,}	        anycharacters
\*	        Occurs zero or more times	A\*B\*C*	    AAACC
?	        Once or none	            plurals?	    plural
'''

'''
Groups
What if we wanted to do two tasks, find phone numbers, but also be able to quickly extract 
their area code (the first three digits). We can use groups for any general task that involves grouping together regular expressions (so that we can later break them down).
'''

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # grouping

results = re.search(pattern, text)

print(f"{results.group()} : {results.group(1)}-{results.group(2)}-{results.group(3)}")
# 123-456-7898 : 123-456-7898


########### 111. Python Regular Expressions Part Three

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

########### 112. Timing Your Python Code

import time     # this can be used to calculate time exactly if time span is larger or n is larger
import timeit   # this can be used to calculate time exactly if time span is smaller or n is small


def func1(n):
    return [str(num) for num in range(n)]


def func2(n):
    return list(map(str, range(n)))


start_time = time.time()
func1(10000000)
end_time = time.time()
print(end_time - start_time)  # 5.9697020053863525

start_time = time.time()
func2(10000000)
end_time = time.time()
print(end_time - start_time)  # 4.814321041107178

'''
but if you have n small you can use timeit
syntax -
timeit.timeit(stmt=<code_execution>, setup=<code_definition>, number=<no. of times you want to 
execute>)
'''

stmt3 = '''
func3(100)
'''
setup3 = '''
def func3(n):
    return [str(num) for num in range(n)] 
'''
print(timeit.timeit(stmt3, setup3, number=100000))  # 3.445076499999999

stmt4 = '''
func4(100)
'''
setup4 = '''
def func4(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt4, setup4, number=100000))  # 3.000827299999999


########### 113. Zipping and Unzipping files with Python

import zipfile  # compress single files
import shutil  # compress folder

f1 = open('file1.txt', 'w+')
f1.write('1st file')
f1.close()

f2 = open('file2.txt', 'w+')
f2.write('2nd file')
f2.close()

compress_file = zipfile.ZipFile('myfile.zip', 'w')
compress_file.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)
compress_file.write('file2.txt', compress_type=zipfile.ZIP_DEFLATED)
compress_file.close()

uncompress_file = zipfile.ZipFile('myfile.zip', 'r')
uncompress_file.extractall('extracted')

# But if you want to archive whole directory instead then check below

dir_to_archive = "C:\\Users\\A711929\\OneDrive - Atos\\Documents\\Study MAterial" \
                 "\\Python\\PyCharm Projects\\PyBootCamp\\Zip File\\extracted"
output_filename = 'Archived'
shutil.make_archive(output_filename, 'tar', dir_to_archive)
shutil.unpack_archive('Archived.tar', 'UnArchived', 'tar')

########### 114. Advanced Python Module Puzzle - Overview

import zipfile
import os
import re

unzip = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
unzip.extractall('puzzle unzipped')
unzip.close()

instructions = open(os.getcwd() + "\\puzzle unzipped\\extracted_content\\Instructions.txt", 'r')
print(f"\n{instructions.read()}")
instructions.close()

for root, folders, files in os.walk(os.getcwd() + "\\puzzle unzipped\\extracted_content"):
    # print(f"------------------------\nCurrently looking in '{root}' directory - ")

    # print(f"\nThe folders are - ")
    # for i_folder in folders:
    #    print(f"\t{i_folder}")

    # print(f"\nThe files are - ")
    for i_file in files:
        # print(f"\t{i_file}")
        myfile = open(root + "\\" + i_file, 'r')
        contents = myfile.read()
        myfile.close()
        match = re.search(r'\d{3}-\d{3}-\d{4}', contents)
        if match:
            print(f"\nTelephone number - {match.group()} found in '{i_file}' file which is in "
                  f"\n'{root}' directory")
            print(f"At index starting from {match.start()} to {match.end()}")

    # print("\n")

# OUTPUT -

'''
Good work on unzipping the file!
You should now see 5 folders, each with a lot of random .txt files.
Within one of these text files is a telephone number formated ###-###-#### 
Use the Python os module and regular expressions to iterate through each file, open it, and search 
for a telephone number. Good luck!

Telephone number - 719-266-2837 found in 'EMTGPSXQEJX.txt' file which is in 
'C:\\Users\\A711929\\OneDrive - Atos\\Documents\\Study MAterial\\Python\\PyCharm Projects
\\PyBootCamp\\Module Puzzle\\puzzle unzipped\\extracted_content\\Four' directory
At index starting from 1062 to 1074
'''

########### Section 15: Web Scraping with Python
########### 116. Introduction to Web Scraping
'''
Web scraping is a general term for techniques involving automating the gathering of data from a website.
​
HTML - Hyper Text Markup Language (Structure of website )
CSS - Cascading Style Sheets (Appearance of website)
JS - Java Script (Interaction of website)

Rules of Web Scraping​
>   Always try to get permission before scraping!​
>   If you make too many scraping attempts or requests your IP Address could get blocked!​
>   Some sites automatically block scraping software.

HTML is used to create the basic structure and content of a webpage​
CSS is used for the design and style of a web page, where elements are placed and how it looks​
JavaScript is used to define the interactive elements of a webpage 

In CSS id (one use) is denoted by # and class (multi use) by period / dot (.)
'''

########### 117. Setting Up Web Scraping Libraries

'''
We will be using BeautifulSoup and requests libraries. Install them -
pip install requests
pip install lxml​
Or for Anaconda distributions, use conda install instead of pip install.​
'''

########### 118. Python Web Scraping - Grabbing a Title

import requests
import bs4

result = requests.get("http://www.example.com/")
print(result)   # <Response [200]>
print(type(result))     # <class 'requests.models.Response'>
print(result.text)      # HTML structure of website in string format

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)     # beautify the result
print(soup.select('title'))     # [<title>Example Domain</title>]
print(soup.select('p'))
# [<p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>,
#  <p><a href="https://www.iana.org/domains/example">More information...</a></p>]

# get text from which ever Tag you want using list indexing
print(soup.select('title')[0].getText())    # Example Domain
print(soup.select('p')[1].getText())    # More information...
print(type(soup.select('title')[0]))    # <class 'bs4.element.Tag'>

########### 119. Python Web Scraping - Grabbing a Class

import requests
import bs4

'''
Syntax                      --> Match Results
soup.select(‘div’)          --> All elements with ‘div’ tag
soup.select(‘#some_id’)     --> Elements containing id=’some_id’
soup.select(‘.some_class’)  --> Elements containing class = ‘some_class’
soup.select(‘div span’)     --> Any elements named span within a div element.
soup.select(‘div > span’)   --> Any elements named span directly within a div element, 
                                with nothing in between.
'''

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup.select('.toctext'))
'''
[<span class="toctext">Early life and education</span>, <span class="toctext">Career</span>, 
<span class="toctext">World War II</span>, .....]
'''
print(soup.select('.toctext')[2])   # <span class="toctext">World War II</span>
print(soup.select('.toctext')[2].text)  # World War II
for item in soup.select('.toctext'):    # will print all the text one by one
    print(item.text)

########### 120. Python Web Scraping - Grabbing an Image

import requests
import bs4

response = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(response.text, 'lxml')

print(soup.select('.thumbimage'))  # all tags containing class as image, then check which 1 do you
# want
deep_blue = soup.select('.thumbimage')[0]  # grab that image and store in object bs4.element.Tag
print(deep_blue)  # as this is bs4.element.Tag we can consider it as dictionary and get what we want
print(deep_blue['src'])     # will give you the URL of where the actual image is

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/'
                     'Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
image_file = open('my_pic.png', 'wb')   # match file extension with URL ; # wb = write binary
image_file.write(image_link.content)    # image_link.content is binary representation of image
image_file.close()

########### 121. Python Web Scraping - Book Examples Part One

# GOAL - Get a title of every book with 2 star rating on http://toscrape.com/
import requests
import bs4

'''
#   Experiments trying to figure out title of 1 book
base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
print(base_url.format('1'))  # https://books.toscrape.com/catalogue/page-1.html
response = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(response.text, 'lxml')
books = soup.select('.product_pod')
print(len(books))   # 20 # As there are 20 books
print(books[10])    # 11th book details
print(str(books[10]))
print('star-rating Two' in str(books[10]))  # True # bad way as this can be matched with anything
print(books[10].select('.star-rating.Two'))     # will give you list # Good way
# if there is space in class name remember to give '.' instead of space
print(books[10].select('.star-rating.Four'))     # will give you empty list and this can be hint
# to find book with star rating two

print(books[10].select('a')[1]['title'])
# we are selecting 'a' tag as required title is in that tag
# but selecting 'a' gives two 'a' tags as there are two 'a' tags in class '.product_pod'
# but the required book title is in 2nd 'a' tag which is at index [1]
# and as this is bs4.element.Tag as similar to dictionary 
# we can use ['title'] to grab the actual title of book
'''

for i in range(1, 51):
    print(f'\n*********************************\nBooks with 2 star rating on page {i} are - ')
    base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
    response = requests.get(base_url.format(str(i)))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if book.select('.star-rating.Two'):     # if the list is empty the if will be false
            print(book.select('a')[1]['title'])

########### 124. Python Web Scraping - Exercise Solutions

# TASK: Import any libraries you think you'll need to scrape a website.
import requests
import bs4

# TASK: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.
response = requests.get('http://quotes.toscrape.com/')
print(response.text)

# TASK: Get the names of all the authors on the first page.
soup = bs4.BeautifulSoup(response.text, 'lxml')
authors = set()     # use set to get unique ones
for author in soup.select('.author'):
    authors.add(author.text)
print(authors)

# TASK: Create a list of all the quotes on the first page.
quotes = []
for quote in soup.select('.text'):
    quotes.append(quote.text)
print(quotes)

# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text
# shown on the top right from the home page (e.g Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote, try to find a class only present
# in the top right tags, perhaps check the span.
for tag in soup.select('.tag-item'):
    print(tag.text)


# TASK: Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation
# to loop through all the pages and get all the unique authors on the website.
# Keep in mind there are many ways to achieve this, also note that you will need to somehow
# figure out how to check that your loop is on the last page with quotes.
# For debugging purposes, I will let you know that there are only 10 pages,
# so the last page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust
# enough that it wouldn't matter to know the amount of pages beforehand, perhaps use try/except
# for this, its up to you!
base_URL = 'http://quotes.toscrape.com/page/{}'
page_number = 1
authors = set()
response = requests.get(base_URL.format(str(page_number)))
soup = bs4.BeautifulSoup(response.text, 'lxml')
''' WAY 1 -
while True:
    try:
        for author in soup.select('.author'):
            authors.add(author.text)
        check = soup.select('.next a')[0]['href']   # this will indicate to continue / break
        page_number += 1
        response = requests.get(base_URL.format(str(page_number)))
        soup = bs4.BeautifulSoup(response.text, 'lxml')
    except IndexError:
        break
'''
# WAY 2 -
while True:
    for author in soup.select('.author'):
        authors.add(author.text)
    if not soup.select('.next a'):  # for last page this (list) will be empty and if will be False
        break
    page_number += 1
    response = requests.get(base_URL.format(str(page_number)))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
''' WAY 3 -
while True:
    for author in soup.select('.author'):
        authors.add(author.text)
    page_number += 1
    response = requests.get(base_URL.format(str(page_number)))
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    if soup.select('.previous a')[0]['href'] == '/page/10/':    # for page after last page 
    # previous a href will be  /page/10/
        break
'''
# WAY 4 - will be to check for "No quotes found!" in response.text if true apply break :)
print(authors)
print(len(authors))     # 50

########### Section 16: Working with Images with Python
########### 125. Introduction to Images with Python

# pip install pillow
# We will use the Pillow library for working with Images, which is a fork of the PIL (Python Imaging Library)
# Documentation - https://pillow.readthedocs.io

########### 126. Working with Images with Python

from PIL import Image

# Note actual image file stays unaffected only object of Image() is affected

computer = Image.open('example.jpg')
computer.show()  # opens the image
print(type(computer))   # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(computer.size)  # (1993, 1257) # (width, height) in pixels
print(computer.filename)  # example.jpg
print(computer.format_description)  # JPEG (ISO 10918)

pencils = Image.open('pencils.jpg')
pencils.show()
print(pencils.size)  # (1950, 1300)

# cropping of Image
# Top Left crop
x = 0
y = 0
# (x,y) can be considered as top left
w = 1950 / 3
h = 1300 / 10
# (w,h) can be considered as bottom right
pencils.crop((x, y, w, h)).show()

# Bottom Left crop
x = 0
y = 1100
w = 1950 / 3
h = 1300
pencils.crop((x, y, w, h)).show()

# Lets try to get computer by cropping
x = (1993 / 2) - 120
y = (1257 / 2) + 210
w = (1993 / 2) + 150
h = 1257

# pasting cropped computer into pencils in -

# top right corner
cropped_computer = computer.crop((x, y, w, h))
# we need to figure out where will the top right corner (box) of the cropped computer will go as
# below
cx = 1950 - (w - x)
cy = 0
pencils.paste(im=cropped_computer, box=(int(cx), int(cy)))
pencils.show()

# lets paste it bottom right also
cy = 1300 - (h - y)
pencils.paste(im=cropped_computer, box=(int(cx), int(cy)))
pencils.show()

# resize # make sure pass as tuple
computer.resize((3000, 500)).show()

# left rotate by degrees
computer.rotate(90).show()

# resize & rotate didn't affected original Image() object
computer.show()

######################## COLOR TRANSPARENCY ########################

from PIL import Image

# RGBA - Red, Green, Blue, Alpha
# All RGBA have values from 0 to 255
# In case of Alpha 0, image is completely transparent and 255 is opaque

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.jpg')

# to change transparency you can use putalpha(<int from 0 to 255>)
red.show()  # before dark
red.putalpha(128)
red.show()  # after light

blue.show()
blue.putalpha(128)
blue.show()

# to get purple
blue.paste(im=red, box=(0, 0), mask=red)
blue.show()
# usually pasting one image on another will hide the below one but as we have adjusted
# transparency using putalpha() hence we get to see effect of both colors which is purple
blue.save('purple_color.png')
purple = Image.open('purple_color.png')
purple.show()

######################## CONVERTING PNG to JPG ########################

# convert from png to jpg
# png - RGBA
# jpg - RGB

from PIL import Image

# current image
blue_png = Image.open('C:\\Users\\A711929\\OneDrive - Atos\\Documents\\Study '
                      'MAterial\\Python\\PyCharm Projects\\PyBootCamp\\Images\\blue_color.png')

blue_jpg = blue_png.convert('RGB')

# new image
blue_jpg.save('C:\\Users\\A711929\\OneDrive - Atos\\Documents\\Study MAterial\\Python\\PyCharm '
              'Projects\\PyBootCamp\\Images\\blue_color.jpg')

########### 127. & 128. Python Image Exercise

from PIL import Image

# load images into Image() objects
words = Image.open('word_matrix.png')
word_masks = Image.open('mask.png')

# resize as per words size
print(words.size)
word_masks = word_masks.resize((1015, 559))

# adjust transparency of mask and paste mask on words
word_masks.putalpha(128)
words.paste(im=word_masks, box=(0, 0), mask=word_masks)
words.show()

########### Section 17: Working with PDFs and Spreadsheet CSV Files
########### 130. Working with CSV Files in Python

# CSV - Comma Separated Values

import csv

# Wrong Way to open file - Common Error - UnicodeDecodeError
# data = open('example.csv')
# Mention encoding to identify special characters in file like below -
data = open('example.csv', encoding='utf-8')
data_csv = csv.reader(data)
data_lines = list(data_csv)     # convert data in list[list[]] form

# print(data_lines[0])    # column header

# lets print 1st 5 data
for line in data_lines[:6]:
    print(line)
'''
['id', 'first_name', 'last_name', 'email', 'gender', 'ip_address', 'city']
['1', 'Joseph', 'Zaniolini', 'jzaniolini0@simplemachines.org', 'Male', '163.168.68.132', 
'Pedro Leopoldo']
['2', 'Freida', 'Drillingcourt', 'fdrillingcourt1@umich.edu', 'Female', '97.212.102.79', 'Buri']
['3', 'Nanni', 'Herity', 'nherity2@statcounter.com', 'Female', '145.151.178.98', 'Claver']
['4', 'Orazio', 'Frayling', 'ofrayling3@economist.com', 'Male', '25.199.143.143', 'Kungur']
['5', 'Julianne', 'Murrison', 'jmurrison4@cbslocal.com', 'Female', '10.186.243.144', 
'Sainte-Luce-sur-Loire']
'''

# lets get emails from 2nd to 5th line
for line in data_lines[2:6]:
    print(line[3])
'''
fdrillingcourt1@umich.edu
nherity2@statcounter.com
ofrayling3@economist.com
jmurrison4@cbslocal.com
'''

# lets get full name from 3rd to 5th line
for line in data_lines[2:6]:
    print(line[1] + ' ' + line[2])
'''
Freida Drillingcourt
Nanni Herity
Orazio Frayling
Julianne Murrison
'''

# writing data to CSV file
out_to_csv = open('my.csv', mode='w', newline='')   # note mode is write
csv_writer = csv.writer(out_to_csv, delimiter=',')  # csv reader and writer are sister
# as its CSV delimeter is ',' also it can be '\t' (tab) or ';' (semi colon)

print(csv_writer.writerow(['a', 'b', 'c']))    # 7 # return no. characters written
# 7 = 3 (abc) + 2 (,) + 2 CRLF ('\r\n') Carriage Return & Line Feed
csv_writer.writerows([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])       # return's nothing
out_to_csv.close()      # remember to close the file once finished writing

# appending data to CSV
out_to_csv = open('my.csv', mode='a', newline='')   # note mode is append
csv_writer = csv.writer(out_to_csv, delimiter=',')

csv_writer.writerow(['10', '11', '12'])
csv_writer.writerows([['13', '14', '15'], ['16', '17', '18']])
out_to_csv.close()

########### 131. Working with PDF Files in Python

# pip install PyPDF2
# A PDF which is simply scanned is highly unlikely to be readable by Python PyPDF2

# PDF - Portable Document Format

import PyPDF2

f = open('Working_Business_Proposal.pdf', 'rb')  # mode = 'rb' , ready binary

# Read pages from PDF
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)  # 5
page1 = pdf_reader.getPage(0)  # 1st page, index starting with 0
print(type(page1))      # <class 'PyPDF2.pdf.PageObject'>
page1_text = page1.extractText()
print(page1_text)  # prints all text on page 1 including header and footer also

# Add page to new PDF
# PyPDF2 can only write to a new PDF page and can't modify existing PDF page
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page1)  # only object type <class 'PyPDF2.pdf.PageObject'> can be added
# open new file where you want to write
new_pdf = open('MyPDF.pdf', 'wb')   # create new file / if exists overwrite # mode - write binary
pdf_writer.write(new_pdf)
new_pdf.close()

# To read all the text from PDF
pdf_text = []   # index represent page
for num in range(pdf_reader.numPages):
    pdf_text.append(pdf_reader.getPage(num).extractText())
# in list comprehension style -
pdf_text = [pdf_reader.getPage(num).extractText() for num in range(pdf_reader.numPages)]
print(pdf_text)

f.close()

########### 132. & 133. PDFs and Spreadsheets Python Puzzle Exercise - Solutions

# Task One: Use Python to extract the Google Drive link from the .csv file. (Hint: Its along the diagonal from top left to bottom right).

import csv

data = open('find_the_link.csv', encoding='utf-8')
data_reader = csv.reader(data)
data_lists = list(data_reader)

link = ""

'''i = 0
for line in data_lists[:]:
    link += line[i]
    i += 1'''

# enumerate adds index to each field in iterable
# >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# >>> list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# >>> list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
for i, line in enumerate(data_lists):
    link += line[i]

print(link)

data.close()

# Task Two: Download the PDF from the Google Drive link (we already downloaded it for you just in case you can't download from Google Drive) and find the phone number that is in the document. Note: There are different ways of formatting a phone number!

import PyPDF2
import re

file = open('Find_the_Phone_Number.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(file)

for num in range(pdf_reader.numPages):
    match = re.search(r'\d{3}\D\d{3}\D\d{4}', pdf_reader.getPage(num).extractText())
    if match:
        print(f"Phone number {match.group()} was present on page no. {num + 1} of PDF document\n"
              f"It was located on index starting from {match.start()} to {match.end()} "
              f"of page no. {num + 1} of PDF document")
        # Phone number 505.503.4455 was present on page no. 14 of PDF document
        # It was located on index starting from 1727 to 1739 of page no. 14 of PDF document

''' # SOLUTION GIVEN in lecture -
pattern = r'\d{3}'  # 1st try to get 3 no.
allPDFtext = ''
for num in range(pdf_reader.numPages):
    allPDFtext += ' ' + pdf_reader.getPage(num).extractText()
# findall will not work as it will give only list of matching patterns
print(re.findall(pattern, allPDFtext))  # ['000', '000', '000', '505', '503', '445']
for each_iter in re.finditer(pattern, allPDFtext):
    print(each_iter)
# <re.Match object; span=(655, 658), match='000'>
# <re.Match object; span=(17805, 17808), match='000'>
# <re.Match object; span=(35059, 35062), match='000'>
# <re.Match object; span=(41808, 41811), match='505'>
# <re.Match object; span=(41812, 41815), match='503'>
# <re.Match object; span=(41816, 41819), match='445'>
print(allPDFtext[41808: 41808 + 20])  # 505.503.4455. So hor  # now redefine pattern using this o/p
pattern = r'\d{3}.\d{3}.\d{4}'
print(re.search(pattern, allPDFtext))
# <re.Match object; span=(41808, 41820), match='505.503.4455'>'''

file.close()

########### Section 18: Emails with Python
########### 134. Introduction to Emails with Python
########### 135. Sending Emails with Python

# To send emails with Python, we need to manually go through the below steps - 
# connecting to an email server, 
# confirming connection, 
# setting a protocol, 
# logging on, 
# sending the message.

# Fortunately the built-in "smtplib" library in Python makes these steps simple function calls.

# What is SMTP ?
# Each major email provider has their own SMTP (Simple Mail Transfer Protocol) Server.
'''
Provider						SMTP server domain name
Gmail (will need App Password)	smtp.gmail.com
Yahoo Mail						smtp.mail.yahoo.com
Outlook.com/Hotmail.com			smtp-mail.outlook.com
AT&T							smpt.mail.att.net (Use port 465)
Verizon							smtp.verizon.net (Use port 465)
Comcast							smtp.comcast.net
'''

'''We will go over this process with a Gmail account.​
For gmail users, you will need to generate an app password instead of your normal password.​
This let’s Gmail know that the Python script attempting to access your account is authorized by you.'''

################ send email TLS ################

import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# if port no. 587 doesn't work you can try 465, if that also doesn't work don't pass any port no.
# if you are using port 587 which means you are using TLS (Transport Layer Security) encryption
# if you are using port 465 which means you are using SSL (Secure Sockets Layer) encryption

# now lets greet server & establish connection using ehlo() which will tell if connection is
# successful or not. This method call needs to be done directly after creating smtplib object,
# calling it after some methods can lead to error
print(smtp_obj.ehlo())  # (250, b'smtp.gmail.com at your service, [103.134.165.10]
#  \nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
# a successful connection is indicated by o/p starting with 250 like above

print(smtp_obj.starttls())   # (220, b'2.0.0 Ready to start TLS')
# if using 465 skip this as you will be using SSL

# Use gmail App Passwords for security - https://support.google.com/accounts/answer/185833?hl=en/
# Click on 2-Step Verification link - https://support.google.com/accounts/answer/185839
# Then follow "Turn on 2-Step Verification" steps and get it turned on get back to 185833 (1st link)
# and then "Create & use App Passwords"

email = input("Email : ")
password = input("Password : ")
print(smtp_obj.login(email, password))  # (235, b'2.7.0 Accepted')

from_email = email
to_email = email
subject = input("Mail Subject : ")
message = input("Mail Body : ")
mail = 'Subject: ' + subject + '\n' + message

print(smtp_obj.sendmail(from_email, to_email, mail))    # {}
# empty {} dictionary indicates its successful

print(smtp_obj.quit())  # (221, b'2.0.0 closing connection ml17sm15836132pjb.18 - gsmtp')


################ send email SSL ################

import smtplib

email = input("Email : ")
password = input("Password : ")
from_email = email
to_email = email
subject = input("Mail Subject : ")
message = input("Mail Body : ")
mail = "Subject: " + subject + '\n' + message

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(server.login(email, password))
print(server.sendmail(from_email, to_email, mail))
print(server.quit())

############## Attachment to email #############

"""Steps to send mail with Attachments from Gmail account:
For adding an attachment, you need to import:

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

These are some libraries which will make our work simple.
These are the native libraries and you dont need to import any external library for this.
Firstly, create an instance of MIMEMultipart, namely “msg” to begin with.
Mention the sender’s email id, receiver’s email id and the subject
in the “From”, “To” and “Subject” key of the created instance “msg”.
In a string, write the body of the message you want to send, namely body.
Now, attach the body with the instance msg using attach function.
Open the file you wish to attach in the “rb” mode.
Then create an instance of MIMEBase with two parameters.
First one is ‘_maintype’ amd the other one is ‘_subtype’.
This is the base class for all the MIME-specific sub-classes of Message.
Note that - ‘_maintype’ is the Content-Type major type (e.g. text or image), and
‘_subtype’ is the Content-Type minor type (e.g. plain or gif or other media).
set_payload is used to change the payload the encoded form. Encode it in encode_base64.
And finally attach the file with the MIMEMultipart created instance msg.
After finishing up these steps, create a session, secure it and check the authenticity and then
after sending the mail, terminate the session."""

# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = input("Email : ")
password = input("Password : ")
toaddr = fromaddr

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = input("Mail Subject : ")

# string to store the body of the mail
body = input("Mail Body : ")

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = input("Enter filename with extension - ")
path = input("Enter path of the file - ")
attachment = open(path + '\\' + filename, "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, password)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()

################ Perfect Email with To Cc Bcc ################

import smtplib

print('Login - ')
sender_mail = input('Email : ')
password = input('Password : ')

n = input('\nEnter no. of "To"s in your mail : ')
To = []
for i in range(int(n)):
    To.append(input(f'"To"({i+1}) : '))

n = input('\nEnter no. of "CC"s in your mail : ')
CC = []
for i in range(int(n)):
    CC.append(input(f'"CC"({i+1}) : '))

n = input('\nEnter no. of "BCC"s in your mail : ')
BCC = []
for i in range(int(n)):
    BCC.append(input(f'"BCC"({i+1}) : '))

subject = input('\nSubject : ')
body = input('Body : ')

mail = f"From: {sender_mail}\nTo: {','.join(To)}\nCC: {','.join(CC)}\nSubject: {subject}\n\n{body}"

To = To + CC + BCC

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())
print(smtp_obj.login(sender_mail, password))
print(smtp_obj.sendmail(sender_mail, To, mail))
print(smtp_obj.quit())

########### 136. Receiving Emails with Python

'''

Keyword						Definition

'ALL'						Returns all messages in your email folder. Often there are size limits from
							imaplib. To change these use imaplib._MAXLINE = 100, where 100 is whatever you want the limit to be.

'BEFORE date'				Returns all messages before the date. Date must be formatted as 01-Nov-2000.

'ON date'					Returns all messages on the date. Date must be formatted as 01-Nov-2000.

'SINCE date'				Returns all messages after the date. Date must be formatted as 01-Nov-2000.

'FROM some_string'			Returns all from the sender in the string. String can be an email, for 
							example 'FROM user@example.com' or just a string that may appear in the email, "FROM example"
							
'TO some_string'			Returns all outgoing email to the email in the string. String can be an
							email, for example 'TO user@example.com' or just a string that may appear in the email, "TO example"

'CC some_string' and/or		Returns all messages in your email folder. Often there are size limits  'BCC some_string'	        imaplib. To change these use imaplib._MAXLINE = 100, where 100 is whatever 
							you want the limit to be.

'SUBJECT string',			Returns all messages with the subject string or the string in the body of 
'BODY string',				the email. If the string you are searching for has spaces in it, wrap it in 
'TEXT "string with spaces"'	double quotes.

'SEEN', 'UNSEEN'			Returns all messages that have been seen or unseen. 
							(Also known as read or unread)

'ANSWERED', 'UNANSWERED'	Returns all messages that have been replied to or unreplied to.		

'DELETED', 'UNDELETED'		Returns all messages that have been deleted or that have not been deleted.

'''

import imaplib
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

myemail = input("Email : ")
password = input("Password : ")
print(M.login(myemail, password))  # ('OK', [b'your@mail.com authenticated (Success)'])

print(M.list())  # Directory structure of your mail
print(M.select('inbox'))  # ('OK', [b'18283'])

typ, data = M.search(None, 'SUBJECT "PERFECT MAIL"')
print(typ)  # OK
print(data)  # [b'18280']    # if no number is returned means there was no such data and if there
# are multiple no. means there are multiple matches for your search. Also this unique number is ID
# of that mail in search result

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
# The Internet RFC 822 specification defines an electronic message format consisting of header
# fields and an optional message body. The header fields contain information about the message,
# such as the sender, the recipient, and the subject. If a message body is included, it is separated
# from the header fields by an empty line (\r\n).

print(email_data)
'''[(b'18281 (RFC822 {639}', 
  b'Bcc: bcc@mail.com\r\n
    Return-Path: <sender@mail.com>\r\n
	Received: from DESKTOP-NAME.www.ROUTER.com ([103.134.165.10])\r\n
	by smtp.gmail.com with ESMTPSA id z12sm14389023pjz.16.2021.02.28.07.32.59\r\n
	(version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);\r\n        
	Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
	Message-ID: <603bb7ad.1c69fb81.543c8.0e1b@mx.google.com>\r\n
	Date: Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
	From: sender@mail.com\r\n
	To: to1@mail.com,to2@mail.com.com\r\n
	CC: cc1@mail.com,cc2@mail.com.com\r\n
	Subject: PERFECT MAIL\r\n
	\r\n
	This is perfect mailwith to cc and bcc. Thanks!\r\n'), 
  b')']'''

raw_email_header = email_data[0][1]  # grabbing message header
raw_email_header_str = raw_email_header.decode('utf-8')

print(raw_email_header_str)
email_message = email.message_from_string(raw_email_header_str)
print(email_message)
'''
Bcc: bcc@mail.com\r\n
Return-Path: <sender@mail.com>\r\n
Received: from DESKTOP-NAME.www.ROUTER.com ([103.134.165.10])\r\n
		by smtp.gmail.com with ESMTPSA id z12sm14389023pjz.16.2021.02.28.07.32.59\r\n
		(version=TLS1_3 cipher=TLS_AES_256_GCM_SHA384 bits=256/256);\r\n        
		Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
Message-ID: <603bb7ad.1c69fb81.543c8.0e1b@mx.google.com>\r\n
Date: Sun, 28 Feb 2021 07:33:01 -0800 (PST)\r\n
From: sender@mail.com\r\n
To: to1@mail.com,to2@mail.com.com\r\n
CC: cc1@mail.com,cc2@mail.com.com\r\n
Subject: PERFECT MAIL\r\n
\r\n
This is perfect mailwith to cc and bcc. Thanks!\r\n
'''

print(type(email_message))  # <class 'email.message.Message'>

# will print message body
for part in email_message.walk():
    if part.get_content_type() == 'text/plain':     # if link is in mail body then - 'text/html'
        body = part.get_payload(decode=True)
        print(body)
# b'This is perfect mailwith to cc and bcc. Thanks!\r\n'
# b indicates bytes string

########### 137. Final Capstone Project
########### Section 20: Advanced Python Objects and Data Structures
########### 138. Advanced Numbers

print(hex(12))      # 0xc
print(hex(512))     # 0x200
print(hex(-512))    # -0x200
# print(hex(-15.5))   # TypeError: 'float' object cannot be interpreted as an integer

print(bin(2))       # 0b10
print(bin(128))     # 0b10000000
print(bin(-128))    # -0b10000000
# print(bin(-15.5))   # TypeError: 'float' object cannot be interpreted as an integer

print(2**4)         # 16
print(pow(2, 4))    # 16

# pow(x, y, z) = (x**y)%z
print(pow(2, 3, 3))     # 2
print(pow(-2, 3, 3))    # 1
print(pow(2, 3, -3))    # -1
'''
r = a % b = a - (b * floor(a/b)) 
r = 8 - (-3 * floor(8/-3))
r = 8 - (-3 * floor(-2.666666666667))
r = 8 - (-3 * -3) # Rounded away from 0
r = 8 - 9
r = -1
'''

print(pow(27, 1/3))     # 3.0

print(abs(-3))      # 3
print(abs(3))       # 3

pi = 3.141592653589793
print(round(3.5))   # 4
print(round(2.5))   # 2
print(round(pi, 3))    # 3.142
print(round(pi, 5))     # 3.14159
print(round(pi, -1))    # 0.0

########### 139. Advanced Strings

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

########### 140. Advanced Sets

s = set()
s.add(1)
s.add(2)
print(s)    # {1, 2}
s.add(2)
print(s)    # {1, 2}    # as set has unique elements
s.clear()
print(s)    # set()
s = {1, 2, 3}
sc = s.copy()
print(sc)   # {1, 2, 3}

# now s and sc are 2 different objects and hence any changes to original / copy won't affect the
# other one
sc.add(4)
print(s)    # {1, 2, 3}
print(sc)   # {1, 2, 3, 4}

'''set A = {10, 20, 30, 40, 80}
set B = {100, 30, 80, 40, 60}

set A - set B = {10, 20}
set B - set A = {100, 60}

Explanation: A - B is equal to the elements present in A but not in B
             B - A is equal to the elements present in B but not in A'''
print(s.difference(sc))     # set()     # {}    # as all elements of s are in sc
print(sc.difference(s))     # {4}

s1 = {1, 2, 3}
s2 = {1, 4, 5}

'''
If A and B are two sets. The set difference() method will get the (A – B) and will return a new set. 
The set difference_update() method modifies the existing set. If (A – B) is performed, 
then A gets modified into (A – B), and if (B – A) is performed, then B gets modified into (B – A).
'''
print(s1.difference(s2))    # {2, 3}
s1.difference_update(s2)    # s1 = s1 - s2
print(s1)   # {2, 3}
print(s2)   # {1, 4, 5}

print(s)    # {1, 2, 3}
s.discard(3)
print(s)    # {1, 2}
s.discard(3)
print(s)    # {1, 2}

'''Intersection of two given sets is the largest set which contains all the elements that are common
to both the sets. Intersection of two given sets A and B is a set which consists of all the elements 
which are common to both A and B.'''
s1 = {1, 2, 3}
s2 = {1, 4, 5}
print(s1.intersection(s2))  # {1}

s1.intersection_update(s2)  # s1 = s1 intersect s2
print(s1)   # {1}

'''
Let set A = {2, 4, 5, 6}
and set B = {7, 8, 9, 10} 
set A and set B are said to be be disjoint sets as their
intersection is null. They do-not have any common elements in between them.
'''
s1 = {1, 2, 3}
s2 = {1, 4, 5}
s3 = {4, 5, 6}
print(s1.isdisjoint(s2))    # False # as they have common elements
print(s1.isdisjoint(s3))    # True # as don't have common elements

s1 = {1, 2, 3}
s2 = {1, 2}
s3 = {1, 2, 4}
print(s2.issubset(s1))    # True # as ALL elements of s2 are present in s1
print(s3.issubset(s1))    # False # as only some elements of s2 are present in s1
# superset is inverse of subset
print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # False

# symmetric_difference is inverse of intersection
s1 = {1, 2, 3}
s2 = {4, 2, 6}
print(s1.symmetric_difference(s2))  # {1, 3, 4, 6}
print(s2.symmetric_difference(s1))  # {1, 3, 4, 6}
s1.symmetric_difference_update(s2)   # s1 = s1 symmetric_difference s2
print(s1)   # {1, 3, 4, 6}

# Union - all elements in both sets
s1 = {1, 2, 3}
s2 = {4, 2, 6}
print(s1.union(s2))  # {1, 2, 3, 4, 6}
print(s2.union(s1))  # {1, 2, 3, 4, 6}
s1.update(s2)   # s1 = s1 union s2  # union update
print(s1)   # {1, 2, 3, 4, 6}

# set comprehension
d = {x * x for x in range(10)}
print(d)    # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(d))  # <class 'set'>

########### 141. Advanced Dictionaries

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

########### 142. Advanced Lists

mylist = [1, 2, 3, 2]
print(mylist)

print(mylist.count(2))  # 2

# appending element -
print(mylist.append(4))     # None
print(mylist)   # [1, 2, 3, 2, 4]

# appending list - incorrect way -
mylist.append([3, 5])
print(mylist)   # [1, 2, 3, 2, [3, 5]]

# appending list - correct way -
mylist = [1, 2, 3, 2]
mylist = mylist + [3, 5]
print(mylist)   # [1, 2, 3, 2, 3, 5]

# OR appending list - another correct way -
mylist = [1, 2, 3, 2]
mylist.extend([3, 5])
print(mylist)   # [1, 2, 3, 2, 3, 5]

print(mylist.index(2))  # 1 # 1st successful hit

mylist.insert(3, 'insert me')
print(mylist)   # [1, 2, 3, 'insert me', 2, 3, 5]

mylist.pop()    # by default last element will be popped
print(mylist)

popped = mylist.pop(3)
print(popped)   # insert me
print(mylist)   # [1, 2, 3, 2, 3]

mylist.remove(2)    # only removes 1st successful hit
print(mylist)   # [1, 3, 2, 3]

# Below will affect original list
mylist.reverse()
print(mylist)    # [3, 2, 3, 1]
mylist.sort()
print(mylist)    # [1, 2, 3, 3]

mylist = [1, 3, 2, 3]
print(sorted(mylist))   # [1, 2, 3, 3]
print(mylist)   # [1, 3, 2, 3]

########### 143. Advanced Python Objects Assessment Test

# Problem 1: Convert 1024 to binary and hexadecimal representation
print(bin(1024))  # 0b10000000000
print(hex(1024))  # 0x400

# Problem 2: Round 5.23222 to two decimal places
print(round(5.23222, 2))  # 5.23

# Problem 3: Check if every letter in the string s is lower case
s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())  # False

# Problem 4: How many times does the letter 'w' show up in the string below?
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))  # 12

# Problem 5: Find the elements in set1 that are not in set2:
set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}
print(set1.difference(set2))  # {2}

# Problem 6: Find all elements that are in either set:
print(set1.union(set2))  # {1, 2, 3, 5, 6, 7, 8}

# Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary
# comprehension.
print({x: x ** 3 for x in range(5)})  # {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# Problem 8: Reverse the list below:
list1 = [1, 2, 3, 4]
list1.reverse()
print(list1)  # [4, 3, 2, 1]

# Problem 9: Sort the list below:
list2 = [3, 4, 2, 5, 1]
list2.sort()
print(list2)    # [1, 2, 3, 4, 5]

########### Zipper

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
