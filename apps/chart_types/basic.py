from dash import dcc
from dash import html
import plotly.express as px

def line():
    df_oceania = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df_oceania, x="year", y="gdpPercap", color='country')
    return dcc.Graph(figure=fig)
def bar():
    df_canada = px.data.gapminder().query("country == 'Canada'")
    fig = px.bar(df_canada, x='year', y='pop')
    return dcc.Graph(figure=fig)
def scatter():
    df_iris = px.data.iris() # iris is a pandas DataFrame
    fig = px.scatter(df_iris, x="sepal_width", y="sepal_length")
    return dcc.Graph(figure=fig)
def pie():
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day')
    return dcc.Graph(figure=fig)