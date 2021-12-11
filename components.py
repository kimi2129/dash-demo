from dash import dcc
from dash import html
from datetime import datetime as dt

def dcc_components():
    return html.Div([
        dcc.Dropdown(
            options=[
                {'label': 'Line Chart', 'value': 'line'},
                {'label': 'Bar Chart', 'value': 'bar'},
                ],
                # multi=True,
                id='chart_type_dpdn',
                value='line'
        ),

        dcc.Slider(
            min=-5,
            max=10,
            step=0.5,
            value=-3,
            # min=0,
            # max=9,
            # marks={i: 'Label {}'.format(i) for i in range(10)},
            # value=5,
        ),

        # RangeSlider
        dcc.RangeSlider(
            count=1,
            min=-5,
            max=10,
            step=0.5,
            value=[-3, 7]
            # marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
            # min=-5,
            # max=6,
            # value=[-3, 4]
        ),
        
        # Input
        dcc.Input(
            placeholder='Enter a value...',
            type='text',
            value=''
        ),

        # Textarea
        dcc.Textarea(
            placeholder='Enter a value...',
            value='This is a TextArea component',
            style={'width': '100%'}
        ),

        # DatePickerSingle
        dcc.DatePickerSingle(
            id='date-picker-single',
            date=dt(1997, 5, 10)
        ), 

        # DatePickerRange
        dcc.DatePickerRange(
            id='date-picker-range',
            start_date=dt(1997, 5, 3),
            end_date_placeholder_text='Select a date!'
        ),


        # Checklists
        # dcc.Checklist(
        #     options=[
        #     {'label': 'New York City', 'value': 'NYC'},
        #     {'label': 'Montréal', 'value': 'MTL'},
        #     {'label': 'San Francisco', 'value': 'SF'}
        #     ],
        #     values=['MTL', 'SF']
        # )

        # Markdown
        dcc.Markdown('''
        #### Dash and Markdown
        
        Dash supports [Markdown](http://commonmark.org/help).
        
        Markdown is a simple way to write and format text.
        It includes a syntax for things like **bold text** and *italics*,
        [links](http://commonmark.org/help), inline `code` snippets, lists,
        quotes, and more.
        '''),

        # Radio Items
        dcc.RadioItems(
            options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='MTL'
        ),

        # Button
        html.Button('Submit', id='button'),
    ], style={'width':'50%'})