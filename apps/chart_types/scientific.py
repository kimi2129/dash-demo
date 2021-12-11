import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

def heatmap():
    fig = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1]])
    return dcc.Graph(figure=fig)
def radar():
    categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=categories,
        fill='toself',
        name='Product A'
    ))
    fig.add_trace(go.Scatterpolar(
        r=[4, 3, 2.5, 1, 2],
        theta=categories,
        fill='toself',
        name='Product B'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=False
    )
    return dcc.Graph(figure=fig)