from django.shortcuts import render

import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from datetime import datetime


# Create your views here.
def homePage(request):

    df = pd.read_csv('stock(data).csv')
    df.columns = df.columns.str.strip()

    fig = go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'])])
    fig.update_layout(
        title='Stocks Chart',
        xaxis_title='Date',
        yaxis_title='Price',
        plot_bgcolor='rgb(20, 6, 54)',  # Transparent background
        paper_bgcolor='rgb(20, 6, 54)',     # Background color outside the plot
        font=dict(family='Arial', size=12, color='white'),
        xaxis=dict(
            showgrid=True,             # Show x-axis grid lines
            gridcolor='rgb(20, 6, 54)'      # Set grid line color
        ),
        yaxis=dict(
            showgrid=True,             # Show y-axis grid lines
            gridcolor='rgb(20, 6, 54)'      # Set grid line color
        ),
        margin=dict(l=40, r=40, t=60, b=40)  # Set margins
    )
    
    

    graph_json = pio.to_json(fig)
    
    return render(request, 'index.html', {'GraphJSON' : graph_json})