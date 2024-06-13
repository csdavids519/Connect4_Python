
grid_row_size = 7
grid_column_size = 6
grid = [["[_]" for r in range(grid_row_size)] for c in range(grid_column_size)]

token_positions = [[]]

input_column = 0


def test():
    grid[5][4] = " o "
    grid[4][4] = " o "
    grid[3][4] = " o "

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
        if grid[i][int(input_column)] == "[_]":
            print(f" {i} is blank")  #debug
            grid[i][int(input_column)] = " X "
            break #only place one token
        elif (i == 0) and grid[i][int(input_column)] != "[_]":
            print("this column is full, pick another")
    update_grid()

def update_grid():
    """
    draw grid with updated player move
    """
    for c in range(grid_column_size):
        for r in range(grid_row_size):
            print(grid[c][r], end=" ")
        print("")
    player_input()




test()
player_input()





""" thursday

fix error checkibng
add pc player
add check for win
"""