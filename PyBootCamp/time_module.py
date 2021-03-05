import time
import timeit


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
