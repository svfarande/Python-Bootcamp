import os
import shutil

f = open('practice.txt', 'w+')
f.write('This is a test text')
f.close()

udemy_path = '/'

# os.listdir("Path\\of\\Directory")
print(f"Contents in '{os.getcwd()}' are - {os.listdir()}")
# Contents in 'C:\Users\A711929\OneDrive - Atos\Documents\Study MAterial\Python\PyCharm Projects\
# PyBootCamp\OS and Shutil' are -
# ['Delete', 'move.html', 'os_and_shutil.py', 'practice.txt', 'Root', 'SubDir']

print(os.listdir(udemy_path + "\\Milestone Project 2"))
# ['BLACKJACK.py', 'BLACKJACK_share.py', 'WAR of CARDS.py']

'''
shutil.move('source\\path', 'destination\\path')
if file with same name is already there then
shutil.Error: "Destination path '%s' already exists" is raised
'''

print(f"Before Move contents in CWD - {os.listdir(os.getcwd())}")
# Before Move contents in CWD -
# ['Delete', 'move.html', 'os_and_shutil.py', 'practice.txt', 'Root', 'SubDir']

shutil.move('move.html', udemy_path + '\\OS and Shutil\\SubDir')

print(f"After Move contents in CWD - {os.listdir(os.getcwd())}")
# After Move contents in CWD - ['Delete', 'os_and_shutil.py', 'practice.txt', 'Root', 'SubDir']

print("After Move contents in SubDir - ", end='')
print(os.listdir(os.getcwd() + '\\SubDir'))
# After Move contents in SubDir - ['move.html']

print('move.html is moved back to its original location - ')

print(shutil.move(udemy_path + '\\OS and Shutil\\SubDir\\move.html', os.getcwd()))
# C:\Users\A711929\OneDrive - Atos\Documents\Study MAterial\Python\
# PyCharm Projects\PyBootCamp\OS and Shutil\move.html

'''
Deleting Files

NOTE: The os module provides 3 methods for deleting files:
1) os.unlink(path) which deletes a file at the path your provide
2) os.rmdir(path) which deletes a root (root must be empty) at the path your provide
3) shutil.rmtree(path) this is the most dangerous, as it will remove all files and folders 
contained in the path. 

All of these methods can NOT be reversed! Which means if you make a 
mistake you won't be able to recover the file. Instead we will use the send2trash module. 
A safer alternative that sends deleted files to the trash bin instead of permanent removal.
'''

'''
Send2Trash
import send2trash

print("Before Delete contents in Delete - ", end='')
print(os.listdir(os.getcwd() + "\\Delete"))
# Before Delete contents in Delete - ['delete.html']

send2trash.send2trash(os.getcwd() + '\\Delete\\delete.html')

print("After Delete contents in Delete - ", end='')
print(os.listdir(os.getcwd() + "\\Delete"))
# After Delete contents in Delete - []

print(f"Before Delete contents in CWD - {os.listdir(os.getcwd())}")
# Before Delete contents in CWD - ['Delete', 'move.html', 'os_and_shutil.py', 'practice.txt',
# 'SubDir']

send2trash.send2trash(os.getcwd() + '\\Delete')

print(f"After Delete contents in CWD - {os.listdir(os.getcwd())}")
# After Delete contents in CWD - ['move.html', 'os_and_shutil.py', 'practice.txt', 'SubDir']
'''

print(os.walk(os.getcwd()))  # <generator object walk at 0x01C0B6B8>

for root, folders, files in os.walk(os.getcwd() + "\\Root"):

    print(f"-------------------------------------------------------------------\n"
          f"Currently looking at Folder - {root}")
    print('\nThe Subfolders are - ')

    for sf in folders:
        print(f"\tSubfolder - {sf}")

    print("\nThe Files are - ")

    for f in files:
        print(f"\tFile - {f}")

    print('-------------------------------------------------------------------\n')

    # OR

    '''
    print(root)     # Path of root
    print(folders)  # list
    print(files)    # list
    '''
