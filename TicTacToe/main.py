#Two player game finished

import os #used to clear screen

board = ['-','-','-',
        '-','-','-',
        '-','-','-'] #empty game baord

def display_board():
    os.system('clear')#used to clear the screen when drawing a new board
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def isValidMove(pos):
    try:
        if (int(pos) > 9 or int(pos) < 1):
            print("Number not allowed (Too Big/Small)")
            return False
        elif (board[int(pos)-1] != '-'):
            print("Space already taken, try again!")
            return False
        else:
            return True
    except:
        print("Invalid input! Try again!")

def handle_turn(player):
    while True:
        position = input("Choose a position from 1-9: ")
        if(player): #Will alternate players based on the state of the boolean 'player'
            if(isValidMove(position)):
                board[int(position)-1] = 'X'
                break
        else:
            if(isValidMove(position)):
                board[int(position)-1] = 'O'
                break

    
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
        display_board() #print the board at the start of each turn
        handle_turn(player)
        player = not player # move to next persons turn
        game_over = check_win() #determines if we need to exit the loop



play_game()