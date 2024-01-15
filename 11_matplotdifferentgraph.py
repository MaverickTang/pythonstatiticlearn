import matplotlib.pyplot as plt
import numpy as np

## 散点图
# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
# x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。
# s：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。
# c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
# marker：点的样式，默认小圆圈 'o'。
# cmap：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap。
# norm：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。
# vmin，vmax：：亮度设置，在 norm 参数存在时会忽略。
# alpha：：透明度设置，0-1 之间，默认 None，即不透明。
# linewidths：：标记点的长度。
# edgecolors：：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。
# plotnonfinite：：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。
# **kwargs：：其他参数。
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([1, 4, 9, 16, 7, 11, 23, 18])

# 普通用法
plt.scatter(x, y)
# 设置图标大小
sizes = np.array([20,50,100,200,500,1000,60,90])
plt.scatter(x, y, s=sizes)
# 自定义点的颜色
colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
plt.scatter(x, y, c=colors)
# 设置多组点
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color = 'hotpink')
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color = '#88c999')
plt.show()

## 柱形图 bar
# matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
# x：浮点型数组，柱形图的 x 轴数据。
# height：浮点型数组，柱形图的高度。
# width：浮点型数组，柱形图的宽度。
# bottom：浮点型数组，底座的 y 坐标，默认 0。
# align：柱形图与 x 坐标的对齐方式，'center' 以 x 位置为中心，这是默认值。 'edge'：将柱形图的左边缘与 x 位置对齐。要对齐右边缘的条形，可以传递负数的宽度值及 align='edge'。
# **kwargs：：其他参数。
x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
y = np.array([12, 22, 6, 18])
# 一般使用
plt.bar(x,y)
# 垂直方向的柱形图可以使用 barh() 方法来设置
plt.barh(x,y)
# 定义各个柱状图颜色
plt.bar(x, y, color = ["#4CAF50","red","hotpink","#556B2F"])
# 设置柱形图宽度，bar() 方法使用 width 设置，barh() 方法使用 height 设置 height
plt.bar(x, y, width = 0.1)
plt.show()


## 饼图 pie
# matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]
# https://www.runoob.com/matplotlib/matplotlib-pie.html 现查资料画吧

# 普通
# y = np.array([35, 25, 25, 15])
# plt.pie(y)
# 加参数
sizes = [15, 30, 45, 10]
# 饼图的标签，颜色
labels = ['A', 'B', 'C', 'D']
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# 突出显示第二个扇形
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("RUNOOB Pie Test")
plt.show()

## 直方图
# matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)
# https://www.runoob.com/matplotlib/matplotlib-hist.html 现查资料画吧
# 多组数据直方图（一组就只有一个）
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)
# 绘制直方图
# bins 参数为 30，这意味着将数据范围分成 30 个等宽的区间，然后统计每个区间内数据的频数
# alpha 参数为 0.5，这意味着每个直方图的颜色透明度为 50%
# label 参数设置了每个直方图的标签，以便在图例中显示
plt.hist(data1, bins=30, alpha=0.5, label='Data 1')
plt.hist(data2, bins=30, alpha=0.5, label='Data 2')
plt.hist(data3, bins=30, alpha=0.5, label='Data 3')
plt.title('RUNOOB hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
#  legend() 函数显示图例
plt.legend()
# 显示图表
plt.show()

# 结合pandas
# 可以使用 Pandas 中的 dataFrame，Series 对象绘制直方图
random_data = np.random.normal(170, 10, 250)# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)
dataframe.hist()# 使用 Pandas hist() 方法绘制直方图
plt.title('RUNOOB hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')
plt.show()

