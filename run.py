import random
from colorama import Fore, Back, Style
# from simple_term_menu import TerminalMenu

columnx_size, rowy_size = 7, 7
grid = [["[_]" for y in range(rowy_size)] for x in range(columnx_size)]

# add row with column identifers
for i in range(columnx_size):
    grid[i][6] = f"[{i}]"

current_player = 0
input_column = 0
player_name = ""


def get_player_name():
    global player_name
    while player_name == "":
        # get players name
        player_name = input("Enter your name: ")


def player_input():
    """ Check payer input value is valid and, find the first empty row in chosen column"""
    waiting_player_input = True
    print_output('player')
    # check input is valid
    while waiting_player_input:
        input_column = input("Enter a column number between 0 and 6: ")
        try:
            input_column = int(input_column)
        except ValueError:
            print("You must enter a number")
            continue
        if 0 <= int(input_column) <= 6:
            waiting_player_input = False
        else:
            print("Enter a value between 0 and 6")
            continue
    check_column(input_column, 0)


def pc_player_input():
    """ PC player easy setting picks column at random """
    print_output('PCplayer') 
    column = random.randint(0, 6)
    check_column(column, 1)


def check_column(column, player):
    """
    Check each row in the users selected column starting at the bottom,
    find the first empty position
    """
    for i in range(5, -1, -1):
        if (i == 0) and grid[int(column)][i] != "[_]":
            print("this column is full, pick another")
            if player == 0:
                player_input()
            else: 
                pc_player_input()
        else:
             place_token(column, player)


def place_token(column, player):
    """ Find first empty position in the column """
    token = ' X ' if player == 0 else ' O '

    for i in range(5, -1, -1):
        if grid[int(column)][i] == "[_]":
            grid[int(column)][i] = token
            break  # only place one token
    update_grid()


def update_grid():
    """ draw grid array in a user readable format """
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

    for token in tokens:
        for y in range(rowy_size):
            for x in range(columnx_size):
                try:
                    # check horizontal
                    if (grid[x][y] == token and
                            grid[x+1][y] == token and
                            grid[x+2][y] == token and
                            grid[x+3][y] == token):
                                winner_found = True
                                break
                    # check vertical
                    if (grid[x][y] == token and
                            grid[x][y+1] == token and
                            grid[x][y+2] == token and
                            grid[x][y+3] == token):
                                winner_found = True
                                break
                    # check diagonal top left to bottom right
                    if (grid[x][y] == token and
                            grid[x+1][y-1] == token and
                            grid[x+2][y-2] == token and
                            grid[x+3][y-3] == token):
                                winner_found = True
                                break
                    # check diagonal top right to bottom left
                    if (grid[x][y] == token and
                            grid[x-1][y-1] == token and
                            grid[x-2][y-2] == token and
                            grid[x-3][y-3] == token):
                                winner_found = True
                                break
                except IndexError:
                    continue
                if winner_found:
                    print_output('winner')
                    return
        change_player()

def change_player():
    global current_player
    current_player = 1 if current_player == 0 else 0

    if current_player == 0:
        player_input()
    else:
        pc_player_input()


def print_output(x):
    global player_name

    if x == 'welcome':
        print(Fore.MAGENTA + """
**************************************************************
****                 WELCOME TO CONNECT 4x                ****
****                                                      ****
**** Pick a column number and try to get 4 'X's' in a row ****
**************************************************************
""")
    elif x == 'player':
        print(Fore.BLUE + f"""
              
*******************************
***    {player_name}'s turn!    ***
*******************************""")

    elif x == 'PCplayer':
        print(Fore.YELLOW + """
*******************************
***     PC player turn      ***
*******************************
              """)
        
    elif x == 'winner':
        print(Fore.GREEN + f"""
*******************************
*******************************
****   Winner: {current_player}   ****
*******************************
*******************************
        """)

    print(Style.RESET_ALL)





def main():
    print_output('welcome')
    get_player_name()
    
    player_input()

main()

