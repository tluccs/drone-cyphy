from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
import csv
import sys

fig = plt.figure()
ax = p3.Axes3D(fig)
steps = 100
datax = []
datay = []
dataz = []

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

with open(sys.argv[1], 'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in csvdata:
        if i == 0:
            print(row)
        else:
            datax.append(float(row[1]))
            datay.append(float(row[2]))
            dataz.append(float(row[3]))
        i = i + 1
data = [datax, datay, dataz]
data = np.array(data)
N = len(datax)
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

# Setting the axes properties
ax.set_xlim3d([-1, 1])
ax.set_xlabel('X')

ax.set_ylim3d([-1, 1])
ax.set_ylabel('Y')

ax.set_zlim3d([0, 1])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N, blit=False)
ani.save(sys.argv[1][:-4] + '.mp4', fps=20, dpi=80)
plt.show()

#https://stackoverflow.com/questions/38118598/3d-animation-using-matplotlib
#TY ophir carmi
