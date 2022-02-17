
import random
board =[' ' for x in range(10) ]


def insert_letter(letter, pos):
    board[pos] = letter


def spaceisFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print()
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print()

    
def isWinner(bo, le):
    return(bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def player1Move():
    run = True
    while run:
        move = input("Please select a position to play an x from (1 - 9) :")
        try:
            move = int(move)
            if move > 0 and move < 10:  
                if spaceisFree(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Sorry This space is occupied !!")    
            else:
                print("Please type a number within a range !! ")        
        except :
            print("Please enter a number !!")

def compMove():
    possmoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] 
    move = 0

    for let in ['O' , 'X']:
        for i in possmoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possmoves:
        if i in[1, 3, 7, 9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possmoves:
        move = 5
        return move 

    edgesOpen = []
    for i in possmoves:
        if i in[2, 4, 6, 8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True   

def main():
    print("TIC TAC TOE")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):  #for player 1
            player1Move()
            printBoard(board)
        else:
            print("Sorry player O's win this time !!")    
            break

        if not (isWinner(board, 'X')): #for player 2 or computer
            move = compMove()
            if move == 0:
                print("Tie Game!!")
            else:
                insert_letter('O', move)
                print("computer placed an O in the position ", move, ":")
                printBoard(board)
                
        else:
            print("Player X's win this time !!")    
            break    

    if (isBoardFull(board)):
        print("GAME TIED !!")

main()