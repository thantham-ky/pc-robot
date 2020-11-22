import open3d as o3d
import sys

ply_file = sys.argv[1]

ply = o3d.io.read_point_cloud(ply_file)

o3d.visualization.draw_geometries([ply])