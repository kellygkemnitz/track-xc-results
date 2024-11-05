from race_results import CrossCountry

import dash
from dash import dash_table
from dash import dcc
from dash import html


app = dash.Dash(__name__)
app.title = "Race Times Dashboard"

# Initialize the CrossCountry class
cross_country = CrossCountry()

app.layout = html.Div([
    html.H1("Race Times Dashboard", style={'textAlign': 'center'}),
    
    # Data Table
    dash_table.DataTable(
        id='race-table',
        columns=[{"name": i, "id": i} for i in cross_country._cross_country_df.columns],
        data=cross_country._cross_country_df.to_dict('records'), 
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'fontFamily': 'Arial'},
        style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold'}
    ),
    
    # Graph
    dcc.Graph(
        id='race-graph',
        figure=cross_country._create_cross_country_plots
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)