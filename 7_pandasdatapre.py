import pandas as pd
# 处理的表格包含了四种空值n/a NA — na
df = pd.read_csv('property-data.csv')
print (df['NUM_BEDROOMS'])

## 空值清理
missing_values = ["n/a", "na", "--"]# 指定空数据类型
df = pd.read_csv('property-data.csv', na_values = missing_values)# 读取时即删除
print (df['NUM_BEDROOMS'])
print (df['NUM_BEDROOMS'].isnull())# 可以通过 isnull() 判断各个单元格是否为空


# 使用dropna方法清理空值
# DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
# axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
# how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
# thresh：设置需要多少非空值的数据才可以保留下来的。
# subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
# inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。
df = pd.read_csv('property-data.csv')
new_df = df.dropna()
print(new_df.to_string())

# 可以用fillna()方法替换空字段
df.fillna(12345, inplace = True)
print(df.to_string())
# 替换空单元格的常用方法是计算列的均值、中位数值或众数
x = df["ST_NUM"].mean()# .median() .mode()众数
df["ST_NUM"].fillna(x, inplace = True)
print(df.to_string())


## 格式化错误清理
# data = {
#   "Date": ['2020/12/01', '2020/12/02' , '20201226'],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# df["Date"] = pd.to_datetime(df["Date"])
# print(df.to_string())

## 数据错误
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 200, 12345]    
}
df = pd.DataFrame(person)
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.loc[x, "age"] = 120
# 或者删除
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())

##清洗重复数据
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]  
}
df = pd.DataFrame(person)
print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df)