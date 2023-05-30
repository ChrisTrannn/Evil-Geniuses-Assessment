from collections import defaultdict
import matplotlib.path as mplPath
import numpy as np
import pandas as pd
import pickle

class ProcessGameState:
    def __init__(self, file, boundary, zaxis_bounds):
        self.dataframe = self._load_data(file)
        self.boundary = boundary
        self.zaxis_bounds = zaxis_bounds
        self.polygon_path = mplPath.Path(np.array(self.boundary))
        
    # private function to load data from pickle file
    def _load_data(self, file):
        with open(file, 'rb') as f:
            data = pickle.load(f)
        return data
    
    # private helper function to check if row is within the boundary, stackoverflow proves runtime efficiency
    # https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
    def _row_within_bounds(self, x_list, y_list, z_list):
        zmin, zmax = self.zaxis_bounds
        
        inside_polygon = self.polygon_path.contains_points(np.column_stack((x_list, y_list)))
        within_z_bounds = np.logical_and(zmin <= z_list, z_list <= zmax)
        
        return inside_polygon & within_z_bounds
    
    # returns a list of all rows within provided boundary
    def all_rows_within_bounds(self):
        x_list = self.dataframe['x'].values
        y_list = self.dataframe['y'].values
        z_list = self.dataframe['z'].values
        
        valid_rows = np.where(self._row_within_bounds(x_list, y_list, z_list))[0]
        
        return valid_rows.tolist()
    
    # returns a dictionary where the key is the weapon class and the value is a set of all weapons in that class
    def extract_weapon_classes(self):
        weapon_classes = defaultdict(set)
        inventory = self.dataframe['inventory']
        
        for arr in inventory:
            if arr is not None:
                dct = arr[0]
                weapon_class = dct['weapon_class']
                weapon_name = dct['weapon_name']
                weapon_classes[weapon_class].add(weapon_name)
        
        return weapon_classes
    
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
    print(game_state.extract_weapon_classes())