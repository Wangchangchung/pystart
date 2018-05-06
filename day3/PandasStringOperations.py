# Author: Charse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



weather_2012 = pd.read_csv('./data/weather_2012.csv', parse_dates=True, index_col='Date/Time')

print(weather_2012[:5])

print("-----------------------------------------")
# 字符串基本操作
weather_description = weather_2012['Weather']
# 查看字符串类型的时字段中是否包含有 snow
is_snowing = weather_description.str.contains('Snow')
print(is_snowing[:5])
# is_snowing.astype(float).plot()
# 平均气温
# 如果我们想知道每个月的温度值中位数，有一个很有用的函数可以调用哈，叫 resample() 取样

weather_2012['Temp (C)'].resample('M', how=np.median).plot(kind='bar')

print("-----------------------------")
is_snowing.astype(float).resample('M', how=np.mean).plot(kind='bar')

# plt.show()


temperature = weather_2012['Temp (C)'].resample('M', how=np.median)
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M', how=np.mean)

# 给列取一个名字
temperature.name = "Temperature"
snowiness.name = "Snowiness"

# 用 concat 把这两列拼接到一列中，组成一个新的dataframe
stats = pd.concat([temperature, snowiness], axis=1)
print(stats)

# 你这2个维度的幅度是不一样的，所以要分开画哦; subplots=True  分别显示
stats.plot(kind='bar', subplots=True, figsize=(15, 10))

plt.show()
