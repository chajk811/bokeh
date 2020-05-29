import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('2020-04-02 모니터링 데이터.csv')
# print(data.head())
# data = data.ix[:9]

arr_MTime = list(map(lambda x: x[11:19], list(data['MTime'])))
arr_MXSineMax = list(data['MXSineMax'])
arr_MXSineAvg = list(data['MXSineAvg'])
arr_MXSineMin = list(data['MXSineMin'])


plt.figure(figsize=(20,5))
# plt.ylim(-0.25, 0.25)

plt.plot(arr_MTime, arr_MXSineMax, 'r', label='MXSineMax')
plt.plot(arr_MTime, arr_MXSineAvg, 'b', label='MXSineAvg')
plt.plot(arr_MTime, arr_MXSineMin, 'g', label='MXSineMin')

plt.xlabel('Mtime')
plt.title('MXSine')
plt.show()
