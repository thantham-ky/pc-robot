import open3d as o3d
import numpy as np
#import os
import sys
import matplotlib.pyplot as plt

ply_file = sys.argv[1]
# ply_file = 'D:/thantham/pc-robot/testcats4_seg.ply'

ply = o3d.io.read_point_cloud(ply_file)


with o3d.utility.VerbosityContextManager(
        o3d.utility.VerbosityLevel.Debug) as cm:
    labels = np.array(
        ply.cluster_dbscan(eps=0.02, min_points=10, print_progress=True))

max_label = labels.max()
print(f"point cloud has {max_label + 1} clusters")
colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
colors[labels < 0] = 0
ply.colors = o3d.utility.Vector3dVector(colors[:, :3])
o3d.visualization.draw_geometries([ply])
