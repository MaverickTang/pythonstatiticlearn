import numpy as np

x=np.array([3,5])
y=np.array([1,2])
# 对应相乘
print(np.multiply(x,y))
# 相乘相加
print(np.dot(x,y))
# 注意点乘顺序不同答案不同
x.shape=2,1
y.shape=1,2
print(np.dot(x,y))
print(np.dot(y,x)) 
x = np.array([1, 2, 1])
y = np.array([[1,2,3],[4,5,6]])
print(x*y)
# 逻辑处理
y = np. array ([1, 1, 1, 4])
x = np. array ([1, 1, 1, 1])
print(x==y)
print(np.logical_and(x,y))
print(np.logical_or(x,y))
print(np.logical_not(x,y))

