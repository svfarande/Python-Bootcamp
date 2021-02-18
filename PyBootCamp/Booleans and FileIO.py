true = True
print(str(true) + " - " + str(type(true)))  # True - <class 'bool'>

false = False
print(str(false) + " - " + str(type(false)))  # False - <class 'bool'>

print(1 > 2)  # False
print(1 == 1)  # True

'''a variable declared must be defined immediately at least with None
none #error - name 'none' is not defined'''
none = None
print(str(none) + " - " + str(type(none)))  # None - <class 'NoneType'>

'''Contents of text.txt before performing file operations. text.txt - 
Hello There
This is 1st line.
This is 2nd line.
This is 3rd line.
'''

myfile = open('text.txt')  # same as open('text.txt', mode='r') or same as open('text.txt', 'r')
print(myfile.read())  # outputs all the contents of file
print(myfile.read())  # will print blank line because cursor was placed at end because of previous print statement
print(myfile.seek(11))  # will output index given in seek() and place cursor to that index of file (note at 11 index there is '\n' of 1st line)
print(myfile.read())  # outputs all the contents of file starting from the index in seek()
myfile.seek(0)
print(myfile.readlines())  # outputs each line in list format
myfile.close()  # close the file, if you don't do this and try to delete the file it will give error python is using it

# using below with statement you need not to close the file manually, it will close immediately after block ends

with open('C:\\Users\\SF5048275\\OneDrive - Atos\\Documents\\Study MAterial\\Python\\PyCharm Projects\\PyBootCamp\\text.txt', mode='r') as myfile:  # by default mode is 'r'
    contents = myfile.read()
    print(contents)

# also remember with specific mode you can only use functions for that mode for ex. with mode='w' you can't use read()

'''
'r' is read only
'w' is write only (will always overwrite or create new file)
'a' is append only (if file don't exists it will create and append content to that file)
'r+' is reading and writing
'w+' is writing and reading
> Opening a file with 'w' or 'w+' truncates the original, meaning that anything that was in the original file is deleted!'''

with open('text.txt', mode='w+') as myfile:
    print(myfile.read())  # contents of text.txt are now vanished as mode='w+'

with open('text.txt', mode='w') as myfile:
    myfile.write("Shubham")     # Shubham is in now in text.txt

with open('text.txt', mode='a') as myfile:
    myfile.write("\n"+contents)

'''Contents of text.txt before performing file operations. text.txt - 
Shubham
Hello There
This is 1st line.
This is 2nd line.
This is 3rd line.
'''