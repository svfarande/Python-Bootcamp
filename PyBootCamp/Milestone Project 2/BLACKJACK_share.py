import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# CARD CLASS
# SUIT, RANK

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.rank + " of " + self.suit
'''
mycard1 = Card('Hearts', 'King')
print("My card is " + str(mycard1))
print(mycard1.rank + " of " + mycard1.suit + " has value - " + str(values[mycard1.rank]))
'''


# DECK CLASS
# HOLDING CARDS IN LIST

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                t_card = Card(suit, rank)
                self.deck.append(t_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

    def __str__(self):
        cards = ''
        for i in self.deck:
            cards = cards + '\n' + i.__str__()
        return "The deck has following cards - " + cards


'''
mydeck = Deck()
print(mydeck)
print("\nAfter Shuffle - ")
mydeck.shuffle()
print(mydeck)
print(len(mydeck.deck))
print(mydeck.deal())
print(len(mydeck.deck))
'''


# CLASS HAND
# CARDS ON TABLE, VALUE & ACES

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
'''
    def __repr__(self):
        str_cards = ''
        length = len(self.cards)
        c = 0
        for i in self.cards:
            if c:
                str_cards = i.__str__() + ' , ' + str_cards
            else:
                str_cards = i.__str__()
                c = c + 1
        return "[" + str_cards + "]"
    '''

'''
player = Hand()
mydeck = Deck()
mydeck.shuffle()
player.add_card(mydeck.deal())
print(player.value)
print(player.cards[0])
'''


# CLASS CHIPS
# TOTAL, BET


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f"\nAs of now you have {chips.total} chips. "
                                  f"Enter the chips (in integer) you want to bet - "))
            if chips.bet > chips.total or chips.bet < 1:
                print(f"That's not good value. Try again!!!")
                continue
            break
        except ValueError:
            print("Please enter only INTEGER. Try again!")

    return chips.bet


def hit(mydeck, hand):
    hand.add_card(mydeck.deal())
    hand.adjust_for_ace()


def hit_or_stand(mydeck, hand):
    global playing

    while True:
        ch = input("\nDo you want to HIT or STAND ? Enter h or s accordingly - ")
        if ch[0].lower() == 'h':
            hit(mydeck, hand)
        elif ch[0].lower() == 's':
            print("\nPlayer stand. Dealer's Turn.")
            playing = False
        else:
            print("Please enter only h (for HIT) or s (for STAND).")
            continue
        break


def show_some(player, dealer):
    print(f"\nDealer's Hand : [<card hidden> , {dealer.cards[1]}]")
    print(f"Player's Hand : {player.cards}")


def show_all(player, dealer):
    print(f"Dealer's Hand : {dealer.cards}")
    print(f"Player's Hand : {player.cards}")


def player_busts(chips):
    print("\nPLAYER BUSTS!")
    chips.lose_bet()


def player_wins(chips):
    print("\nPLAYER WINS!")
    chips.win_bet()


def dealer_busts(chips):
    print("\nDEALER BUSTS! PLAYER WINS!")
    chips.win_bet()


def dealer_wins(chips):
    print("\nDEALER WINS!")
    chips.lose_bet()


def push():
    print("\nDealer and Player TIE! PUSH")


print("\n\n*********!!! WELCOME TO BLACKJACK !!!*********")

player_chips = Chips()

while True:

    deck = Deck()
    deck.shuffle()

    player_Hand = Hand()
    player_Hand.add_card(deck.deal())
    player_Hand.add_card(deck.deal())

    dealer_Hand = Hand()
    dealer_Hand.add_card(deck.deal())
    dealer_Hand.add_card(deck.deal())

    take_bet(player_chips)
    show_some(player_Hand, dealer_Hand)

    while playing:

        hit_or_stand(deck, player_Hand)

        show_some(player_Hand, dealer_Hand)

        if player_Hand.value > 21:
            player_busts(player_chips)
            break

    if player_Hand.value <= 21:

        while dealer_Hand.value < 17:
            print("\nDealer want to HIT!")
            hit(deck, dealer_Hand)
        else:
            print("\nDealer STANDS!")

        show_all(player_Hand, dealer_Hand)

        if dealer_Hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_Hand.value > player_Hand.value:
            dealer_wins(player_chips)
        elif dealer_Hand.value < player_Hand.value:
            player_wins(player_chips)
        else:
            push()
    print("\nRESULTS : ")
    show_all(player_Hand, dealer_Hand)
    print(f"Player's Value : {player_Hand.value}\nDealer's Value : {dealer_Hand.value}")
    print(f"Player total chips are : {player_chips.total}")

    new_game = input("\nDo you want to play again ? If yes enter y - ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\n\nThanks! for playing. Have a great day!")
        break
