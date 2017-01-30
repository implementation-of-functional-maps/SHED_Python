import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3, 0.25)
y = np.arange(-3, 3, 0.25)

X, Y = np.meshgrid(x, y)
print("x=" , x)
print("X=" , X)
print("y=" , y)
print("Y=" , Y)

x = np.arange(-3, 3, 0.25)
y = np.arange(-3, 3, 0.25)
X, Y = np.meshgrid(x, y)
Z = np.sin(X)+ np.cos(Y)

fig = plt.figure()
ax = mpl_toolkits.mplot3d.Axes3D(fig)
ax.plot_wireframe(X,Y,Z)

plt.show()
