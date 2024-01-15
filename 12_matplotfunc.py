import matplotlib.pyplot as plt
import numpy as np

## imshow
# imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, shape=None, filternorm=1, filterrad=4.0, imlim=None, resample=None, url=None, *, data=None, **kwargs)
# https://www.runoob.com/matplotlib/matplotlib-imshow.html
# imshow() 函数常用于绘制二维的灰度图像或彩色图像,矩阵、热力图、地图等。

# 随机的彩色图像
# img = np.random.rand(10, 10, 3)
# plt.imshow(img)
# plt.show()
# 灰度gray 热力图hot
img = np.random.rand(10, 10)
plt.imshow(img, cmap='gray')
# 绘制热力图
plt.imshow(img, cmap='hot')
plt.colorbar()# 加上热度映射条
plt.show()

n = 4
# 创建一个 n x n 的二维numpy数组
a = np.reshape(np.linspace(0,1,n**2), (n,n))
plt.figure(figsize=(12,4.5))
# 第一张图展示灰度的色彩映射方式，并且没有进行颜色的混合
plt.subplot(131)
plt.imshow(a, cmap='gray', interpolation='nearest')
plt.xticks(range(n))
plt.yticks(range(n))
# 灰度映射，无混合
plt.title('Gray color map, no blending', y=1.02, fontsize=12)
# 第二张图展示使用viridis颜色映射的图像，同样没有进行颜色的混合
plt.subplot(132)
plt.imshow(a, cmap='viridis', interpolation='nearest')# 采用viridis颜色映射
plt.yticks([])
plt.xticks(range(n))
# Viridis映射，无混合
plt.title('Viridis color map, no blending', y=1.02, fontsize=12)
# 第三张图展示使用viridis颜色映射的图像，并且使用了双立方插值方法进行颜色混合
plt.subplot(133)
plt.imshow(a, cmap='viridis', interpolation='bicubic')# 双立方插值方法
plt.yticks([])
plt.xticks(range(n))
# Viridis 映射，双立方混合
plt.title('Viridis color map, bicubic blending', y=1.02, fontsize=12)
plt.show()

# imsave()
# matplotlib.pyplot.imsave(fname, arr, **kwargs)
# 可选参数，用于指定保存的图像格式以及图像质量等参数。
plt.imsave('imsavetest.png', a)

# imread()
# 返回一个 numpy.ndarray 对象，其形状是 (nrows, ncols, nchannels)，表示读取的图像的行数、列数和通道数：
# 如果图像是灰度图像，则 nchannels 为 1。
# 如果是彩色图像，则 nchannels 为 3 或 4，分别表示红、绿、蓝三个颜色通道和一个 alpha 通道。
img_array = plt.imread('tiger.jpeg')
tiger = img_array/255
#print(tiger)
# 显示图像
plt.figure(figsize=(10,6))
for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') #hide coordinate axes
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)# 通过调整数组大小来使图像变暗
plt.show()
# 裁剪图像
plt.figure(figsize=(6,6))
plt.imshow(tiger[:300,100:400,:])
plt.axis('off')
plt.show()
# 将 RGB 颜色的绿色和蓝色坐标的数组元素设置为0，我们将得到红色的图像
red_tiger[:, :,[1,2]] = 0
plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()






