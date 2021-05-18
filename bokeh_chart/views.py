from bokeh_chart.settings import DATABASES
from django.shortcuts import render
from .app import get_ticker, plot_stock

def base(request):
    
    script, div = components(p_stock)
    

    

    return render(request, '/', {'script':script, 'div':div})