# import bokeh
# bokeh.sampledata.download()

import pandas as pd
from bokeh.plotting import figure
from bokeh.sampledata.stocks import AAPL
from bokeh.io import show

df = pd.DataFrame(AAPL)
# print(df.head())
# print(df.shape)

# 문자열을 시간데이터로 변경해줌
df.index = pd.to_datetime(df['date'])
df = df.drop('date', axis=1)
print(df.head())

p = figure(plot_width=700, plot_height=300, x_axis_type='datetime')
p.line(df.index, df['close'], color='navy', alpha=0.5)
# show(p)

import jinja2
from bokeh.embed import components
template = jinja2.Template('''
<html>
<link href='http://cdn.pydata.org/bokeh/release/bokeh-2.0.2.min.css' rel='stylesheet' type='text/css'>
<script src='http://cdn.pydata.org/bokeh/release/bokeh-2.0.2.min.js'></script>
<head><title>bokeh test</title></head>
<body>

<h1>This site for Bokeh Test</h1>
{{script}}
{{div}}

</body>
</html>
'''
)

script, div = components(p)

# 확인을 위한
# from IPython.display import HTML
# HTML(template.render(script=script, div=div))

# 파일 작성 및 열기
with open('a.html', 'w') as f:
    f.write(template.render(script=script, div=div))

import webbrowser
webbrowser.open('a.html')
