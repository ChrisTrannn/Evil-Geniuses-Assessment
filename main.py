# run pip install pandas and matplotlib if not installed already
from processGameState import ProcessGameState
import matplotlib.pyplot as plt
import numpy as np

# function that returns how frequent a team on a specific side is within the boundary
def in_boundary_frequency(team, side, game_state):
    dataframe = game_state.dataframe
    filtered_dataframe = dataframe[(dataframe['team'] == team) & (dataframe['side'] == side)]
    valid_rows = game_state.all_rows_within_bounds()
    filtered_dataframe = filtered_dataframe.index.isin(valid_rows)
    
    return filtered_dataframe.mean()
    
# function that returns the average time a team on a specific side takes to enter a site
def average_time(team, side, site, game_state):
    dataframe = game_state.dataframe
    filtered_dataframe = dataframe[(dataframe['team'] == team) & (dataframe['side'] == side) & (dataframe['area_name'] == site)]
    
    grouped_data = filtered_dataframe.groupby(['round_num', 'player'])
    average_times = grouped_data['seconds'].mean()
    average_times = average_times.dropna()
    overall_average_time = np.mean(average_times)

    return overall_average_time
    
# function that returns a heatmap of a team on a specific side holding down a site
def generate_heatmap(team, side, site, game_state):
    dataframe = game_state.dataframe
    filtered_dataframe = dataframe[(dataframe['team'] == team) & (dataframe['side'] == side) & (dataframe['area_name'] == site) & (dataframe['t_alive'] == 5) & (dataframe['ct_alive'] == 5) & (dataframe['bomb_planted'] == False)]
    
    x = filtered_dataframe['x']
    y = filtered_dataframe['y']

    plt.hist2d(x, y, bins=30, cmap='hot')
    
    plt.colorbar()
    plt.title(f'{side} Side {site} Heatmap')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.show()

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
    if in_boundary_frequency('Team2', 'T', game_state) >= 0.5:
        print('Team2 on T side entering the light blue boundary is a common strategy.')
    else:
        print('Team2 on T side entering the light blue boundary is not a common strategy.')
        
    # TASK B
    avg_time = average_time('Team2', 'T', 'BombsiteB', game_state)
    print(f'The average time it takes for Team2 on T side to enter BombsiteB is {avg_time} seconds.')
    
    # TASK C
    generate_heatmap('Team2', 'CT', 'BombsiteB', game_state)