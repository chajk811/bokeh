import datetime

import pandas as pd
from scipy.signal import savgol_filter

from bokeh.io import show, curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import Blues4
from bokeh.plotting import figure

## 예시 => 잘 나오는지 확인
# df = pd.read_csv('2020-04-02 모니터링 데이터.csv')
# df.index = pd.to_datetime(df['MTime'])
# df = df.drop('MTime', axis=1)
# print(df.head())

# plot = figure(plot_width=700, plot_height=300, x_axis_type='datetime')
# plot.line(df.index, df['MXSineMax'], color='navy', alpha=0.5)
# show(plot)

## --------------------
STATISTICS = [
    'MXSineMax', 'MXSineAvg', 'MXSineMin',
    'MYSineMax', 'MYSineAvg', 'MYSineMin',
    'MXAcelMax', 'MXAcelAvg', 'MXAcelMin',
    'MYAcelMax', 'MYAcelAvg', 'MYAcelMin',
    'MZAcelMax', 'MZAcelAvg', 'MZAcelMin',
]

def get_dataset(src, sensor_id_num, sensor_kind_name, distribution):
    # sensor_kind_name 은 X, Y dict or X, Y, Z dict 형태로 들어온다.
    df = src[src.GHID == sensor_id_num].copy()
    df['MTime'] = pd.to_datetime(df.MTime)
    df['left'] = df.MTime - datetime.timedelta(minutes=0.5)
    df['right'] = df.MTime + datetime.timedelta(minutes=0.5)
    df = df.set_index(['MTime'])
    df.sort_index(inplace=True)
    if distribution == 'smoothed':
        window, order = 51, 3
        for key in STATISTICS:
            df[key] = savgol_filter(df[key], window, order)

    return ColumnDataSource(data=df)

def make_plot(source, title):
    plot = figure(plot_width=800, x_axis_type='datetime', tools='', toolbar_location=None)
    plot.title.text = title

    plot.quad(top='MXSineMax', bottom='MXSineMin', left='left', right='right',
              color=Blues4[2], source=source, legend_label='MXSine')
    '''
    plot.quad(top='MYSineMax', bottom='MYSineMin', left='left', right='right',
              color=Blues4[0], source=source, legend_labal='MYSine')
    '''
    return plot


def update_plot():
    pass


# 기본값 설정
sensor_id = 'ID201'
sensor_kind = 'Tilt'
distribution = 'Discrete'

# 일단 어떤 센서ID가 어떤 번호인지 모르니
# ID 201, 202, 203, 204 => 5, 6, 7, 8
sensor_id_dict = {
    'ID201': {
        'GHID': 5,
        'title': 'ID201 sensor',
    },
    'ID202': {
        'GHID': 6,
        'title': 'ID202 sensor',
    },
    'ID203': {
        'GHID': 7,
        'title': 'ID203 sensor',
    },
    'ID204': {
        'GHID': 8,
        'title': 'ID201 sensor',
    },
}

sensor_kind_dict = {
    'Tilt': {
        'X': ['MXSineMax', 'MXSineAvg', 'MXSineMin'],
        'Y': ['MYSineMax', 'MYSineAvg', 'MYSineMin'],
    },
    'Acel': {
        'X': ['MXAcelMax', 'MXAcelAvg', 'MXAcelMin'],
        'Y': ['MYAcelMax', 'MYAcelAvg', 'MYAcelMin'],
        'Z': ['MZAcelMax', 'MZAcelAvg', 'MZAcelMin'],
    },
}

sensor_id_select = Select(value=sensor_id, title='sensor_id', options=sorted(sensor_id_dict.keys()))
sensor_kind_select = Select(value=sensor_kind, title='sensor_kind', options=sorted(sensor_kind_dict.keys()))
distribution_select = Select(value=distribution, title='distribution', options=['discrete', 'smoothed'])

# 그래프 그리는 부분
df = pd.read_csv('2020-04-02 모니터링 데이터.csv')
source = get_dataset(df, sensor_id_dict[sensor_id]['GHID'], sensor_kind_dict[sensor_kind], distribution) 
title = 'data for ' + sensor_id_dict[sensor_id]['title']
plot = make_plot(source, title)

# 동적으로 선택 옵션 적용
# sensor_id_select.on_change('value', update_plot)
# sensor_kind_select.on_change('value', update_plot)
# distribution_select.on_change('value', update_plot)

# # 화면 구성
controls = column(sensor_id_select, sensor_kind_select, distribution_select)

curdoc().add_root(row(plot, controls))
curdoc().title = 'Data'

show(plot)