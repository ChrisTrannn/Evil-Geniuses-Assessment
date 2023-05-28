import matplotlib.path as mplPath
import numpy as np
import matplotlib.pyplot as plt

polygon = [
            [-1735, 250], 
            [-2024, 398], 
            [-2806, 742],
            [-2472, 1233],
            [-1565, 580]
        ]
point = (-1565, 40)

def _row_within_bounds(self, x, y, z):
    path = mplPath.Path(np.array(polygon))
    zmin, zmax = self.zaxis_bounds
    
    if path.contains_point((x, y)):
        return zmin <= z <= zmax
    else:
        return False
    
print(_row_within_bounds(*point, 0))