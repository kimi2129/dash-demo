from dash import dcc
from dash import html
import plotly.express as px

def histogram():
    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y='tip',histfunc='avg')
    return dcc.Graph(figure=fig)
def boxplot():
    df = px.data.tips()
    fig = px.box(df, y="total_bill")
    return dcc.Graph(figure=fig)