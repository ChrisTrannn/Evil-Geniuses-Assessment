# run pip install pandas and matplotlib if not installed already
from processGameState import ProcessGameState

# function that returns how frequent a team on a specific side is within the boundary
def in_boundary_frequency(team, side, game_state):
    dataframe = game_state.dataframe
    filtered_dataframe = dataframe[(dataframe['team'] == team) & (dataframe['side'] == side)]
    valid_rows = game_state.all_rows_within_bounds()
    filtered_dataframe = filtered_dataframe.index.isin(valid_rows)
    
    return filtered_dataframe.mean()
    
def average_time(team, side, site, game_state):
    pass

if __name__ == '__main__':
    # input parameters
    filePath = './data/game_state_frame_data.pickle'
    boundary = [
                    [-1735, 250], 
                    [-2024, 398], 
                    [-2806, 742],
                    [-2472, 1233],
                    [-1565, 580]
                ]
    zaxis_bounds = (285, 421)
    
    game_state = ProcessGameState(filePath, boundary, zaxis_bounds)
    
    # TASK A
    # if the frequency of a team entering the boundayr is less than 50%, it is not a common strategy
    if in_boundary_frequency('Team2', 'T', game_state) >= 0.5:
        print('Team2 on T side entering the light blue boundary is a common strategy.')
    else:
        print('Team2 on T side entering the light blue boundary is not a common strategy.')
        
    # TASK B
    average_time('Team2', 'T', 'BombsiteB', game_state)