import pandas as pd
import requests
from bokeh_chart.settings import DATABASES
from django.shortcuts import render
from bokeh.embed import components
from bokeh.plotting import figure, ColumnDataSource, show
from bokeh.io import curdoc
from bokeh.layouts import column

from .app import get_ticker, plot_stock



def base(request):
    
   
    stock = ColumnDataSource(
    data=dict(Date=[], Open=[], Close=[], High=[], Low=[],index=[]))

    ticker = "DOGE-USD"

    df = get_ticker(ticker)

    stock.data = stock.from_df(df)



    # update_plot()
    p_stock = plot_stock(stock)
    
    curdoc().theme = 'dark_minimal'
    show(p_stock)

    script, div = components(p_stock)

    return render(request, '/', {'script':script, 'div':div})