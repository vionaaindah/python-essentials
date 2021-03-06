from random import randrange # for drawing a random integer number

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in range(len(board)):
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   "    + str(board[row][0])  + "   " + \
              "|   " + str(board[row][1]) + "   " + \
              "|   " + str(board[row][2]) + "   |   ")
        print("|       "*3 + "|")
    print("+-------"*3 + "+")


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    user_fields = int(input("Enter your move:"))

    while(user_fields < 1 or user_fields > 9):
        print("Enter number between 1 and 9")
        user_fields = int(input("Enter your move:"))
        
    while True:
        if user_fields in free_fields:
            user_fields = user_fields - 1
            row = user_fields // 3
            column = user_fields % 3
            board[row][column] = "O"
            break
        else:
            print('Position already filled, choose another position')
            user_fields = int(input("Enter your move:"))
    display_board(board)

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(len(board)):
        for column in range(len(board)):
          if board[row][column] != "O" and board[row][column] != "X":
            free_fields.append(board[row][column])
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    if (board[0][0] == board[0][1] == board[0][2] == sign) or \
       (board[1][0] == board[1][1] == board[1][2] == sign) or \
       (board[2][0] == board[2][1] == board[2][2] == sign) or \
       (board[0][0] == board[1][0] == board[2][0] == sign) or \
       (board[0][1] == board[1][1] == board[2][1] == sign) or \
       (board[0][2] == board[1][2] == board[2][2] == sign) or \
       (board[0][0] == board[1][1] == board[2][2] == sign) or \
       (board[0][2] == board[1][1] == board[2][0] == sign):
        return True
    return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    computer_fields = randrange(1,10)
    while True:
        if computer_fields in free_fields:
            computer_fields = computer_fields - 1
            row = computer_fields // 3
            column = computer_fields % 3
            board[row][column] = "X"
            break
        else:
            computer_fields = randrange(1, 10)
    display_board(board)

# Initialize the board
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
display_board(board)

#Tic Tac Toe Main Program
while True:
    # check if all board filled
    moves = 0
    for row in range(len(board)):
      for column in range(len(board)):
        if board[row][column] == "O" or board[row][column] =="X":
            moves +=1
    if moves == 9:
        print("It's a tie game!")
        break

    # User Move Program
    enter_move(board)
    if victory_for(board, "O"):
        print('You won!')
        break

    # Computer Move Program
    draw_move(board)
    if victory_for(board, "X"):
        print('You lose!')
        break
