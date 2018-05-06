# Author: Charse
import numpy
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

# 对时间维度进行相关的分析
bikes = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
bikes['Berri 1'].plot()

## 区分时工作日还是周末

# index_col表示的是索引的字段

berri_bikes = bikes[['Berri 1']].copy()

print("------------------------------------")
# 查看索引列的数据
print(berri_bikes.index)

print("------------------------------------")
# 索引列的数据时date对象,所以可以通过 .day可以直接看到是一个月的第几天
print(berri_bikes.index.day)

print("------------------------------------")

# 其实dataframe对于日期类型的数据，可以直接知道是星期几
print(berri_bikes.index.weekday)

# 增加一个 weekday 周末的这个字段
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

print("------------------------------------")
print(berri_bikes[:5])

##  分组 + 排序 + 聚合统计

# 用过SQL里面的groupby吗，恰巧pandas的dataframe也有一个.groupby()函数
print("------------------------------------")
# 下面的操作就是: 将数据按照星期几分一下组, 然后再求和放回给我
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print(weekday_counts)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(weekday_counts)

print("------------------------------------")
# 求每一中的最大值
print(berri_bikes.groupby('weekday').aggregate(max))
print("------------------------------------")
print(berri_bikes.groupby('weekday').aggregate(numpy.median))




