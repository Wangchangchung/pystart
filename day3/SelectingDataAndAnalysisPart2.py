# Author: Charse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (15, 5)

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

complaints = pd.read_csv('./data/311-service-requests.csv')

# "Complaint Type"字段为某一类（比如"Noise - Street/Sidewalk"）的数据
noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]
print(noise_complaints[:3])

print("------------------------------")


# complaints['Complaint Type'] == "Noise - Street/Sidewalk"法返回的是一个boolean类型的dataframe
is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
in_brooklyn = complaints['Borough'] == 'BROOKLYN'

# 选出 Complaint Type == 'Noise - Street/Sidewalk'  并且 Borough == 'BROOKLYN' 的数据
print(complaints[is_noise & in_brooklyn][:5])

print("------------------------------")

# 同时我们也可以只查看出指定的一些类数据, 摈弃给只展示出前几条
print(complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10])


# pandas数据的每一列其实是  pd.Series 类型的
print(pd.Series([1, 2, 3]))

# pandas Series底层时numpy数组, 如果你在Series后面加上.values 你就可以得到一个实实在在的numpy数组
print(np.array([1, 2, 3]))

print(pd.Series([1, 2, 3]).values)


arr = np.array([1, 2, 3])

print(arr != 2)

print(arr[arr != 2])


print("------------------------------")
noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()
#  强制类型转换 python默认的整型和整型除法得到的结果还是整型，所以我们最好把 complaint_counts 字段类型转换一下，转成float型的。
print(noise_complaint_counts / complaint_counts.astype(float))