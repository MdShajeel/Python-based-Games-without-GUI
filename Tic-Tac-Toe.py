#!/usr/bin/env python
# coding: utf-8

# In[ ]:


board=[['','',''],['','',''],['','','']]
def print_board(board):
    print(*board[0],sep=" | ")
    print("--------")
    print(*board[1],sep=" | ")
    print("--------")
    print(*board[2],sep=" | ")
    
def get_markers():
    marker1=input("Player 1 choice(X or O): ").upper()
    marker2=""
    if marker1=='X':
        marker2="O"
        return ['X','O']
    elif marker1=='O':
        marker2='X'
        return ['O','X']
    else:
        print("Invalid Input")
        return get_markers()
    
def get_coordinates():
    x,y=list(map(int,input("Enter coordinates:")))
    if x in [0,1,2] and y in [0,1,2] and board[x][y]=="":
        return [x,y]
    else:
        if board[x][y]!="":
            print("Position is already filled")
        else:
            print("Invalid Input")
        return get_coordinates()
    
def check_for_win(board):
    for row in board:
        if row[0]==row[1] and row[1]==row[2] and row[1]!="":
            return True
    for i in range(len(board)):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[2][i]!="":
            return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]!="":
        return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[2][0]!="":
        return True
    return False

def update_board(board,chance,marker,x,y):
    if chance==True:
        board[x][y]=marker
        if check_for_win(board):
            print("Player 1 wins")
            return "Game over"
        return False
    else:
        board[x][y]=marker
        if check_for_win(board):
            print("player 2 wins")
            return "Game over"
        return True
        
def play_game():
    player1=0
    player2=0
    count=0
    m1,m2=get_markers()
    print(f"Player 1: {m1},Player 2:{m2}")
    chance=True
    while count!=9:
        print_board(board)
        x,y=get_coordinates()
        if chance:
            chance=update_board(board,chance,m1,x,y)
            if chance=='Game over':
                break
        else:
            chance=update_board(board,chance,m2,x,y)
            if chance=="Game over":
                break
        count+=1
    if count==9:
        print("Draw")
play_game()

