
grid_row_size = 6
grid_column_size = 7
grid = [["[_]" for c in range(grid_column_size)] for r in range(grid_row_size)]  

token_position_row = 0
token_position_col = 0

input_column = 0


def test():
    #grid[row][col]
    grid[4][5] = " o "
    grid[4][4] = " o "
    grid[4][3] = " o "
    
    print(grid)
    
    
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

def check_place_position():
    """
    Check each row in the users selected column starting at the bottom, find the first empty position
    """
    global token_position_row
    global token_position_col

    for i in range(5, -1, -1):
        if grid[int(input_column)][i] == "[_]":
            print(f" {i} is blank")  #debug
            grid[int(input_column)][i] = " X "
            token_position_row = i
            token_position_col = int(input_column)
            break #only place one token
        elif (i == 0) and grid[int(input_column)][i] != "[_]":
            print("this column is full, pick another")
    update_grid()

def update_grid():
    """
    draw grid with updated player move
    """
    for r in range(grid_column_size):
        for c in range(grid_row_size):
            print(grid[r][c], end=" ")
        print("")
    check_winner()


def check_winner():
    """
    Check for a game win or change player
    - code reference Shaun Halverson see readme for link
    """
    global token_position_row
    global token_position_col

    # check horizontal 
    for y in range(grid_row_size):
        for x in range(grid_column_size -3):
            if (grid[x][y] == " X " and grid[x+1][y] == " X " and grid[x+2][y] == " X " and grid[x+3][y] == " X "):
                print(f"x winner {x}")
                return True
            
    # check vertical
    for y in range(grid_row_size):
        for x in range(grid_column_size -3):
            if (grid[x][y] == " X " and grid[x][y+1] == " X " and grid[x][y+2] == " X " and grid[x][y+3] == " X "):
                print(f"x winner {x}")
                return True
            
    # check diagonal top right to bottom left
    for y in range(grid_row_size -3):
        for x in range(3, grid_column_size):
            if (grid[x][y] == " X " and grid[x+1][y-1] == " X " and grid[x+2][y-2] == " X " and grid[x+3][y-3] == " X "):
                print(f"x winner {x}")
                return True
            
    # check diagonal top left to bottom right
    for y in range(grid_row_size -3):
        for x in range(grid_column_size - 3):
            if (grid[x][y] == " X " and grid[x+1][y+1] == " X " and grid[x+2][y+2] == " X " and grid[x+3][y+3] == " X "):
                print(f"x winner {x}")
                return True
            
    player_input()












test()
player_input()





""" thursday

add pc player
add check for win
"""