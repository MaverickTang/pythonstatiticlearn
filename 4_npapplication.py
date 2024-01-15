import numpy as np
## 拓展内容
# 构造一个5*5的矩阵，令其值都为1，并在最外层加上一圈0
tang_array = np.ones((5,5))
tang_array = np.pad(tang_array, pad_width = 1, mode = 'constant', constant_values = 0)
print(tang_array)

# 构建一个shape为（6，7，8）的矩阵，并找到第100个元素的索引值
np.unravel_index (100, (6, 7, 8))

# 归一化操作
tang_array = np. random. random((5, 5))
tang_max = tang_array. max()
tang_min = tang_array. min()
tang_array = (tang_array-tang_min)/ (tang_max- tang_min)
print(tang_array)

# 找到两个数组中相同的值
z1 = np. random. randint (0, 10, 10)
z2 = np. random. randint (0, 10, 10)
print (z1)
print (z2)
print(np.intersect1d(z1, z2))

# 得到今天明天昨天的日期
yesterday = np.datetime64 ('today', 'D') - np.timedelta64(1, 'D' )
today = np.datetime64 ('today', 'D' )
tommorow = np.datetime64 ('today', 'D' ) + np.timedelta64 (1, 'D')
print(today)

# 得到一个月天数
np.arange (' 2017-10',' 2017-11', dtype='datetime64[D]')

# 得到一个数的整数部分
z = np.random.uniform (0, 10, 10)
np.floor(z)

# 打印大数据的部分值，全部值
np.set_printoptions(threshold=5)
z = np.zeros( (15, 15))
print(z)

# 找到在一个数组中，最接近一个数的索引
z = np.arange(100)
v = np.random.uniform(0, 100)
print(v)
print(z[(np.abs(z-v)).argmin()])

# 统计数组中每个数值出现的次数
z = np.array([1, 1, 1, 2, 2, 3, 3, 4, 5, 8])
print(np.bincount(z))


# 何对一个四维数组的最后两维来求和
z = np.random.randint (0, 10, (4, 4, 4, 4))
res = z.sum(axis= (-2, -1))