# %% 1 import lib
import open3d as o3d
import numpy as np

# %% 2 define arguments
ply_file = ""

# %% 3 read files
ply = o3d.io.read_point_cloud(ply_file)

# %% 4 convert ply to array

ply_arr = np.asarray(ply.points)

# %%% visualize pc

o3d.visualization.draw_geometries([ply])

# %% 5 downsampling pc

down_ply = ply.voxel_down_sample(voxel_size=0.05) 
