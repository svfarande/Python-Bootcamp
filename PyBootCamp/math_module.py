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
