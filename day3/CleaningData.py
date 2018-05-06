# Author: Charse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

requests = pd.read_csv('./data/311-service-requests.csv')

'''
怎么找到脏数据?
其实也没有特别好的办法，还是得先拿点数据出来看看。比如说我们这里观察到邮政编码可能有问题的字段。
需要提到的一点是 .unique() 函数有很巧的用处，我们把所有出现过的邮政编码列出来（之后再看看分布？），也许会有一些想法。

下面我们就把unique()用起来，然后你会发现，确确实实是存在一些问题的，比如：

为什么大部分被解析出数值，而有些被解析出字符串了？
- 好多缺省值（nan）
- 格式不一样，有些是29616-0759，有些是83
- 有一些pandas不认的，比如'N/A'或者'NO CLUE'

那我们能做什么呢？
- 规整'N/A'和'NO CLUE'到缺省值的“队列”里
- 看看83是什么鬼，然后再决定怎么处理
- 统一一下，全处理成字符串好啦
'''

print(requests['Incident Zip'].unique)

## 处理缺省值
'''
pd.read_csv读数据的时候，传一个na_values给它，清理掉一部分的脏数据，我们还可以指明说，我们就要保证邮政编码是字符串型的，
不要给我整些数值型出来！！
'''
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('./data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})

# 这样我们读取出的数据就是比较好的数据
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
print(len(requests[rows_with_dashes]))

# 对 Incident Zip中的数据进行设置为 nan 这个对数据做清洗
zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan