from bokeh.io import output_file, show, curdoc
from bokeh.layouts import column, row
from bokeh.models import CheckboxGroup

def checkbox_handler(new):
    print('Checkbox button option ' + str(new) + 'selected.')

checkbox_group = CheckboxGroup(labels=['Option 1', 'Option 2', 'Option 3'], active=[0])
checkbox_group.on_click(checkbox_handler)

controls = column(checkbox_group)

curdoc().add_root(row(controls))