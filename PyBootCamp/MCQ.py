# ROUND() BEHAVIOUR
# prefers even number if value to be rounded off can be increased & decreased (.5 numbers)
print(round(5.5))   # 6
print(round(4.5))   # 4
print(round(3.5))   # 4 ****
print(round(2.6))   # 3
print(round(2.5))   # 2 ****
print(round(2.4))   # 2
print(round(1.6))   # 2
print(round(1.5))   # 2
print(round(1.4))   # 1
print(round(0.6))   # 1
print(round(0.5))   # 0
print(round(0.4))   # 0

print(round(-5.5))  # -6
print(round(-4.5))  # -4
print(round(-3.5))  # -4 ****
print(round(-2.6))  # -3
print(round(-2.5))  # -2 ****
print(round(-2.4))  # -2
print(round(-1.6))  # -2
print(round(-1.5))  # -2
print(round(-1.4))  # -1
print(round(-0.6))  # -1
print(round(-0.5))  # 0
print(round(-0.4))  # 0

print(11 % 3)   # 2
print(-11 % 3)  # 1
print(11 % -3)  # -1

'''
r = a % b = a - (b * floor(a/b))
r = 8 - (-3 * floor(8/-3))
r = 8 - (-3 * floor(-2.666666666667))
r = 8 - (-3 * -3) # Rounded away from 0
r = 8 - 9
r = -1
'''

print(-16 // 3)     # -6
print(-11 // 3)     # -4
print(8.0 == 8)     # True

print("dog" in "My dog is great")   # True

print(type(range(1, 5)))    # <class 'range'>
print(range(1, 5))  # range(1, 5)
