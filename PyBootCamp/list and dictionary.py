mylist = ['Shubham', 'Vasant', 'Farande', 6, 12, 1996, 75.9]
print(mylist)  # ['Shubham', 'Vasant', 'Farande', 6, 12, 1996, 75.9]
nlist = ['3', '4.5', '1', '-36']
print(nlist)  # ['3', '4.5', '1', '-36']
print(nlist.sort())  # None
print(nlist)  # ['-36', '1', '3', '4.5']
nlist = ['3', '4.5', '1', ['67', 'Shubham', '7.6'], '-36']
print(nlist)  # ['3', '4.5', '1', ['67', 'Shubham', '7.6'], '-36']
print(nlist[::-1])
newlist = mylist + nlist
newlist[1] = "V."
print(newlist)  # ['Shubham', 'V.', 'Farande', 6, 12, 1996, 75.9, '3', '4.5', '1', ['67', 'Shubham', '7.6'], '-36']

mydict = {"key": 'value', 'Shubham': "Farande"}
print(mydict)  # {'key': 'value', 'Shubham': 'Farande'}
print(mydict['Shubham'])  # Farande

cmpxdict = {'keys': 'values', 'list': [34, 'Shubham', 4.5], 'dict': {5.5: 'five chips five', 'five': 5}}
print(cmpxdict)  # {'keys': 'values', 'list': [34, 'Shubham', 4.5], 'dict': {5.5: 'five chips five', 'five': 5}}

print(cmpxdict['list'][1][::-1].upper())  # MAHBUHS
print(cmpxdict['dict'][5.5])  # five chips five

cmpxdict['list'][1] = "Hi"
cmpxdict['dict'][6] = 'Six'
cmpxdict['Six'] = 6
print(cmpxdict)  # {'keys': 'values', 'list': [34, 'Hi', 4.5], 'dict': {5.5: 'five chips five', 'five': 5,
# 6: 'Six'}, 'Six': 6}

# newdict = mydict + cmpxdict
# print(newdict) # unsupported operand type(s) for +: 'dict' and 'dict'

print(cmpxdict.keys())  # dict_keys(['keys', 'list', 'dict', 'Six'])
print(cmpxdict.values())  # dict_values(['values', [34, 'Hi', 4.5], {5.5: 'five chips five', 'five': 5, 6: 'Six'}, 6])
print(cmpxdict.items())  # dict_items([('keys', 'values'), ('list', [34, 'Hi', 4.5]), ('dict', {5.5: 'five chips
# five', 'five': 5, 6: 'Six'}), ('Six', 6)])

# Note below overwrite of value when same key is used
dictionary = {"key1": "value2", "key2": "value2", "key1": "value1"}
print(dictionary)   # {'key1': 'value1', 'key2': 'value2'}
