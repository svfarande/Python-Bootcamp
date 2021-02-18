from random import shuffle


def shuffle_(mylist):
    shuffle(mylist)
    return mylist


def guess():
    no = ""
    while no not in ["0", "1", "2"]:
        no = input("Pick a guess 0 , 1 or 2 : ")
    return int(no)


def check(mylist, place):
    if mylist[place] == 'O':
        print("Correct Guess !")
        print(mylist)
    else:
        print("Wrong Guess !")
        print(mylist)


mylist = [' ', 'O', ' ']
mylist = shuffle_(mylist)
place = guess()
check(mylist, place)
