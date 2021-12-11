import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

def line():
    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="gdpPercap", color='country')
    return dcc.Graph(figure=fig)
def bar():
    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.bar(df, x='year', y='pop',color='country',barmode='group',category_orders={"country": ["New Zealand", "Australia"]})
    return dcc.Graph(figure=fig)
def scatter():
    df = px.data.iris() # iris is a pandas DataFrame
    fig = px.scatter(df, x="sepal_width", y="sepal_length")
    return dcc.Graph(figure=fig)