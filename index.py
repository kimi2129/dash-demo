from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Tabs(id="tabs", value='plotly', children=[
            dcc.Tab(label='Plotly', value='plotly'),
            dcc.Tab(label='Dash', value='dash'),
        ]),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('tabs', 'value'))
def display_page(tab):
    if tab == 'plotly':
        return app1.layout
    if tab == 'dash':
        return app2.layout

if __name__ == '__main__':
    app.run_server(debug=True)