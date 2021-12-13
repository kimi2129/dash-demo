from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go

def time_series():
    df_stock = px.data.stocks()
    fig = px.line(df_stock, x='date', y="GOOG")
    return dcc.Graph(figure=fig)
def candlestick():
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['AAPL.Open'],
                    high=df['AAPL.High'],
                    low=df['AAPL.Low'],
                    close=df['AAPL.Close'])])
    return dcc.Graph(figure=fig)
