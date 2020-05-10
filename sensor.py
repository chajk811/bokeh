import datetime
import copy

import pandas as pd

from bokeh.io import curdoc, show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import Blues4
from bokeh.plotting import figure


def get_dataset(src, sensor_id_num, sensor_kind_name, axis_kind_name):
    # sensor_kind_name 은 X, Y dict or X, Y, Z dict 형태로 들어온다.
    STATISTICS = sensor_kind_dict[sensor_kind_name][axis_kind_name]
    df = src[src.GHID == sensor_id_num].copy()[STATISTICS + ['MTime']]
    df['MTime'] = pd.to_datetime(df.MTime)
    df = df.set_index(['MTime'])

    return ColumnDataSource(data=df.iloc[0:9000,:])
    ## 오류 => 그래서 ColumnDataSorce 에 들어가는 df의 row 개수를 9000개로 조정
    # ColumnDataSource's columns must be of the same length. Current lengths:
    # ('MTime', 9926), ('MXAcelAvg', 9926), ('MXAcelMax', 9926), ('MXAcelMin', 9926),
    # ('MXSineAvg', 9931), ('MXSineMax', 9931), ('MXSineMin', 9931),
    # ('MYAcelAvg', 9951), ('MYAcelMax', 9951), ('MYAcelMin', 9951),
    # ('MYSineAvg', 9931), ('MYSineMax', 9931), ('MYSineMin', 9931),
    # ('MZAcelAvg', 9931), ('MZAcelMax', 9931), ('MZAcelMin', 9931)



def make_plot(source, title):
    plot = figure(plot_width=800, x_axis_type='datetime')
    plot.title.text = title

    ## !!!!!!!!!!!!!!!!!!!!!!!!
    ## 이부분 수정만 하면됨
    ## ColumnDataSource를 왜 사용하는지
    ## 참고 : https://stackoverrun.com/ko/q/10124318
    # print(list(source.data.keys()))

    y_keys = list(source.data.keys())
    plot.line('MTime', y_keys[1], source=source, color='red')
    plot.line('MTime', y_keys[2], source=source, color='blue')
    plot.line('MTime', y_keys[3], source=source, color='green')

    ## ColumnDataSource로 변환하여 받아온 DataFrame을 사용해서 선 그리기
    # plot.line(source.index, source.iloc[:, 0], source=source, color='red')
    # plot.line(source.index, source.iloc[:, 1], source=source, color='blue')
    # plot.line(source.index, source.iloc[:, 2], source=source, color='green')

    return plot


def update_plot(attrname, old, new):
    sensor_id = sensor_id_select.value
    sensor_kind = sensor_kind_select.value
    axis_kind = axis_kind_select.value

    plot.title.text = '{}_{}'.format(sensor_kind, axis_kind) + ' data for ' + sensor_id_dict[sensor_id]['title']

    if sensor_kind_select.value == 'Acel':
        axis_kind_select.options = ['X', 'Y', 'Z']
    else:
        axis_kind_select.options = ['X', 'Y']

    src = get_dataset(df, sensor_id_dict[sensor_id]['GHID'], sensor_kind, axis_kind) 
    source.data.update(src.data)


# 기본값 설정
sensor_id = 'ID201'
sensor_kind = 'Tilt'
axis_kind = 'X'

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
        'title': 'ID204 sensor',
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
axis_kind_select = Select(value=axis_kind, title='axis_kind', options=['X', 'Y'])

# 그래프 그리는 부분
df = pd.read_csv('2020-04-02 모니터링 데이터.csv')
source = get_dataset(df, sensor_id_dict[sensor_id]['GHID'], sensor_kind, axis_kind) 
title = '{}_{}'.format(sensor_kind, axis_kind) + ' data for ' + sensor_id_dict[sensor_id]['title']
plot = make_plot(source, title)

# 동적으로 선택 옵션 적용
sensor_id_select.on_change('value', update_plot)
sensor_kind_select.on_change('value', update_plot)
axis_kind_select.on_change('value', update_plot)

# # 화면 구성
controls = column(sensor_id_select, sensor_kind_select, axis_kind_select)

curdoc().add_root(row(plot, controls))
curdoc().title = 'Data'