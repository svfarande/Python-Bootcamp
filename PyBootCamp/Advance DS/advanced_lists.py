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
