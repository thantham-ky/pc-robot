import open3d as o3d
import numpy as np
import os
import sys

import sklearn.cluster import Kme

# ply_file = sys.argv[1]
ply_file = 'D:/thantham/pc-robot/testcats4_seg.ply'

pcd = o3d.io.read_point_cloud(ply_file)

pcd_array = np.asarray(pcd.points)