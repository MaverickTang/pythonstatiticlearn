# -*- coding: utf-8 -*-
import pandas as pd
import json

## csv操作
print('---------------------csv操作---------------------------')

##读取csv
df = pd.read_csv('nba.csv')
# to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
# print(df.to_string())
# 直接打出会让表格中间省略
print(df)
##存储csv
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
# 字典
dict = {'name': nme, 'site': st, 'age': ag}  
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')

##数据处理
df = pd.read_csv('nba.csv')
# info() 方法返回表格的一些基本信息
print(df.info())
# head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行
print(df.head())
# tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。
print(df.tail())


## JSON操作
# 可以直接将 Python 字典转化为 DataFrame 数据，
print('---------------------JSON操作---------------------------')
# 读取json
df = pd.read_json('sites.json')
# to_string() 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串
print(df.to_string())
##读取 JSON 并转为 DataFrame 
# 直接处理JSON字符串（将其转换为dataframe
data=[{
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    }]
df = pd.DataFrame(data)
print(df) 
# 字典格式的 JSON                                                                                              
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}
                                                                                         
df = pd.DataFrame(s)
print(df)
# 用 json_normalize() 方法将内嵌的数据完整的解析出来
with open('nested_list.json','r') as f:
    data=json.loads(f.read())# 使用 Python JSON 模块载入数据
# json_normalize() 使用了参数 record_path 并设置为 ['students'] 
# 用于展开内嵌的 JSON 数据 students。
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)
# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数
# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)