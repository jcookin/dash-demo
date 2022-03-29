# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children=[
        html.H1(children="Components"),
    ], className='app-header'),

    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Salt Lake City', 'San Francisco', 'Logan'], 'Salt Lake City', className='dropdowns'),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['New York City', 'Salt Lake City', 'San Francisco', 'Toronto'],
                     ['Toronto', 'San Francisco'],
                     multi=True, className='dropdowns'),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    ],
    style={'padding': 10, 'flex': 1},
    className='components-all'),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                      ['Montréal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Text Input '),
        dcc.Input(value='I totally typed this', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),
    ],
    style={'padding': 10, 'flex': 1},
    className='components-all'),

    html.Div(children=[
        html.H1(children='Callback Example'),
        html.Div(dcc.Input(placeholder='Enter your name', id='input-on-submit', type='text', style={'width': 120, 'height': 40})),
        html.Button('Submit', id='submit-text-box', n_clicks=0),
        html.Div(id='button-out', children='Names:'),
    ],
    className='components-all',
    )

], style={'display': 'flex', 'flex-direction': 'row'})


names={}
def check_names(name):
    # print(names)
    if name is None:
        return 0
    if not name in names.keys():
        names[name] = 0
    names[name] += 1
    return names[name]

# Get the text box's current value and add it to the div below the button
@app.callback(
    Output('button-out', 'children'),
    Input(component_id='submit-text-box', component_property='n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value=""):
    name_clicks = check_names(value)

    return 'Hello {}, the button has been clicked {} times, {} times by you'.format(
        value,
        n_clicks,
        name_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)