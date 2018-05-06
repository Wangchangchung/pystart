# Author: Charse

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

broken_df = pd.read_csv('./data/bikes.csv', encoding='latin1')

# pd.set_option('display.mpl_style', 'default')
#plt.rcParams['figure.figsize'] = (15, 5)

# 输出前三列
print(broken_df[:3])

# 对数据进行格式化
'''
设置编码格式, 设置分割符, 对日期进行格式化, 设置第一列, 按照'Date'字段进行排序
用pandas读取完CSV文件呢, 我们会得到一个叫做DataFrame的对象，由行和列组成类似上面的excel(说废话的感觉)。
可以像下面这样通过列名取出其中的某一列。
'''
fixed_df = pd.read_csv('./data/bikes.csv', encoding='latin1', sep=';', dayfirst=True, parse_dates=['Date'],
                        index_col='Date')
print(fixed_df)

# 绘制指定某一列的数据
'''
The plot method on Series and DataFrame is just a simple wrapper around plt.plot():
'''
fixed_df['Berri 1'].plot()

fixed_df.plot(figsize=(15, 10))

# 图像显示, plot只是绘制在内存中,在界面中显示时需要借助pyplot ,显示的时将会前面的两张图片都显示出来
plt.show()


