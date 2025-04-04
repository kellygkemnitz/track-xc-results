import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

from xc_results import CrossCountry
from track_results import Track

app = dash.Dash(__name__)
app.title = "Race Times Dashboard"

# Initialize classes
xc = CrossCountry()
track = Track()

app.layout = html.Div([
    html.H1("Race Times Dashboard", style={'textAlign': 'center'}),
    
    # Tabs
    dcc.Tabs(id='tabs', value='cross_country', children=[
        dcc.Tab(label='Cross Country Results', value='cross_country'),
        dcc.Tab(label='Track Results', value='track')
    ]),
    
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'), Input('tabs', 'value'))
def render_content(tab):
    if tab == 'cross_country':
        return html.Div([
            dash_table.DataTable(
                id='race-table',
                columns=[{"name": i, "id": i} for i in xc.xc_df.columns],
                data=xc.xc_df.to_dict('records'), 
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', 'fontFamily': 'Arial'},
                style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
            ),
            dcc.Graph(
                id='race-graph',
                figure=xc.create_cross_country_plots()
            )
        ])
    
    elif tab == 'track':
        return html.Div([
            dash_table.DataTable(
                id='race-table',
                columns=[{"name": i, "id": i} for i in track.track_df.columns],
                data=track.track_df.to_dict('records'), 
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', 'fontFamily': 'Arial'},
                style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
            ),
            dcc.Graph(
                id='3200m-graph',
                figure=track.create_track_plots('3200m')
            ),
            dcc.Graph(
                id='1600m-graph',
                figure=track.create_track_plots('1600m')
            ),
            dcc.Graph(
                id='800m-graph',
                figure=track.create_track_plots('800m')
            ),
            dcc.Graph(
                id='4x800m-relay-graph',
                figure=track.create_track_plots('4x800m Relay')
            ),
            dcc.Graph(
                id='4x400m-relay-graph',
                figure=track.create_track_plots('4x400m Relay')
            )
        ])

if __name__ == "__main__":
    app.run(port=8002, debug=True)
