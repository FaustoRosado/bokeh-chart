from django.shortcuts import render
from bokeh.embed import components
from .app import get_symbol, plot_stock

def index(request):
    
    

    script, div = components(p_stock)

    return render('base.html', {'script':script, 'div':div})