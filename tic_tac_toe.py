import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentplayer = "X"
winner = None
gameRunning = True 

#make the board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("-----")
printBoard(board)

#take player input
def playerInput(board):
    inp = int(input("Enter a number 1-9:"))
    if inp >=1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("That input is invalid.")

#check for win/tie/loss
#win horizontal, vertical, or diagonal
def checkhorizontal(board):
    global winner #global = changes made within scope changes in the entire file
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6]!= "-":
        winner = board[6]
        return True 

def checkrow(board):
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True 

def checkdiagonal(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True 

def checktie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie")
        gameRunning = False

def checkwin():
    if checkdiagonal(board) or checkhorizontal(board) or checkrow(board):
        print(f"The winner is {winner}")
        gameRunning = False 

#switch the player 
def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else: 
        currentplayer = "X"

#computer 
def computer(board):
    while currentplayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchplayer()



while gameRunning: 
    printBoard(board)
    playerInput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)




