import numpy as np
import matplotlib.pyplot as plt
import matplotlib

x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
# 普通画图
# plt.plot([1,2,3,4,5],[1,2,3,4,5],'o') 
# # 颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。
# # 线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
# # 标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。
# plt.xlabel('xlabel',fontsize=16)
# plt.ylabel('ylabel',fontsize=16)
# plt.show()#没有show()不会放出来
# 画多个曲线
# plt.plot(x,y,x,z)
# plt.show()

## 绘图标签
## fmt参数
####     可以用plot.style设置风格来让图片更好看      ####
ypoints = np.array([6, 2, 13, 10])
# fmt = '[marker][line][color]'
## 标记大小与颜色
# o 表示实心圆标记，: 表示虚线，r 表示颜色为红色
# plt.plot(ypoints, 'o:r')
# 我们可以自定义标记的大小与颜色，使用的参数分别是：
# markersize，简写为 ms：定义标记的大小。
# markerfacecolor，简写为 mfc：定义标记内部的颜色。
# markeredgecolor，简写为 mec：定义标记边框的颜色。
# 定义大小与边框颜色
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# 自定义内部与边框颜色
plt.plot(x,y,x,z, marker = 'o', ms = 2, mec = '#4CAF50', mfc = '#4CAF50')

## 轴标签与标题
# fontdict 可以使用 css 来设置字体样式
plt.title("菜鸟教程 - 测试",loc="left") 
# fontproperties 设置中文显示，fontsize 设置字体大小
plt.xlabel("x 轴", loc="left")
plt.ylabel("y 轴", loc="top")

## 网格线
# matplotlib.pyplot.grid(b=None, which='major', axis='both', )
# b：可选，默认为 None，可以设置布尔值，true 为显示网格线，false 为不显示，如果设置 **kwargs 参数，则值为 true。
# which：可选，可选值有 'major'、'minor' 和 'both'，默认为 'major'，表示应用更改的网格线。
# axis：可选，设置显示哪个方向的网格线，可以是取 'both'（默认），'x' 或 'y'，分别表示两个方向，x 轴方向或 y 轴方向。
# **kwargs：可选，设置网格样式，可以是 color='r', linestyle='-' 和 linewidth=2，分别表示网格线的颜色，样式和宽度。
# 普通网格线
# plt.grid()
# 设置x就在y轴方向显示网格线
plt.grid(axis='x') 
# 设置网格线的颜色，样式，宽度
plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)


plt.show()

##  颜色条
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
# 需要使用 cmap 参数，默认值为 'viridis'，之后颜色值设置为 0 到 100 的数组
# 换个颜色条参数， cmap 设置为 afmhot_r等（可查网上
plt.scatter(x, y, c=colors, cmap='viridis')
# 如果要显示颜色条，需要使用 plt.colorbar()
plt.colorbar()
plt.show()






