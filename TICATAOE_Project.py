def display_board(board):
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("---------------")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("---------------")
    print(board[7]+" | "+board[8]+" | "+board[9])
    
def player_input():
    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player1:choose X or O: ').upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
    
def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark)or
    (board[4]==board[5]==board[6]==mark)or
    (board[7]==board[8]==board[9]==mark)or
    (board[1]==board[4]==board[7]==mark)or
    (board[2]==board[5]==board[8]==mark)or
    (board[3]==board[6]==board[9]==mark)or
    (board[1]==board[5]==board[9]==mark)or
    (board[3]==board[5]==board[7]==mark))    
    
    
import random

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "Player1"
    else:
        return "Player2"

def space_check(board, position):
    return board[position]==" "

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position(1-9):  '))
        
    return position

def replay():
    choice= input("Play again?: Y or N:")
    return choice=='Y'

print("Welcome to Shravan's  Tic Tac Toe" )
while True:
    ticboard = [' ']*10
    Player1_marker , Player2_marker = player_input()
    turn=choose_first()
    print(turn+'will go first')
    
    play_game=input('Ready to Play: Yes or No')
    if play_game=='Yes':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        
        if turn=='Player1':
            display_board(ticboard)
            position=player_choice(ticboard)
            place_marker(ticboard,Player1_marker,position)
            
            if win_check(ticboard,Player1_marker):
                display_board(ticboard)
                print("Player1 Has WON!!")
                game_on= False
            else:
                if full_check(ticboard):
                    display_board(ticboard)
                    print("Game is TIE")
                    game_on= False
                else:
                    turn='Player2'
                
        
        else:
            display_board(ticboard)
            position=player_choice(ticboard)
            place_marker(ticboard,Player2_marker,position)
            if win_check(ticboard,Player2_marker):
                display_board(ticboard)
                print("Player2 Has WON!!")
                game_on= False
            else:
                if full_check(ticboard):
                    display_board(ticboard)
                    print("Game is TIE")
                    game_on= False
                else:
                    turn='Player1'
            
        
        
    if not replay():
        break