# Author: Charse

import pandas
import matplotlib.pyplot as plt
import numpy

# 调用pandas工具包的read_csv函数/模块, 传入训练文件地址参数, 获得返回的数据保存至变量df_train
df_train = pandas.read_csv('./Datasets/breast-cancer-train.csv')
# 传入测试文件地址参数, 获得返回的数据保存至变量df_test
df_test = pandas.read_csv('./Datasets/breast-cancer-test.csv')

# 选取 'Clump Thickness' 与 'Cell Size'作为特征。构建测试集中的正负分类样本
df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]

# 绘制良性肿瘤样本点 标记为o, 设置大小和颜色
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
# 绘制恶性肿瘤样本点 标记为x, 设置大小和颜色
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=150, c='black')

# 设置x, y轴的说明
plt.xlabel('ClumpThickness')
plt.ylabel('Cell Size')

# 设置截聚返回一个size = 1(random.random(size=(3, 2))) 的列表
# numpy.random.random 取值为随机生成一个0.0-1.0的浮点数
intercept = numpy.random.random([1])
print("intercept:", intercept)

# [0.75362834 0.09331885]  将两者变成斜率
coef = numpy.random.random([2])
print("coef", coef)

# 获取0-11的12个整数  返回的是一个矩阵对象而不是一个列表
lx = numpy.arange(0, 12)

ly = (-intercept - lx*coef[0])/coef[1]
''''
绘制的直线
y = -(coef[0]/coef[1])* x - intercept/coef[1] 
'''
print("lx:", lx)
print("ly:", ly)
# 绘制2d直线
'''
lx: [ 0  1  2  3  4  5  6  7  8  9 10 11]
ly: [-0.10559902 -0.45859319 -0.81158735 -1.16458152 -1.51757568 -1.87056985
 -2.22356402 -2.57655818 -2.92955235 -3.28254652 -3.63554068 -3.98853485]
 
 各个点(0, -0.105), (1,-0.458), (2, -0.811)...
'''
plt.plot(lx, ly, c='yellow')
# 显示图片
plt.show()
