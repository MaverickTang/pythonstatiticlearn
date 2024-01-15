# -*- coding: utf-8 -*-
import numpy as np

## 定义
# 注意：对于ndarray，所有的元素必须是同一类型，不是则会向下兼容
array=np.array([1,2,3,4,5.0])
# print(help(np.info(np.add)))

## 基本属性操作 
# 普通array不能直接+1
print("----------------基本属性操作-----------------")
print(array+1)
array2=array+array
# 数组大小
print(array.shape)
# 数组类型
print(array.dtype)
# 数据所占字节
print(array.itemsize)
# 全部填为0
array.fill(0)
print(array)
# 注意：非numpy数组直接赋值的话是把位置传过去（指针），但numpy会分配新地址
array2=array
array2=array2+1
print(array)
# 倒序
tang_array = np. arange (10, 50, 1)
tang_array = tang_array[::-1]
print(tang_array)
print("----------------切片与索引-----------------")
## 切片与索引（与python没区别
print(array2[0])
print(array2[1:3])

## 多维形式
print("----------------多维形式-----------------")
twod=np.array([[1,2,3],[4,5,6],[7,8,9]])
# 取一行
print(twod[0,:])#或者twod[0]
# 取一列
print(twod[:,1])
# 用bool类型的数组做mask来筛选
arr=np.arange(0,100,10)
print(arr)
mask=np.array([1,1,1,0,0,1,0,1,0,1],dtype=bool)
mask2=np.random.rand(10)
mask2=mask2>0.5
print(arr[mask])
print(arr[mask2])

## 数组的数值计算
print("----------------数组的数值计算-----------------")
sample=np.array([[1,2,3],[4,5,6]])
# 求和 sum
print(np.sum(sample))
# 给定纬度
print(np.sum(sample, axis=0))
print(np.sum(sample, axis=1))
# 乘积 prod
print(sample.prod())
# 给定纬度
print(sample.prod(axis=0))
print(sample.prod(axis=1))
# 最大最小值
print(sample.min())
print(sample.max())
# 给定纬度
print(sample.min(axis=0))
print(sample.min(axis=1))
# 找索引值
print(sample.argmin())
# 平均值
print(sample.mean())
# 标准差
print(sample.std())
# 方差
print(sample.var())
# 四舍五入
sample=np.array([[1,2,3.56],[4,5,6.41]])
print(sample.round(decimals=1))
# 做限制变化（小于的值变成。。。大于的值变成。。。
print(sample.clip(2,4))

## 排序操作
print("----------------排序操作-----------------")
sample=np.array([[1.5,1.3,7.5],[5.6,7.8,1.2]])
#默认以最后一个轴来排
print(np.sort(sample))
print(np.sort(sample,axis=0))
# 索引值排序（显示排序完的位置
print(np.argsort(sample))
# 插入数组排序
sample=np.linspace(0,10,10)
print(sample)
values=np.array([2.5,6.5,9.5])
# 给出values数组在sample中应该的索引位置，注意，必须把数组排序好
print(np.searchsorted(sample,values))
# 不同列排序规则不同
a = np.array ([[1, 0, 6],[1, 7, 0],[2, 3, 1],[2, 4, 0]])
print(a)
index=np.lexsort([-1*a[:,0],a[:,2]])#按照第1列取所有样本倒序，按照第三列取所有样本升序
a=a[index]
print(a)

## 数组维度操作
print("----------------数组维度操作-----------------")
tang_array=np.arange(10)#从0-10，含左不含右，每隔一个值打印一个数
print(tang_array)
# 将array改成2行，5列
tang_array.shape=2,5
print(tang_array)
# 另一种方法
tang_array=tang_array.reshape(1,10)
print(tang_array)
# 新加维度
# 变成二维 shape 1,10
print(tang_array[np.newaxis,:])
tang_array=np.arange(10)
# 变成一维 shape 10,1
print(tang_array[:,np.newaxis])
# 阔充维度 变成 10,1,1
print(tang_array[:,np.newaxis,np.newaxis])
# 转置
tang_array=np.arange(10)
tang_array.shape=2,5
tang_array=tang_array.transpose()#或者array.T
print(tang_array)

## 数组的拼接 concatenate
print("----------------数组拼接-----------------")
a=np.array([[123,456,789],[3214,456,134]])
b=np.array([[1235,3124,432],[43,13,134]])
c=np.concatenate((a,b))#第一个括号表示传参数，第二个括号表现里面是元组的形式
#默认沿着第一个维度拼接
print(c)
c=np.concatenate((a,b),axis=1)#沿着第二个维度拼接
print(c)
print(np.vstack((a,b)))# 轴=0
print(np.hstack((a,b)))# 轴=1
# 拉平,变成一个长条
print(a.flatten())
print(a.ravel())


## 数组生成函数
print("----------------数组生成函数-----------------")
np.array([1,2,3])
# 生成函数的顺序都是（起始数，终止数，xxx）
np.arange(2,20,2,dtype=np.float32)#后面的2是递进
#自动算每个数的间距，后面是起始与终止间隔了多少个数
np.linspace(0,10,50)
# 默认log space以十为底
print(np.logspace(0,1,5))
# 网格类工具
x=np.linspace(-10,10,5)
y=np.linspace(-10,10,5)
x,y=np.meshgrid(x,y)
print(x)
# 全为0的矩阵
np.zeros(3)
np.zeros((3,3))#多维用元组
# 全为n的矩阵
n=8
np.ones((3,3),dtype=float)*n
# 空值填充
a=np.empty(6)
print(a.shape)
a.fill(1)
# 构造相似矩阵
likematrix=np.array([1,2,3,4])
print(np.zeros_like(likematrix))
np.ones_like(likematrix)
# 单位矩阵
np.identity(5)

## 随机模块
print("----------------随机模块-----------------")
# 构造3X2矩阵，所有值都是从0到1
print(np.random.rand(3,2))
# 构造5X4矩阵，值为0-10(不含右)间的整数
print(np.random.randint(10,size=(5,4)))
# 构造分布
mu, sigma=0,0.1
print(np.random.normal(mu,sigma,10))
# 设置打印精度
np.set_printoptions(precision=3)
print(np.random.normal(mu,sigma,10))
# 洗牌
tang_array = np.arange (10)
np.random.shuffle(tang_array)
print(tang_array)
## 随机种子，设定种子之后下一个随机就是按照当前模式去做，不会有变化
np.random.seed(0)
mu,sigma = 0,0.1
np.random.normal(mu,sigma,10)


