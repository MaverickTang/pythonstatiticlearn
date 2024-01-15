import matplotlib. pyplot as plt 
import numpy as np 
from mpl_toolkits. mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(x, y)# 生成网格数据
Z = np.sin(np.sqrt(X**2 + Y**2))# x^2+y^2
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()

