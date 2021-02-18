mystr = "Shubham"
print(len(mystr))

print(mystr[::-1])
print("Shubham"[::-1])

mystr = mystr[:3] + "B" + mystr[4:]
print(mystr)

letter = "S"
print(letter * 5)

mystr = "Shubham Farande"
print(mystr.split("a"))

print('%f' % (0.1 + 0.2 - 0.3))

print("Answer is {s:}".format(s=100 / 777))  # Answer is 0.1287001287001287
print("Answer is {s:.2}".format(s=100 / 777))  # Answer is 0.13
print("Answer is {s:10}".format(s=100 / 777))  # Answer is 0.1287001287001287
print("Answer is {s:10.0}".format(s=100 / 777))  # Answer is        0.1
print("Answer is {s:10.1}".format(s=100 / 777))  # Answer is        0.1
print("Answer is {s:10.2}".format(s=100 / 777))  # Answer is       0.13
print("Answer is {s:10.3}".format(s=100 / 777))  # Answer is      0.129

mystr = "aa"
print(f"My name is {mystr}.")
