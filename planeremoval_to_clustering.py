import open3d as o3d
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans

# ply_file = sys.argv[1]
ply_file = 'D:/thantham/pc-robot/testcats4_seg.ply'

pcd = o3d.io.read_point_cloud(ply_file)

pcd_array = np.asarray(pcd.points)

kmeans = KMeans(n_clusters=11, random_state=0).fit(pcd_array)

print('Labels on training: ',kmeans.labels_)
print('Centroid coordinates: \n',kmeans.cluster_centers_)

centroids = kmeans.cluster_centers_

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax = plt.axes(projection='3d')

ax.scatter3D(centroids[:,0], centroids[:, 1], centroids[:, 2], c = centroids[:, 2], cmap='Greens')
