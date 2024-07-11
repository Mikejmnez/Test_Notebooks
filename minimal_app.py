from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import Div

div = Div(text="Hello, Bokeh!", width=200, height=100)
curdoc().add_root(column(div))

