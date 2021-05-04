import os
import sys
import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy import sparse
from scipy.sparse import linalg

import argparse
parser = argparse.ArgumentParser(description='Plot 2D and 3D trajectories')
parser.add_argument("-d", "--data",type=str,metavar='', required=True, help="data source")
parser.add_argument("-t","--title",type=str,metavar='', required=True, help='title of the graph')
parser.add_argument("-c","--color",type=str,metavar='', required=True, help='color with this form -Color')
args=parser.parse_args()
#parser = argparse.ArgumentParser()
#parser.add_argument("-d","data",type=str)
#args = parser.parse_args()

class Pose3D:

    def __init__(self, x, y, z, qw, qx, qy, qz):
        self.x = x
        self.y = y
        self.z = z
        self.qw = qw
        self.qx = qx
        self.qy = qy
        self.qz = qz
		
def plot_nodes(nodes, ax, color="-r", label=""):
    x, y, z = [], [], []
    for n in nodes:
        x.append(n.x)
        y.append(n.y)
        z.append(n.z)
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    max_range = np.array([x.max() - x.min(), y.max() - y.min(), z.max() - z.min()]).max() / 2.0
    mid_x = (x.max() + x.min()) * 0.5
    mid_y = (y.max() + y.min()) * 0.5
    mid_z = (z.max() + z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    ax.plot(x, y, z, color, label=label)
	
	

def load_data(fname):
    nodes= []

    for line in fname:
        sline = line.split()
        # data_id = int(sline[1]) # unused
        x = float(sline[1])
        y = float(sline[2])
        z = float(sline[3])
        qx = float(sline[4])
        qy = float(sline[5])
        qz = float(sline[6])
        qw = float(sline[7])

        nodes.append(Pose3D(x, y, z, qw, qx, qy, qz))
       
    print("n_nodes:", len(nodes))
    
    return nodes

def main():
    print("start!!")
#file1 = open('data1.txt', "r")
#file2 = open('data2.txt', "r")
file = open(args.data, "r")
#fnames = [file1,file2]
#fnames = file.readlines()
#print(fnames)
#for f in fnames:
#print(f)
nodes= load_data(file.readlines())
        # plot
est_traj_fig = plt.figure(args.title)
ax = est_traj_fig.add_subplot(111, projection='3d')
plot_nodes(nodes, ax, color=args.color, label="data")
plt.legend()
#plt.titre("aref")
plt.pause(0.05)
plt.show()

print("done!!")


if __name__ == '__main__':
    main()
