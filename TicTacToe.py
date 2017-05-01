# Create a 2 dimensional array to hold the positions of the array
# winning combinations 012 000 111 222

#Create Board
#Game Logic
#Player Move

board =[" "," "," "," "," "," "," "," "," "]

def printBoard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
#printBoard(board)


def checkWin(board):
    if(
        (board[0] == board[1] and board[0] == board[2] and board[0] != " ") or
        (board[3] == board[4] and board[3] == board[5] and board[3] != " ") or
        (board[6] == board[7] and board[6] == board[8] and board[6] != " ") or
        (board[0] == board[3] and board[0] == board[6] and board[0] != " ") or
        (board[1] == board[4] and board[1] == board[7] and board[1] != " ") or
        (board[2] == board[5] and board[2] == board[8] and board[2] != " ") or
        (board[0] == board[4] and board[0] == board[8] and board[0] != " ") or
        (board[2] == board[4] and board[2] == board[6] and board[2] != " ")
    ):
        return True

#Start
print("\n\n")
printBoard(board)