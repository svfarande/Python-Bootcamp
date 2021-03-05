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
