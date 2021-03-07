import pdb  # py debugger

x = 2
y = 3
z = [3, 5, 7]

result1 = x + y
pdb.set_trace()
result2 = z + x

'''

Output -

> c:\users\svfarande\onedrive\documents\study material\python\pycharm projects\udemy\py_debugger.py(9)<module>()
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
> c:\users\svfarande\onedrive\documents\study material\python\pycharm projects\udemy\py_debugger.py(9)<module>()
-> result2 = z + x
(Pdb) n
--Return--
> c:\users\svfarande\onedrive\documents\study material\python\pycharm projects\udemy\py_debugger.py(9)<module>()->None
-> result2 = z + x
(Pdb) n
--Call--
Traceback (most recent call last):
  File "C:/Users/svfarande/onedrive/Documents/Study MAterial/Python/PyCharm Projects/PyBootCamp/py_debugger.py", line 9, in <module>
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(309)__init__()
-> def __init__(self, errors='strict'):
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(310)__init__()
-> IncrementalDecoder.__init__(self, errors)
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(312)__init__()
-> self.buffer = b""
(Pdb) n
--Return--
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(312)__init__()->None
-> self.buffer = b""
(Pdb) n
--Call--
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(331)getstate()
-> def getstate(self):
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(333)getstate()
-> return (self.buffer, 0)
(Pdb) n
--Return--
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(333)getstate()->(b'', 0)
-> return (self.buffer, 0)
(Pdb) n
--Call--
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(319)decode()
-> def decode(self, input, final=False):
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(321)decode()
-> data = self.buffer + input
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(322)decode()
-> (result, consumed) = self._buffer_decode(data, self.errors, final)
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(324)decode()
-> self.buffer = data[consumed:]
(Pdb) n
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(325)decode()
-> return result
(Pdb) n
--Return--
> c:\users\svfarande\appdata\local\programs\python\python38-32\lib\codecs.py(325)decode()->
'import pdb  ...2 = z + x\r\n'
-> return result
(Pdb) n
    result2 = z + x
TypeError: can only concatenate list (not "int") to list

'''