# run pip install pandas and matplotlib if not installed already
from processGameState import ProcessGameState

if __name__ == '__main__':
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
    
    # a. Is entering via the light blue boundary a common strategy used by Team2 on T (terrorist) side?
    # common strategy is determined if the proportion of entries in the boundary is greater than 50%
    team, side = 'Team2', 'T'
    if game_state.is_common_strategy(team, side):
        print(f"Entering the light blue boundary is a common strategy used by {team} on {side} side.")
    else:
        print(f"Entering the light blue boundary is not a common strategy used by {team} on {side} side.")
    
    # b. What is the average time that Team2 on T (terrorist) side enters BombsiteB with least 2 rifles or SMGs?
    team, side, site, weapons, min_num = 'Team2', 'T', 'BombsiteB', ['Rifle', 'SMG'], 2
    print(f'Average time: {game_state.average_time(team, side, site, weapons, min_num)}')
    
    # c. Now that we’ve gathered data on Team2 T side, let's examine their CT
    # (counter-terrorist) Side. Using the same data set, tell our coaching
    #staff where you suspect them to be waiting inside “BombsiteB”