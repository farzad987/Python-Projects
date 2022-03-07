#Printing out the board
def display_board(board):
    print("\n"*15)
    print(board[7],"|",board[8],"|",board[9])
    print("---------")
    print(board[4],"|",board[5],"|",board[6])
    print("---------")
    print(board[1],"|",board[2],"|",board[3])

#Recieving input
def user_input():
    marker=" "
    while marker!="X" and marker!="O":
        marker=input("Player 1, Choose X or O: ").upper()

    if marker=="X":
        return ("X","O")
    else:
        return("O","X")
    
    
#Puting value in Place
def place_marker(board,marker,position):
    board[position]=marker

#WIN
    #HORIZONTAL
def win_check(board,mark):    
    if board[1]==board[2]==board[3]==mark or board[4]==board[5]==board[6]==mark or board[7]==board[8]==board[9]==mark:
        return True
    #VERTICAL
    elif board[1]==board[4]==board[7]==mark or board[2]==board[5]==board[8]==mark or board[3]==board[6]==board[9]==mark:
        return True
    #DIAGONAL
    elif board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark:
        return True
    else:
        return False

#RANDOM FIRST PLAYER
import random
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "Player 1"
    else:
        return "Player 2"

#SPACE AVAILABLE OR NO
def space_check(board,position):
    return board[position]==" "

#BOARD FULL OR NO2

def board_full(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    

#NEXT MOVE
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Choose a number between 1-9: "))
    
    return position    

#Play Again or No?
def replay():
    choice=input("Do you want to play again? Yes or No?")
    return choice=="yes"
    
    
#GAME COMBINE
    #WHILE LOOP FOR GAME
print("Welcome to Tic Tac Toe!\n")
while True:
    
    #SETTING UP GAME
    the_board=[" "]*10
    player1_marker,player2_marker = user_input()

    turn=choose_first()
    print(turn,"will play first!\n")
    play_game=input("Are you ready? y or n:")
    
    if play_game=="y":
        game_on = True
    else:
        game_on = False 
    #PLAY GAME
    
    while game_on:
        if turn=='Player 1':
            
            #SHOW BOARD
            
            display_board(the_board)
            
            #CHOOSE POSITION
            
            position=player_choice(the_board)
            
            #PLACE MARKER
            
            place_marker(the_board,player1_marker,position)
           
            #CHECK IF THEY WON
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print("PLAYER ONE HAS WON!")
                game_on = False
            else:
                if board_full(the_board):
                    display_board(the_board)
                    print("THE GAME IS TIE")
                    game_on = False
                else:
                    turn="Player 2"
    
        else:
            #SHOW BOARD
            
            display_board(the_board)
            
            #CHOOSE POSITION
            
            position=player_choice(the_board)
            
            #PLACE MARKER
            
            place_marker(the_board,player2_marker,position)
            
            #CHECK IF THEY WON
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print("PLAYER TWO HAS WON!")
                game_on = False
            else:
                if board_full(the_board):
                    display_board(the_board)
                    print("THE GAME IS TIE")
                    game_on = False
                else:
                    turn="Player 1"
    #Playing the game
    if not replay():
        break
    
    #BREAK

    

    
