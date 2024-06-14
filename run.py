
columnx_size, rowy_size = 7,6

grid = [["[_]" for y in range(rowy_size)] for x in range(columnx_size)]

token_position_row = 0
token_position_col = 0

input_column = 0


def test():

    grid[1][5] = " @ "
    
    grid[2][5] = " @ "
    grid[2][4] = " @ "
    
    grid[3][5] = " @ "
    grid[3][4] = " @ "
    grid[3][3] = " @ "

    grid[4][5] = " @ "
    grid[4][4] = " @ "
    
    grid[5][5] = " @ "
    
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
    draw grid array in a user readable format
    """
    
    for row in range(rowy_size):
        for col in range(columnx_size):
            print(grid[col][row], end=" ")
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

    for y in range(rowy_size):
        for x in range(columnx_size):
            try:
                if (grid[x][y] == " X " and grid[x+1][y] == " X " and grid[x+2][y] == " X " and grid[x+3][y] == " X "):
                    print(f"x winner {x}")
                    return True
            except IndexError:
                print(f"IndxeError x:{x} y:{y}")
                
    # check vertical
    for y in range(rowy_size):
        for x in range(columnx_size):
            try:
                if (grid[x][y] == " X " and grid[x][y+1] == " X " and grid[x][y+2] == " X " and grid[x][y+3] == " X "):
                    print(f"x winner {x}")
                    return True
            except IndexError:
                print(f"IndxeError x:{x} y:{y}")
                
    # check diagonal top left to bottom right
    for y in range(rowy_size): 
        for x in range(columnx_size):
            try:
                if (grid[x][y] == " X " and grid[x+1][y-1] == " X " and grid[x+2][y-2] == " X " and grid[x+3][y-3] == " X "):
                    print(f"x winner {x}")
                    return True
            except IndexError:
                print(f"IndxeError x:{x} y:{y}")
                
    # check diagonal top right to bottom left
    for y in range(rowy_size):
        for x in range(columnx_size):
            try:
                if (grid[x][y] == " X " and grid[x-1][y-1] == " X " and grid[x-2][y-2] == " X " and grid[x-3][y-3] == " X "):
                    print(f"x winner {x}")
                    return True
            except IndexError:
                print(f"IndxeError x:{x} y:{y}")
                
    player_input()












test()
player_input()





""" thursday

add pc player
add check for win
"""