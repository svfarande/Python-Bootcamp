loc = "Bank"
if loc == "Auto Shop":
    print("Cars")
elif loc == "Bank":
    print("Money")
elif loc == "Gym":
    print("Fitness")
else:
    print("Don't know")

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
