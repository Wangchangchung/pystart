# Author: Charse

import pandas
import matplotlib.pyplot as plt
import numpy
# sklear包是依赖scipy, 所以环境中必须安装了scipy
from sklearn.linear_model import LogisticRegression


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
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')

lr = LogisticRegression()

# 将所有的训练样本学习直线模型, 得到直线的系统和截据
lr.fit(df_train[['Clump Thickness', 'Cell Size']], df_train['Type'])

print(lr.score(df_test[['Clump Thickness', 'Cell Size']], df_test['Type']))

# 从模型中获取截据
intercept = lr.intercept_
# 从模型中获取系统,一般是两个
coef = lr.coef_[0, :]

lx = numpy.arange(0, 12)
ly = (-intercept-lx*coef[0])/coef[1]

plt.plot(lx, ly, c='blue')
plt.show()


