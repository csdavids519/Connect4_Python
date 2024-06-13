
grid_row_size = 7
grid_column_size = 6
grid = [["[_]" for c in range(grid_column_size)] for r in range(grid_row_size)]  

token_positions = [[]]

input_column = 0


def test():
    #grid[row][col]
    grid[4][5] = " o "
    grid[4][4] = " o "
    grid[4][3] = " o "
    
    
    
    




def player_input():
    """
    Check payer input value is int and in rage of the game grid
    """
    global input_column
    waiting_player_input = True
    
    while waiting_player_input:
        input_column = input("enter a column number: ")
        try:
            input_column = int(input_column)
        except ValueError:
            print("You must enter a number")
            continue

        if 0 <= int(input_column) <= 6:
            waiting_player_input = False
            check_place_position()
        else:
            print("Enter a value between 0 and 6")
            continue
    # player_input()

def check_place_position():
    """
    Check each row in the users selected column starting at the bottom, find the first empty position
    """
    for i in range(5, -1, -1):
        if grid[int(input_column)][i] == "[_]":
            print(f" {i} is blank")  #debug
            grid[int(input_column)][i] = " X "
            break #only place one token
        elif (i == 0) and grid[int(input_column)][i] != "[_]":
            print("this column is full, pick another")
    update_grid()

def update_grid():
    """
    draw grid with updated player move
    """
    for c in range(grid_column_size):
        for r in range(grid_row_size):
            print(grid[r][c], end=" ")
        print("")
    check_winner()


def check_winner():
    """
    Check for a game win or change player
    """

    # check horizontal 
    












test()
player_input()





""" thursday

add pc player
add check for win
"""