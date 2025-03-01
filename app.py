from modules.xc_results import CrossCountry
from modules.track_results import Track

import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
app.title = "Race Times Dashboard"

# Initialize classes
cross_country = CrossCountry()
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
                columns=[{"name": i, "id": i} for i in cross_country._cross_country_df.columns],
                data=cross_country._cross_country_df.to_dict('records'), 
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', 'fontFamily': 'Arial'},
                style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
            ),
            dcc.Graph(
                id='race-graph',
                figure=cross_country._create_cross_country_plots()
            )
        ])
    elif tab == 'track':
        return html.Div([
            dash_table.DataTable(
                id='race-table',
                columns=[{"name": i, "id": i} for i in track._track_df.columns],
                data=track._track_df.to_dict('records'), 
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', 'fontFamily': 'Arial'},
                style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
            ),
            dcc.Graph(
                id='race-graph',
                figure=track._create_track_plots()
            )
        ])

if __name__ == "__main__":
    app.run_server(debug=True)
