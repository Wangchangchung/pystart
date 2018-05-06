# Author: Charse
import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt

# 因为文件中的数据时以空格的形式分离的,  设置读取时候选择用空格, 并且最后一行时不相关的数据
# 所以最后一行不选择取
popular = pd.read_csv('./data/popularity-contest', sep=' ')[:-1]
# 给定列名
popular.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

print(popular[:5])
'''
读取的数据时: 
        atime       ctime  package-name  
0  1387295797  1367633260     perl-base   
1  1387295796  1354370480         login   
2  1387295743  1354341275    libtalloc2   
3  1387295743  1387224204  libwbclient0   
4  1387295742  1354341253   libselinux1   

所以, 将事件转换成我们好看的格式
'''
# 先转换成整数
popular['atime'] = popular['atime'].astype(int)
popular['ctime'] = popular['ctime'].astype(int)

popular['atime'] = pd.to_datetime(popular['atime'], unit='s')
popular['ctime'] = pd.to_datetime(popular['ctime'], unit='s')

# datetime64[ns]
print(popular['atime'].dtype)

#这样我们的前面的两个字段就变成正常的时间格式的
print(popular[0:5])

popular = popular[popular['atime'] > '1970-01-01']
nonlibraries = popular[~popular['package-name'].str.contains('lib')]

print(nonlibraries.sort('ctime', ascending=False)[:10])







