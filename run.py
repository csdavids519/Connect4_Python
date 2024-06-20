import random
from colorama import Fore, Back
# from simple_term_menu import TerminalMenu

columnx_size, rowy_size = 7, 7
grid = [["[_]" for y in range(rowy_size)] for x in range(columnx_size)]

# add row with column identifers
for i in range(columnx_size):
    grid[i][6] = f"[{i}]"

current_player = 0
input_column = 0
player_name = ""
tokens = ['\033[44m' + ' X ' + '\033[49m', '\033[46m' + ' O ' + '\033[49m']


def get_player_name():
    global player_name
    while True:
        # get players name
        player_name = input(Fore.YELLOW +"Enter your name: ")
        if len(player_name) < 3:
             print(Fore.RED + 'Name must be at least 3 characters long') 
        else:
            break


def player_input():
    """ Check payer input value is valid and, find the first empty row in chosen column"""
    print_player_turn()
    # check input is valid
    while True:
        input_column = input(Fore.YELLOW +"Enter a column number between 0 and 6: ")
        try:
            input_column = int(input_column)
        except ValueError:
            print(Fore.RED +"You must enter a real number, without decimal points or letters")
            continue
        if 0 <= int(input_column) <= 6:
            break
        else:
            print(Fore.RED +"Enter a value between 0 and 6")
            continue
    check_column(input_column, 0)


def pc_player_input():
    """ PC player easy setting picks column at random """
    print_pc_turn() 
    check_column(random.randint(0, 6), 1)


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
    place_token(column, player)


def place_token(column, player):
    """ Find first empty position in the column """
    # token = '\033[44m' + ' X ' + '\033[49m' if player == 0 else '\033[46m' + ' O ' + '\033[49m'
    global tokens

    token = tokens[0] if player == 0 else tokens[1]
    for i in range(5, -1, -1):
        if grid[int(column)][i] == "[_]":
            grid[int(column)][i] = token
            break  # only place one token
    update_grid()


def update_grid():
    """ draw grid array in a user readable format """
    print(Fore.RESET)
    for row in range(rowy_size):
        for col in range(columnx_size):
            print(Back.RESET + grid[col][row], end=" ")
        print(Back.RESET )
    check_winner()


def check_winner():
    """
    Check for a game win or change player
    * code reference modified from Shaun Halverson example see readme for link
    """
    global tokens
    # tokens = [" O ", '\033[44m' + ' X ']
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
                    print_winner(token)
                    return
    change_player()

def change_player():
    global current_player
    current_player = 1 if current_player == 0 else 0

    if current_player == 0:
        player_input()
    else:
        pc_player_input()


def print_winner(winner):
    print(Fore.GREEN + f"""
*******************************
*******************************
****   Winner: {winner} \033[49m   ****
*******************************
*******************************
        """)
    print(Fore.RESET)


def print_welcome():
    print(Fore.MAGENTA + """
**************************************************************
****                 WELCOME TO CONNECT 4x                ****
****                                                      ****
****                                                      ****
**************************************************************

    
    Pick a column number to insert your token at the top,
    it will fall to the next empty space.
          
    Try to get four X's in a row before the computer player!
""")
    print(Fore.RESET)

    for row in range(rowy_size):
        for col in range(columnx_size):
            print(Back.RESET + grid[col][row], end=" ")

        print(Back.RESET )
    print("")


def print_player_turn():
    print(Fore.MAGENTA + f"""
              
          
*******************************
***    {player_name}'s turn!    ***
*******************************""")

def print_pc_turn():
    print(Fore.MAGENTA + """
          

*******************************
***     PC player turn      ***
*******************************""")
        

def main():
    print_welcome()
    get_player_name()
    
    player_input()

main()

