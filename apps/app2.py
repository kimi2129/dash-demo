from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px

from app import app

# from apps.input_state import input, state
layout = html.Div([
    #dcc.Link('Go to Plotly', href='/apps/app1'),
    #html.H3('Dash'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': 'Input', 'value': 'input'},
            {'label': 'State', 'value': 'state'},
        ]
    ),
    html.Br(),
    html.Div(id='app-2-display-value'),
])


@app.callback(
    Output('app-2-display-value', 'children'),
    Input('app-2-dropdown', 'value'))
def display_value(value):
    if value == 'input':
        return html.Div([
                dcc.Dropdown(
                    id='type-input-ddpn',
                    options=[
                        {'label': 'Line Chart', 'value': 'line'},
                        {'label': 'Bar Chart', 'value': 'bar'},
                    ]
                ),
                html.Br(),
                html.Div(id='input-div-display'),
            ])
    if value == 'state':
        return html.Div([
            dcc.Dropdown(
                id='type-state-ddpn',
                options=[
                    {'label': 'Line Chart', 'value': 'line'},
                    {'label': 'Bar Chart', 'value': 'bar'},
                ],
            ),
            html.Br(),
            html.Button('Submit', id='btn-submit'),
            html.Br(),
            html.Div(id='state-div-display'),
        ])

@app.callback(
    Output('input-div-display', 'children'),
    Input('type-input-ddpn', 'value'))
def display_value(value):
    if value == 'line':
        df = px.data.gapminder().query("country=='Canada'")
        fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
        return dcc.Graph (figure= fig)
    if value == 'bar':
        df = px.data.gapminder().query("country=='Canada'")
        fig = px.bar(df, x="year", y="lifeExp", title='Life expectancy in Canada')
        return dcc.Graph (figure= fig)

@app.callback(
    Output('state-div-display', 'children'),
    Input('btn-submit', 'n_clicks'),
    State('type-state-ddpn', 'value'))
def display_value(n_clicks, value):
    if n_clicks:
        if value == 'line':
            df = px.data.gapminder().query("country=='Canada'")
            fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
            return dcc.Graph (figure= fig)
        if value == 'bar':
            df = px.data.gapminder().query("country=='Canada'")
            fig = px.bar(df, x="year", y="lifeExp", title='Life expectancy in Canada')
            return dcc.Graph (figure= fig)