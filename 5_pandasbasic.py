# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
# print(pd.__version__ )

## Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型
print('-----------------Series--------------------')
# 创建
# pandas.Series( data, index, dtype, name, copy)
# data：一组数据(ndarray 类型)。
# index：数据索引标签，如果不指定，默认从 0 开始。
# dtype：数据类型，默认会自己判断。
# name：设置名称。
# copy：拷贝数据，默认为 False。
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
# 指定索引值创建
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar["y"])
# 类似字典的创建方式
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)
# Series基本操作
a=[1,2,3]
series=pd.Series(a)
# 获取值
value = series[2]  # 获取索引为2的值
# 获取多个值
subset = series[1:4]  # 获取索引为1到3的值
# 使用自定义索引
series_with_index = pd.Series(a, index = ["b", "y", "z"])
value = series_with_index['b']  # 获取索引为'b'的值
# 索引和值的对应关系
for index, value in series_with_index.items():
    print(f"Index: {index}, Value: {value}")
# 基本运算
# 算术运算
result = series * 2  # 所有元素乘以2
# 过滤
filtered_series = series[series > 2]  # 选择大于2的元素
# 数学函数
result = np.sqrt(series)  # 对每个元素取平方根
# 属性与方法
# 获取索引
index = series_with_index.index
# 获取值数组
values = series_with_index.values
# 获取描述统计信息
stats = series_with_index.describe()
# 获取最大值和最小值的索引
max_index = series_with_index.idxmax()
min_index = series_with_index.idxmin()

## DataFrame
print('-----------------Data Frame--------------------')
# 创建
# pandas.DataFrame( data, index, columns, dtype, copy)
# data：一组数据(ndarray、series, map, lists, dict 等类型)。
# index：索引值，或者可以称为行标签。
# columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
# dtype：数据类型。
# copy：拷贝数据，默认为 False。
# 用数组创建
data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'])
print(df)
# 用ndarray创建
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)
# 用字典创建
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)# 没有对应的部分数据为 NaN。
# 返回数据其中一行（其实就是一个pandas series数据
# 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print(df.loc[0])
# 返回第一行和第二行（使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开
print(df.loc[[0, 1]])

# ## 读取数据
# pd.read_csv(filename)	读取 CSV 文件；
# pd.read_excel(filename)	读取 Excel 文件；
# pd.read_sql(query, connection_object)	从 SQL 数据库读取数据；
# pd.read_json(json_string)	从 JSON 字符串中读取数据；
# pd.read_html(url)	从 HTML 页面中读取数据。
# ## 查看数据
# df.head(n)	显示前 n 行数据；
# df.tail(n)	显示后 n 行数据；
# df.info()	显示数据的信息，包括列名、数据类型、缺失值等；
# df.describe()	显示数据的基本统计信息，包括均值、方差、最大值、最小值等；
# df.shape	显示数据的行数和列数。
# ## 数据清洗
# df.dropna()	删除包含缺失值的行或列；
# df.fillna(value)	将缺失值替换为指定的值；
# df.replace(old_value, new_value)	将指定值替换为新值；
# df.duplicated()	检查是否有重复的数据；
# df.drop_duplicates()	删除重复的数据。
# ## 数据选择与切片
# df[column_name]	选择指定的列；
# df.loc[row_index, column_name]	通过标签选择数据；
# df.iloc[row_index, column_index]	通过位置选择数据；
# df.ix[row_index, column_name]	通过标签或位置选择数据；
# df.filter(items=[column_name1, column_name2])	选择指定的列；
# df.filter(regex='regex')	选择列名匹配正则表达式的列；
# df.sample(n)	随机选择 n 行数据。
# ## 数据排序
# df.sort_values(column_name)	按照指定列的值排序；
# df.sort_values([column_name1, column_name2], ascending=[True, False])	按照多个列的值排序；
# df.sort_index()	按照索引排序。
# ## 数据分组与聚合
# df.groupby(column_name)	按照指定列进行分组；
# df.aggregate(function_name)	对分组后的数据进行聚合操作；
# df.pivot_table(values, index, columns, aggfunc)	生成透视表。
# ## 数据合并
# pd.concat([df1, df2])	将多个数据框按照行或列进行合并；
# pd.merge(df1, df2, on=column_name)	按照指定列将两个数据框进行合并。
# ## 数据选择和过滤
# df.loc[row_indexer, column_indexer]	按标签选择行和列。
# df.iloc[row_indexer, column_indexer]	按位置选择行和列。
# df[df['column_name'] > value]	选择列中满足条件的行。
# df.query('column_name > value')	使用字符串表达式选择列中满足条件的行。
# ## 数据统计和描述
# df.describe()	计算基本统计信息，如均值、标准差、最小值、最大值等。
# df.mean()	计算每列的平均值。
# df.median()	计算每列的中位数。
# df.mode()	计算每列的众数。
# df.count()	计算每列非缺失值的数量。

