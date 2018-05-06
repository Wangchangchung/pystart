# Author: Charse

import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from pandas import Series, DataFrame


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

print(ts)
ts = ts.cumsum()

'''
plt.plot(np.arange(20))
plt.show()
'''
plt.plot(np.array([2.5, 4.1, 2.7, 8.8, 1.0]))


# series = Series(np.array([2.5, 4.1, 2.7, 8.8, 1.0]))


# series.plot()

plt.show()


# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))


