import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 5000)
plt.rcParams['figure.figsize'] = (15, 5)

complaints = pd.read_csv('./data/311-service-requests.csv', parse_dates=['Created Date', 'Closed Date', 'Due Date', 'Resolution Action Updated Date'])

# dataframe这种格式 会告诉你很多基本信息
# print(complaints)
# 选择 行或者列
# print(complaints['Complaint Type'])

# print(complaints[:5])

# 将前面的进行合并一下,两者是等效的
print(complaints['Complaint Type'][:5])
print(complaints[:5]['Complaint Type'])

# 选择多列  里面时一个列表
print(complaints[['Unique Key', 'Agency']])


# 选择多列的前几行
print(complaints[['Unique Key', 'Agency']][:5])

# dataframe 是非常智能的,  通过 value_counts() 可以统计出每列某种的统计
print(complaints['Complaint Type'].value_counts())

# 通过value_counts是将所有的进行统计, 如果只需要 top10的数据那么就可以先存储起来再进行
# 列表的获取
complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]

# ki
complaint_counts[:10].plot(kind='bar')

plt.show()




