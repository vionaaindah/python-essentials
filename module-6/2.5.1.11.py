def string_list(string):
    list_row=[]
    list_row[:0]= string
    return list_row

def sudoku_valid(board):
     len_board = len(board)

     if len_board < 1:
        return False
     for row in range(0, len_board):
        row_fields = []
        col_fields = []

        for col in range(0, len_board):
            if int(board[col][row]) in col_fields:
                return False
            col_fields.append(int(board[col][row]))

            if int(board[row][col]) in row_fields:
                return False
            row_fields.append(int(board[row][col]))

            if int(board[row][col]) <= 0:
                return False
     return True

board = [[0], [1], [2], [3], [4], [5], [6], [7], [8]]

for i in range(9):
    row = input("Enter row: ")
    if len(row) != 9:
        row = input("Enter 9 digits. Enter row: ")
    board[i] = string_list(row)

if sudoku_valid(board):
     print("Yes")
else:
     print("No")
