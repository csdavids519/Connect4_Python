
grid_row_size = 7
grid_column_size = 6
grid = [["[_]" for r in range(grid_row_size)] for c in range(grid_column_size)]

token_positions = [[]]

token_drop_position = 0

def update_grid():
    """
    draw grid with updated player move
    """
    for c in range(grid_column_size):
        for r in range(grid_row_size):
            print(grid[c][r], end=" ")
        print("")



def test():
    grid[5][4] = " o "
    grid[4][4] = " o "
    grid[3][4] = " o "

def player_input():
    waiting_player_input = True
    while waiting_player_input:
        try:
            input_column = input("enter a column number: ")
            # grid[0][int(input_column)] = " X "
        except IndexError:
            print("Enter a value between 0 and 6")
        except ValueError:
            print("Enter a number between 0 and 6")
        else:
            waiting_player_input = False
    def check_place_position():
        """
        check each row in the users selected column starting at the bottom, find the first empty position
        """
        nonlocal input_column
        for i in range(5, 0, -1):
            if grid[i][int(input_column)] == "[_]":
                print(f" {i} is blank")
                token_drop_position = i
                grid[i][int(input_column)] = " X "
                break #only place one token
        update_grid()
    check_place_position()
    player_input()


test()

player_input()

