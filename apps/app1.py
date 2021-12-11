from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps.chart_types.basic import *
from apps.chart_types.statistical import *
from apps.chart_types.scientific import *
from apps.chart_types.financial import *
from apps.chart_types.maps import *
from apps.chart_types.threeD import *

layout = html.Div([
    dcc.Link('Go to Dash', href='/apps/app2'),
    html.H3('Plotly'),
    dcc.Dropdown(
        id='app-1-dropdown',
        options=[
            {'label': 'Basic Charts', 'value': 'basic'},
            {'label': 'Statistical Charts', 'value': 'statistical'},
            {'label': 'Scientific Charts', 'value': 'scientific'},
            {'label': 'Financial Charts', 'value': 'financial'},
            {'label': 'Maps', 'value': 'maps'},
            {'label': '3D Charts', 'value': 'threeD'},
        ]
    ),
    html.Div(id='app-1-display-value'),
])


@app.callback(
    Output('app-1-display-value', 'children'),
    Input('app-1-dropdown', 'value'))
def display_value(value):
    if value == 'basic':
        return html.Div([line(),
                        bar(),
                        scatter()])
    if value == 'statistical':
        return html.Div([histogram(),
                        boxplot()])
    if value == 'scientific':
        return html.Div([heatmap(),
                        radar()])
    if value == 'financial':
        return html.Div([time_series(),
                        candlestick()])
    if value == 'maps':
        return html.Div([Choropleth_Maps()])
    if value == 'threeD':
        return html.Div([Surface_Plots()])