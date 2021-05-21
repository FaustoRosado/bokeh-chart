import yfinance as yf
import pandas as pd
import requests
from bokeh.embed import components
from bokeh.plotting import figure, ColumnDataSource, show
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models.formatters import NumeralTickFormatter

def get_ticker(ticker=None):
    df = yf.Ticker(ticker)
    df = df.history(period='60d')
    df.reset_index(inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    return df

def plot_stock(stock):
    
    p = figure(plot_width=1200, plot_height=900, x_axis_label="DATES", y_axis_label="STOCK PRICE",
        title="DOGE PRICE IN THE LAST 60 DAYS", toolbar_location='above')

    p.xaxis.major_label_overrides = {
        i+int(stock.data['index'][0]): date.strftime('%b %d') for i, date in 
        enumerate(pd.to_datetime(stock.data["Date"]))
        }
        
    p.xaxis.bounds = (stock.data['index'][0], stock.data['index'][-1])
    
    p.vbar(x='index', width=.70, top='High', bottom='Low', fill_color='BLUE', line_color='RED',
        source=stock,name="price")
    
    p.xaxis.major_label_orientation = 1
    
    p.xaxis.ticker.desired_num_ticks = 60
    
    p.yaxis.formatter = NumeralTickFormatter(format='$ 0,0[.]000')
    
    #print(p.xaxis.major_label_overrides)

    return p


# stock = ColumnDataSource(
#     data=dict(Date=[], Open=[], Close=[], High=[], Low=[],index=[]))

# ticker = "DOGE-USD"

# df = get_ticker(ticker)

# stock.data = stock.from_df(df)



#     # update_plot()
# p_stock = plot_stock(stock)




# curdoc().theme = 'dark_minimal'
# show(p_stock)