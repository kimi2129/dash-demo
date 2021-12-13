import plotly.graph_objects as go
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px

def Surface_Plots():
    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

    fig = go.Figure(data=[go.Surface(z=z_data.values)])

    fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    width=500, height=500,
                    margin=dict(l=65, r=50, b=65, t=90))
    return dcc.Graph(figure=fig)

def threed_scatter():
    df = px.data.iris()
    fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
                        color='species')
    return dcc.Graph(figure=fig)