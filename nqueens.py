def copyList(l):
    n = len(l)
    ret = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = l[i][j]
    return ret

def isValidPlace(i,j,n):
    if i<0 or j<0 or i>=n or j>=n:
        return False
    return True

def isSafe(board,row,col):
    n=len(board)

    if board[row][col] == 1:
        return False

    for i in range(n):
        if board[i][col] == 1:
            return False
    for i in range(n):
        if board[row][i] == 1:
            return False
    
    #down right
    i,j = row,col
    while(isValidPlace(i,j,n)):
        if board[i][j] == 1:
            return False
        i+=1
        j+=1

    #down left
    i,j = row,col
    while(isValidPlace(i,j,n)):
        if board[i][j] == 1:
            return False
        i+=1
        j-=1

    #up left
    i,j = row,col
    while(isValidPlace(i,j,n)):
        if board[i][j] == 1:
            return False
        i-=1
        j-=1

    #up right
    i,j = row,col
    while(isValidPlace(i,j,n)):
        if board[i][j] == 1:
            return False
        i-=1
        j+=1

    return True

def printBoard(board):
    for i in board:
        print(i)

def solveNQueens(board, queensRemaining):
    if(len(board)<queensRemaining):
        return False, board

    if queensRemaining == 0:
        print("Problem Solved")
        return True, board
    

    n = len(board)

    for i in range(n):
        for j in range(n):
            if isSafe(board,i,j):
                newBoard = copyList(board)
                newBoard[i][j] = 1
                isSolved, ansBoard = solveNQueens(newBoard, queensRemaining-1)
                if isSolved == True:
                    return True, ansBoard
    
    return False, board
    



def main():

    n = int(input("Enter the size of board: "))
    noOfQueens = int(input("Enter the number of queens: "))
    board = [[0 for _ in range(n)] for _ in range(n)]


    isSolved, ansBoard = solveNQueens(board, noOfQueens)

    if isSolved:
        print(f"{noOfQueens} queens can be placed on board of size {n}*{n}")
        printBoard(ansBoard)
    else:
        print(f"{noOfQueens} queens can not be placed on board of size {n}*{n}")
        printBoard(ansBoard)


main()