def display_instructions():
    print("\n\nWELCOME TO TIC TAC TOE !!!\nPlease read instructions on how to play - ")
    print("\nYour board will be as below and you have to enter choice from 1 to 9 in order to "
          "give input for specific position. Note the numbers are mapped to NUM PAD on keyboard.")
    display_board([['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']])
    print("Once input given can't be changed.\nPlayer 1 (X) will play 1st and then Player 2 (O)"
          " alternate until a player wins or match is a tie\n")


def take_name():
    return [input("Enter Player 1 (X) name : "), input("Enter Player 2 (O) name : ")]


def display_board(choices):
    print("\n")
    for i in range(0, 3):
        print(choices[i])
    print("\n")


def get_input(occupied_choices, name, s, board):
    mark = 'O'
    if s == 0:
        mark = 'X'

    while True:
        try:
            number = int(input(name + " : Enter your number for '" + mark + "' - "))
        except ValueError:
            print("Please enter integer only")
            display_board(board)
            continue

        if number not in range(1, 10):
            print(name + " : " + str(number) + " is not from 1 to 9. Please enter correct number.")
            display_board(board)
            continue

        if number in occupied_choices:
            print(name + " : " + str(number) +
                  " position is already occupied. Please enter correct number.")
            display_board(board)
            continue
        else:
            occupied_choices.append(number)
            break

    return occupied_choices


def update_board(board, occupied_choices, s):
    replace = occupied_choices[len(occupied_choices) - 1]

    mark = 'O'
    if s == 0:
        mark = 'X'

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == 'X' or board[i][j] == 'O':
                continue
            if replace == int(board[i][j]):
                board[i][j] = mark
    return board


def check_win(board):
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] or board[0][i] == board[1][i] == board[2][i]:
            return True

    if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]:
        return True

    return False


def game(players):
    board = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]
    display_board(board)
    occupied_choices = []
    s = 0

    for i in range(1, 10):
        occupied_choices = get_input(occupied_choices, players[s], s, board)
        board = update_board(board, occupied_choices, s)

        if check_win(board):
            print("Congratulations!! " + players[s] + " is winner.")
            display_board(board)
            break

        display_board(board)

        if s == 0:
            s = 1
        else:
            s = 0

        if i == 9:
            print("Match is a Tie. Please play again")


def begin():
    display_instructions()
    game(take_name())


begin()
print("Game Over!")
