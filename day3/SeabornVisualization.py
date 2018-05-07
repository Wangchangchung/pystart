# Author: Charse
'''
使用斯坦福大学的seaboarn进行数据可视化操作
'''
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sns.set_style('darkgrid')
names = [
       'mpg'
    ,  'cylinders'
    ,  'displacement'
    ,  'horsepower'
    ,  'weight'
    ,  'acceleration'
    ,  'model_year'
    ,  'origin'
    ,  'car_name'
]
df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data", sep='\s+', names=names)
df['maker'] = df.car_name.map(lambda x: x.split()[0])
df.origin = df.origin.map({1: 'America', 2: 'Europe', 3: 'Asia'})
df = df.applymap(lambda x: np.nan if x == '?' else x).dropna()
df['horsepower'] = df.horsepower.astype(float)
print(df.head())

# 绘制基本的图形, factorplot 折线图
sns.factorplot(data=df, x="model_year", y="mpg")
# 按照是哪个维度进行分析 col= 以区域作为一个维度
sns.factorplot(data=df, x="model_year", y="mpg", col="origin")
# cylinders 换成柱状图
sns.factorplot("cylinders", data=df, col="origin", kind='bar')

# 绘制散点图   横坐标为mpg
g = sns.FacetGrid(df, col="origin")
g.map(sns.distplot, "mpg")

# 绘制散点图,横坐标为horsepower, 纵坐标为mpg
g = sns.FacetGrid(df, col="origin")
g.map(plt.scatter, "horsepower", "mpg")

# 绘图的同时还做回归   sns.regplot
g = sns.FacetGrid(df, col="origin")
g.map(sns.regplot, "horsepower", "mpg")
# 对左边的横纵坐标进行限制
plt.xlim(0, 250)
plt.ylim(0, 60)

# 绘制等高线
df['tons'] = (df.weight/2000).astype(int)
g = sns.FacetGrid(df, col="origin", row="tons")
g.map(sns.kdeplot, "horsepower", "mpg")
plt.xlim(0, 250)
plt.ylim(0, 60)

# 按照两个维度进行绘图
g = sns.FacetGrid(df, col="origin", row="tons")
g.map(plt.hist, "mpg", bins=np.linspace(0, 50, 11))

# 多个维度两两组合绘图
g = sns.pairplot(df[["mpg", "horsepower", "weight", "origin"]], hue="origin", diag_kind="hist")
for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45)

# 组合绘图的时候顺便做一下回归预测
g = sns.PairGrid(df[["mpg", "horsepower", "weight", "origin"]], hue="origin")
g.map_upper(sns.regplot)
g.map_lower(sns.residplot)
g.map_diag(plt.hist)
for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=45)
g.add_legend()
g.set(alpha=0.5)

# 联合绘图(kde等高)
sns.jointplot("mpg", "horsepower", data=df, kind='kde')

#  联合绘图(加回归)
sns.jointplot("horsepower", "mpg", data=df, kind="reg")

#
g = sns.JointGrid(x="horsepower", y="mpg", data=df)
g.plot_joint(sns.regplot, order=2)
g.plot_marginals(sns.distplot)

plt.show()

