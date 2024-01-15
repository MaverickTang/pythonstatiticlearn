import numpy as np
## 读数据
data=[]
with open('test.txt') as f:
    for line in f.readlines():
        fields=line.split()
        cur_data=[float(x) for x in fields]
        data.append(cur_data)
data=np.array(data)
print(data)
# 指定分隔符读取（只有,的话）,第一行有其他变量的话可以指定跳过
data=np.loadtxt('test2.txt',delimiter=',', skiprows=1)
print(data)
# 'tang2.txt’：路径最好放到和代码一起
# skiprows ：去掉几行
#  delimiter =：分隔符
# usecols = （0, 1, 4）：指定使用哪几列

## 存储数据
data=np. array ([[1, 2, 3], [4, 5, 6]])
np.savetxt ('test3. txt', data)
np.savetxt ('test4. txt', data, fmt=' %d')
np.savetxt ('test5. txt', data, fmt=' %.2f', delimiter = ',')

## 读写array结构,使用npy数据格式
tang_array = np. array ([[1, 2, 3], [4, 5, 6]])
np.save ('tang_array.npy', tang_array)
tang = np.load ('tang_array.npy' )
print(tang)
tang_array2 = np.arange (10)
np. savez ('tang_array.npz', a=tang_array, b=tang_array2)
data = np.load('tang_array.npz')
print(data. keys())
print(data['a'])