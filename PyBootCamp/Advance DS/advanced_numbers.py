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
