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
