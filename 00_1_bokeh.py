import numpy as np
from bokeh.io import output_notebook, show
from bokeh.plotting import figure

p = figure(plot_width=800, plot_height=400)

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]

# p.circle(x, y, size=10)

p.circle(x, y, size=10, line_color='orange', fill_color='blue', fill_alpha=0.5 )

show(p)
