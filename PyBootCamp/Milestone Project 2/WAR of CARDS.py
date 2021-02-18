import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


# CARD CLASS
# SUIT, RANK, VALUE

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


'''
mycard1 = Card('Hearts', 'King')
print("My card is " + str(mycard1))
print(mycard1.rank + " of " + mycard1.suit + " has value - " + str(mycard1.value))
'''


# DECK CLASS
# HOLDING CARDS IN LIST

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                t_card = Card(suit, rank)
                self.all_cards.append(t_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


'''
mydeck = Deck()
for i_card in mydeck.all_cards:
    print("Card " + str(i_card) + " has value of " + str(i_card.value))
mydeck.shuffle()
print("After Shuffle - ")
for i_card in mydeck.all_cards:
    print("Card " + str(i_card) + " has value of " + str(i_card.value))
print(len(mydeck.all_cards))
print(mydeck.deal_one())
print(len(mydeck.all_cards))
'''


# CLASS PLAYER
# NAME, CARDS


class Player:

    def __init__(self, name):
        self.name = name
        self.point = 0
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, type([])):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} card(s) with {self.point} point(s)."


'''
mydeck = Deck()
mydeck.shuffle()
player1 = Player("Shubham")
card1 = mydeck.deal_one()
print(card1)
card2 = mydeck.deal_one()
print(card2)
card3 = mydeck.deal_one()
print(card3)
player1.add_cards(card1)
print(player1)
print(player1.all_cards[0])
player1.add_cards([card2, card3])
print(player1)
print(player1.all_cards[0])
print(player1.all_cards[1])
print(player1.all_cards[2])
'''

print("\n\n*********!!! WELCOME TO WAR OF CARDS !!!*********\n")
print('Rules - \n'
      '1. Player must have name to play the game.\n'
      '2. Answer the questions correctly in order to WIN the game.\n'
      '3. TIE will be settled based on no. of cards you hold, the more the better.\n'
      '4. Select the no. of deals on WAR between 5 and 20.\n'
      '   Make sure to keep it max in order to finish the game quickly.\n')

nod = 1  # no. of deals

while nod < 5 or nod > 20:
    try:
        nod = int(input("Enter the no. of deals on WAR between 5 and 20 - "))
    except ValueError:
        print("It should be integer.")

name1 = name2 = ""

while len(name1) == 0 or len(name2) == 0:
    name1 = input("Enter Player1 name - ")
    name2 = input("Enter Player2 name - ")

player1 = Player(name1)
player2 = Player(name2)

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player1.all_cards.append(new_deck.deal_one())
    player2.all_cards.append(new_deck.deal_one())

game_on = True
flag = random.choices([True, False])[0]
Round = 0

while game_on:
    Round += 1
    print(f"\n********************************\nRound - {Round}")

    player1_cards = []
    player2_cards = []

    if len(player1.all_cards) == 0 or len(player2.all_cards) == 0:
        game_on = False
        at_war = False
    else:
        player1_cards = [player1.remove_one()]
        player2_cards = [player2.remove_one()]
        at_war = True

    while at_war:

        print(f"\nPlayer1 - {player1.name} has drawn : {player1_cards[-1]}\n"
              f"Player2 - {player2.name} has drawn : {player2_cards[-1]}")

        if flag:
            print(f"\nQuestion to Player1 - {player1.name} : Who will win this Round or is it a "
                  f"WAR ?")
            ans = input("Enter 1 for Player1, 2 for Player2, W for WAR - ")
            flag = False
        else:
            print(f"\nQuestion to Player2 - {player2.name} : Who will win this Round or is it a "
                  f"WAR ?")
            ans = input("Enter 1 for Player1, 2 for Player2, W for WAR - ")
            flag = True

        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            actual = "1"
            at_war = False
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player2_cards)
            player2.add_cards(player1_cards)
            actual = "2"
            at_war = False
        else:
            actual = "W"
            if len(player1.all_cards) < nod or len(player2.all_cards) < nod:
                game_on = at_war = False

            if len(player1.all_cards) > nod and len(player2.all_cards) > nod:
                for i in range(nod):
                    player1_cards.append(player1.remove_one())
                    player2_cards.append(player2.remove_one())

        if not flag:
            if actual == ans:
                player1.point += 1
            else:
                player2.point += 1
        else:
            if actual == ans:
                player2.point += 1
            else:
                player1.point += 1

    print(f"\nResults of Round - {Round} are : \nPlayer1 - {player1}\nPlayer2 - {player2}")

    if (not game_on) and player1.point < player2.point:
        print(f"\n################################\n"
              f"GAME OVER for Player1 - {player1.name}\n"
              f"Player2 - {player2.name} is VICTOR as he has more points !!!")
    elif (not game_on) and player1.point > player2.point:
        print(f"\n################################\n"
              f"GAME OVER for Player2 - {player2.name}\n"
              f"Player1 - {player1.name} is VICTOR as he has more points !!!")
    elif (not game_on) and len(player1.all_cards) < len(player2.all_cards):
        print(f"\n################################\n"
              f"GAME OVER for Player1 - {player1.name} , don't have enough cards\n"
              f"Player2 - {player2.name} is VICTOR !!!")
    elif not game_on:
        print(f"\n################################\n"
              f"GAME OVER for Player2 - {player2.name} , don't have enough cards\n"
              f"Player1 - {player1.name} is VICTOR !!!")
