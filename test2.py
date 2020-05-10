import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import csv

# ------------------------------
# data = pd.read_csv('2020-04-02 모니터링 데이터.csv')
# tmp = pd.DataFrame({'MTime': data['MTime'], 'MXSineMax': data['MXSineMax'], 'MXSineAvg': data['MXSineAvg'], 'MXSineMin': data['MXSineMin']})

# data.plot(x='MTime', y='MXSineMax')
# data.plot(x='MTime', y='MXSineAvg', color='r')
# data.plot(x='MTime', y='MXSineMin', color='g')

# tmp.plot(x='MTime')
# plt.show()

# ---------------------
data = pd.read_csv('2020-04-02 모니터링 데이터.csv')

sensor_5 = data[data['GHID'] == 5]
# print(sensor_5.head())
# print(sensor_5.shape)

# 센서별 변수 선언
# sensor_6 = data[data['GHID'] == 6]
# sensor_7 = data[data['GHID'] == 7]
# sensor_8 = data[data['GHID'] == 8]

# MXSineMax, Avg, Min 세개 한번에 그린 그래프
kind = ['Sine', 'Acel']
d = ['X', 'Y', 'Z']

tmp =  pd.DataFrame({'MTime': sensor_5['MTime'], 'MXSineMax': sensor_5['MXSineMax'], 'MXSineAvg': sensor_5['MXSineAvg'], 'MXSineMin': sensor_5['MXSineMin']})
# tmp =  pd.DataFrame({'MTime': sensor_5['MTime'], 'MYSineMax': sensor_5['MYSineMax'], 'MYSineAvg': sensor_5['MYSineAvg'], 'MYSineMin': sensor_5['MYSineMin']})
# tmp =  pd.DataFrame({'MTime': sensor_5['MTime'], 'MXAcelMax': sensor_5['MXAcelMax'], 'MXAcelAvg': sensor_5['MXAcelAvg'], 'MXAcelMin': sensor_5['MXAcelMin']})
# tmp =  pd.DataFrame({'MTime': sensor_5['MTime'], 'MYAcelMax': sensor_5['MYAcelMax'], 'MYAcelAvg': sensor_5['MYAcelAvg'], 'MYAcelMin': sensor_5['MYAcelMin']})
# tmp =  pd.DataFrame({'MTime': sensor_5['MTime'], 'MZAcelMax': sensor_5['MZAcelMax'], 'MZAcelAvg': sensor_5['MZAcelAvg'], 'MZAcelMin': sensor_5['MZAcelMin']})

tmp.plot(x='MTime', figsize=(20,15), ylim=(-0.06, 0.06))

# MXSineMas 한개만
# sensor_5.plot(x='MTime', y='MXSineMax')

plt.show()