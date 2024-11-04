import plotly.graph_objs as go
import pandas as pd

# Data
data = {
    "Date": ["2022-09-10", "2022-09-24", "2022-10-01", "2022-10-15", "2022-10-22"],
    "Meet": ["Emporia Cross Country Invitational (JV)", "Rim Rock Farm High School Classic (V)", "Bishop Carrol Invitational (V)", "AVCTL League (V)", "KSHSAA 5A Regionals (V)"],
    "Time": ["24:19.4", "23:08.8", "22:20.0", "21:47.4", "22:15.2"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'Time' to seconds for plotting
df['Seconds'] = df['Time'].apply(lambda x: int(x.split(':')[0]) * 60 + float(x.split(':')[1]))

# Create Plotly figure
fig = go.Figure()

# Add trace
fig.add_trace(go.Scatter(
    x=df['Date'],
    y=df['Seconds'],
    mode='lines+markers',
    name='Race Times',
    line=dict(color='blue'),
    marker=dict(size=8, color='red')
))

# Update layout
fig.update_layout(
    title='Race Times Over Events',
    xaxis_title='Date',
    yaxis_title='Time (seconds)',
    xaxis=dict(
        tickmode='linear'
    ),
    yaxis=dict(
        tickformat='%M:%S'
    ),
    plot_bgcolor='#f0f0f0',
    paper_bgcolor='#f0f0f0'
)

# Show plot
fig.show()
