rules = '''First one to get three in a row wins
The bottom left corner is 1, to the right is 2, etc..
4 is the position above 1, 5 is right of 4, etc...'''


board = ['x', '', '', '', '', '', '', '', '', '',]
def draw_board(board):
    print('   |   |')
    print('  ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('  ' + board[4] + ' | ' + board[5] + '  | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('  ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('   |   |')

def intialize():
    print 'Start game? (Yes or No)'
    start = raw_input()
    print 'X goes first'
    print rules
    if start[0] == 'y' or start[0] == 'Y':
        print draw_board(board)
        player_action(win_check)
    if start[0] == 'n' or start[0] == 'N':
        quit()

def play_again():
    user_response = raw_input()
    if user_response == 'Y' or user_response == 'y':
        for i in range(1, len(board)):
            board[i] = ''
        board[0] = 'x'
        intialize()
    else:
        quit()


def win_check():
    if (board[1] == 'x' and board [2] == 'x' and board [3] == 'x') or (board[1] == 'y' and board [2] == 'y' and board [3] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[4] == 'x' and board [5] == 'x' and board [6] == 'x') or (board[4] == 'y' and board [5] == 'y' and board [6] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[7] == 'x' and board [8] == 'x' and board [9] == 'x') or (board[7] == 'y' and board [8] == 'y' and board [9] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[1] == 'x' and board [5] == 'x' and board [9] == 'x') or (board[1] == 'y' and board [5] == 'y' and board [9] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[7] == 'x' and board [5] == 'x' and board [3] == 'x') or (board[7] == 'y' and board [5] == 'y' and board [3] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[1] == 'x' and board [4] == 'x' and board [7] == 'x') or (board[1] == 'y' and board [4] == 'y' and board [7] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[2] == 'x' and board [5] == 'x' and board [8] == 'x') or (board[2] == 'y' and board [5] == 'y' and board [8] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()
    if (board[3] == 'x' and board [6] == 'x' and board [9] == 'x') or (board[3] == 'y' and board [6] == 'y' and board [9] == 'y'):
        print 'Game over!'
        print 'Play again? (Y/N)'
        play_again()


def player_action(win_check):
    while True:
        turn = board[0]
        print 'It is ' + turn + ' turn'
        print 'Which coordinate?'
        turn_coordinate = int(raw_input())
        if board[turn_coordinate] == '':
            board[turn_coordinate] = turn
            print draw_board(board)
            win_check()
        else:
            print 'Invalid coordinate, try again'
        if board[turn_coordinate] == 'x':
            board[0] = 'y'
        if board[turn_coordinate] == 'y':
            board[0] = 'x'




intialize()
