# Make a game grid 

grid_row_size = 7
grid_colum_size = 6
grid = [[0 for r in range(grid_row_size)] for c in range(grid_colum_size)]

token_positions = [[]]


def create_new_grid():
    for c in range(grid_colum_size):
        for r in range(grid_row_size):
            grid[c][r]= "[_]"
        # print(c," ",grid[c])  #only for debug

def update_grid():
    """
    draw grid with updated player move
    """
    for c in range(grid_colum_size):
        for r in range(grid_row_size):
            print(grid[c][r], end=" ")
        print("")



def player_input():
    input_colum = input("enter a colum number: ")
    grid[2][int(input_colum)] = " X "
    
    
    
    
create_new_grid()

player_input()

update_grid()