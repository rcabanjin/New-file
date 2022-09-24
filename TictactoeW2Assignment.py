#Tictactoe Week 2 Assignment
#Ron Cabanjin


print ("Tictactoe Week 2 Assignment")

def main():
    player = next_player ("")
    board = create_board()
    while not (winningspot(board)or tiegame (board)):
        show_board (board)
        make_move (player, board)
        player = next_player(player)
    show_board (board)
    print ("Congratulations, Thank you for playing")


def create_board():
    board = []
    for square in range (16):
        board.append (square + 1)
    return board

# print the board game to screen    
def show_board (board):
    print ()
    print (f"{board[0]} | {board[1]} | {board[2]} | {board[3]}") 
    print ('---+---+---+---')   
    print (f"{board[4]} | {board[5]} | {board[6]} | {board[7]}") 
    print ('---+---+---+---')    
    print (f"{board[8]} | {board[9]}| {board[10]}| {board[11]}") 
    print ('---+---+---+---')    
    print (f"{board[12]}| {board[13]}| {board[14]}| {board[15]}") 
    print ()   

#check for win or tie
def tiegame (board):
    for square in range (16):
        if board [square] != "x" and board [square] !="o":
            return False
        else: 
            print ("It's a tie")

    return True
    
#Check for win or tie
def winningspot (board):
    return (board [0] == board[1] == board [2] or 
            board [1] == board[2] == board [3] or 
            board [4] == board[5] == board [6] or 
            board [5] == board[6] == board [7] or 
            board [8] == board[9] == board [10] or 
            board [9] == board[10] == board [11] or 
            board [12] == board[13] == board [14] or 
            board [13] == board[14] == board [15] or
            board [0] == board[4] == board [8] or
            board [4] == board[8] == board [12] or
            board [1] == board[5] == board [9] or
            board [5] == board[9] == board [13] or
            board [2] == board[6] == board [10] or
            board [6] == board[10] == board [14] or
            board [3] == board[7] == board [11] or
            board [7] == board[11] == board [15] or
            board [0] == board[5] == board [10] or
            board [5] == board[10] == board [15] or
            board [1] == board[6] == board [11] or
            board [4] == board[9] == board [14] or
            board [3] == board[6] == board [9] or
            board [6] == board[9] == board [12] or
            board [2] == board[5] == board [8] or
            board [7] == board[10] == board [13])

def make_move (player, board):
    square = int (input (f"{player}'s turn to choose a square (1 to 16):"))
    board [square - 1] = player

#Switch the player
def next_player (current):
    if current == "" or current == "o":
        return "x"    
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()

