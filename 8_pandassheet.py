import pandas as pd
import numpy as np
## 数据透视表
example = pd.DataFrame({'Month': ["January", "January", "January", "January","February", "February", "February", "February","March","March","March","March"],
'Category': ["Transportation","Grocery", "Household", "Entertainment", "Transportation","Grocery", "Household", "Entertainment", "Transportation","Grocery", "Household", "Entertainment"],
'Amount': [74., 235., 175., 100., 115., 240., 225., 125., 90., 260., 200., 120.]})
print(example)
example_pivot = example.pivot(index = 'Category', columns= 'Month', values = 'Amount')
print(example_pivot)
print(example_pivot.sum(axis = 0))
# 注意使用pandas.Timestamp时间索引

# Pandas绘图
print('-------------------Drawing------------------------')
s = pd.Series(np.random.rand(10), index=np.arange(0, 100, 10))
s.plot()#只有在interactive window有图片