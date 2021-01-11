

#Things we need to complete

    # Draw board
    # play game
    # check win
    # Check tie
    # Flip board


board = ['-','-','-',
        '-','-','-',
        '-','-','-'] #empty game baord

def display_board():
    #find cleaner way to write
    #gui
    #impliment horozontal bars
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    if(player):
        board[int(position) - 1] = 'X'
    else:
        board[int(position) -1 ] = 'O'
    
def check_col():
    #find better way to do this
    if(((board[0] == board[3] == board[6])) and board[0] != '-'):
        display_board()
        print(board[0] + "'s won the game!")
        return True
    if((board[1] == board[4] == board[7])and board[1] != '-'):
        display_board()
        print(board[1] + "'s won the game!")
        return True
    if((board[2] == board[5] == board[8]) and board[2] != '-'):
        display_board()
        print(board[2] + "'s won the game!")
        return True
    return False

def check_row():
    #find better way to do this
    if(board[0] == board[1] == board[2] != '-'):
        display_board()
        print(board[0] + "'s won the game!")
        return True
    if(board[3] == board[4] == board[5] != '-'):
        display_board()
        print(board[3] + "'s won the game!")
        return True
    if(board[6] == board[7] == board[8] != '-'):
        display_board()
        print(board[6] + "'s won the game!")
        return True
    return False

def check_diag():
    if(board[0] == board[4] == board[8] != '-'):
        display_board()
        print(board[0] + "'s won the game!")
        return True
    if(board[3] == board[4] == board[6]!= '-'):
        display_board()
        print(board[3] + "'s won the game!")
        return True
    return False

def check_tie():
    for i in board:
        if(i == '-'):
            return False
    
    display_board()
    print("Tie game!")
    return True

def check_win():
    return check_diag() or check_col() or check_row() or check_tie()


def play_game():
    game_over = False
    player = True #true players are X, false are O's
    while(not game_over):
        display_board()
        handle_turn(player)
        player = not player #move to next persons turn
        game_over = check_win()




play_game()