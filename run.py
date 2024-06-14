import random

columnx_size, rowy_size = 7,7
grid = [["[_]" for y in range(rowy_size)] for x in range(columnx_size)]

# add row with column identifers 
for i in range(columnx_size):
    grid[i][6] = f"[{i}]"

input_column = 0
player = "PC"
    
print("**************************************************************")
print("****                 WELCOME TO CONNECT 4                 ****")
print("**** Pick a column number and try to get 4 'X's' in a row ****")
print("**************************************************************")    

player_name = ""
while player_name == "":
    #get players name
    player_name = input("Enter your name: ")

def player_input():
    """
    Check payer input value is int and in rage of the game grid
    """
    global input_column
    global player_name
    waiting_player_input = True
    print("")   
    print("")   
    print("*******************************")
    print(f"**** {player_name}'s turn! ****")
    print("*******************************")
    
    while waiting_player_input:
        input_column = input("Enter a column number between 0 and 6: ")
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
    for i in range(5, -1, -1):
        if grid[int(input_column)][i] == "[_]":
            grid[int(input_column)][i] = " X "
            break #only place one token
        elif (i == 0) and grid[int(input_column)][i] != "[_]":
            print("this column is full, pick another")
            player_input()
    update_grid()

def pc_player():
    """
    PC player easy setting picks column at random
    """
    print("")   
    print("")   
    print("*******************************")
    print("**** PC player turn ****")
    print("*******************************")

    check_row = True
    pc_choice = random.randint(0,6)

    while check_row:
        #check if the PC column choice is not full
        for i in range(5, -1, -1):
            if grid[pc_choice][i] == "[_]":
                grid[pc_choice][i] = " O "
                check_row = False
                break #only place one token
            elif (i == 0) and grid[pc_choice][i] != "[_]":
                pc_choice = random.randint(0,6)
                i = 0 # reset for loop
                continue
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
    * code reference modified from Shaun Halverson example see readme for link
    """
    tokens = [" O ", " X "]
    winner_found = False
    
    # check horizontal 
    for token in tokens:
        for y in range(rowy_size):
            for x in range(columnx_size):
                try:
                    if (grid[x][y] == token and grid[x+1][y] == token and grid[x+2][y] == token and grid[x+3][y] == token):
                        winner_found = True
                        break
                except IndexError:
                    continue
                
    # check vertical
    for token in tokens:
        for y in range(rowy_size):
            for x in range(columnx_size):
                try:
                    if (grid[x][y] == token and grid[x][y+1] == token and grid[x][y+2] == token and grid[x][y+3] == token):
                        winner_found = True
                        break
                except IndexError:
                    continue
                
    # check diagonal top left to bottom right
    for token in tokens:
        for y in range(rowy_size): 
            for x in range(columnx_size):
                try:
                    if (grid[x][y] == token and grid[x+1][y-1] == token and grid[x+2][y-2] == token and grid[x+3][y-3] == token):
                        winner_found = True
                        break
                except IndexError:
                    continue
                
    # check diagonal top right to bottom left
    for token in tokens:
        for y in range(rowy_size):
            for x in range(columnx_size):
                try:
                    if (grid[x][y] == token and grid[x-1][y-1] == token and grid[x-2][y-2] == token and grid[x-3][y-3] == token):
                        winner_found = True
                        break
                except IndexError:
                    continue
                
    if winner_found:
        print("")   
        print("*******************************")
        print("*******************************")
        print(f"****     Winner: {player} !!  ****")
        print("*******************************")
        print("*******************************")
        print("")
        return   
    change_player()

def change_player():
    """
    Manage what player is next
    """
    global player
    global player_name
    
    if player == player_name:
        player = "PC"
        pc_player()
    elif player == "PC":
        player = player_name
        player_input()
        
# Start game here with printing blank game grid
update_grid()