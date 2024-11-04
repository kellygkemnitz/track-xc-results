import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)
app.title = "Race Times Dashboard"

# Organized data
data = [
    {"Date": "2022-09-10", "Meet": "Emporia Cross Country Invitational (JV)", "Event": "5K", "Class": "10", "Result": "35th", "Time": "24:19.4"},
    {"Date": "2022-09-24", "Meet": "Rim Rock Farm High School Classic (V)", "Event": "5K", "Class": "10", "Result": "133rd", "Time": "23:08.8"},
    {"Date": "2022-10-01", "Meet": "Bishop Carrol Invitational (V)", "Event": "5K", "Class": "10", "Result": "38th", "Time": "22:20.0"},
    {"Date": "2022-10-15", "Meet": "AVCTL League (V)", "Event": "5K", "Class": "10", "Result": "27th", "Time": "21:47.4"},
    {"Date": "2022-10-22", "Meet": "KSHSAA 5A Regionals (V)", "Event": "5K", "Class": "10", "Result": "30th", "Time": "22:15.2"},
    {"Date": "2023-08-31", "Meet": "Great Bend Invitational (V)", "Event": "5K", "Class": "11", "Result": "40th (4th)", "Time": "23:08.7"},
    {"Date": "2023-09-09", "Meet": "Emporia Invitational (V)", "Event": "5K", "Class": "11", "Result": "73rd (4th)", "Time": "23:48.4"},
    {"Date": "2023-09-22", "Meet": "Rim Rock Classic (V)", "Event": "5K", "Class": "11", "Result": "129th (4th)", "Time": "23:36.0"},
    {"Date": "2023-10-13", "Meet": "AVCTL League - Salina (V)", "Event": "5K", "Class": "11", "Result": "25th (5th)", "Time": "22:53.6"},
    {"Date": "2023-10-21", "Meet": "Regionals - Bishop Carrol (V)", "Event": "5K", "Class": "11", "Result": "30th (5th)", "Time": "22:49.0"},
    {"Date": "2023-11-12", "Meet": "NXR Heartland Regional", "Event": "5K", "Class": "11", "Result": "143rd (5th)", "Time": "22:05.1"},
    {"Date": "2024-10-05", "Meet": "The Rush at Brown Thrush Invitational (V)", "Event": "5K", "Class": "12", "Result": "44th (8th", "Time": "22:35.8"},
    {"Date": "2024-10-12", "Meet": "Wild Wind XC Festival (V)", "Event": "5K", "Class": "12", "Result": "52nd", "Time": "22:48.0"},
    {"Date": "2024-10-19", "Meet": "AVCTL League (JV)", "Event": "5K", "Class": "12", "Result": "1st", "Time": "21:08.6"},
    {"Date": "2024-10-26", "Meet": "KSHSAA 6A Regionals - Hutchinson", "Event": "5K", "Class": "12", "Result": "8th (3rd)", "Time": "21:34.9"},
    {"Date": "2024-11-02", "Meet": "KSHSAA 6A State - Rim Rock", "Event": "5K", "Class": "12", "Result": "67th (3rd)", "Time": "21:25.8"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'Time' to seconds for plotting
df['Seconds'] = df['Time'].apply(lambda x: int(x.split(':')[0]) * 60 + float(x.split(':')[1]))

app.layout = html.Div([
    html.H1("Race Times Dashboard", style={'textAlign': 'center'}),
    
    # Data Table
    dash_table.DataTable(
        id='race-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'), style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left', 'fontFamily': 'Arial'},
        style_header={ 'backgroundColor': 'lightgrey', 'fontWeight': 'bold' }
    ),
    
    # Graph
    dcc.Graph(
        id='race-graph',
        figure={
            'data': [
                go.Scatter(
                    x=df['Date'],
                    y=df['Seconds'],
                    mode='lines+markers',
                    name='Race Times',
                    line=dict(color='blue'),
                    marker=dict(size=8, color='red')
                )
            ]
        }
    )
])