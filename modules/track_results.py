import plotly.graph_objects as go
import pandas as pd

class Track:
    def __init__(self):
        self._track_data = 'data/track-results.json'
        self._track_df = self._convert_to_df(self._track_data)
        self._race_times = self._times_to_seconds(self._track_df)
        self._create_track_plots = self._create_track_plots(self._race_times)

    def _convert_to_df(self, file_path):
        try:
            df = pd.read_json(self._track_data)
            return df
        except FileNotFoundError as e:
            print (f'Error {e}')
            return None
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None
        
    def _times_to_seconds(self, track_df):
        track_df['Seconds'] = track_df['Individual Time'].apply(lambda x: int(x.split(':')[0]) * 60 + float(x.split(':')[1]) if pd.notna(x) else x)
        return track_df

    def _create_track_plots(self, track_results):
        fig = go.Figure()

        track_results = track_results.sort_values('Date')

        hover_text = track_results.apply(lambda row:
            f"Date: {row['Date']}<br>" +
            f"Grade: {row['Grade']}<br>" +
            f"Race: {row['Meet']}<br>" +
            f"Time: {row['Individual Time']}", axis=1)

        fig.add_trace(go.Scatter(
            x=track_results['Date'],
            y=track_results['Seconds'],
            mode='lines+markers',
            name='Race Times',
            line=dict(color='blue'),
            marker=dict(size=8, color='blue'),
            text=hover_text,
            hoverinfo='text'
        ))
        
        fig.update_layout(
            title='Race History',
            xaxis_title='Date',
            yaxis_title='Time (seconds)',
            xaxis=dict(
                type='category',
                tickmode='array',
                tickvals=track_results['Date'],
                ticktext=track_results['Date'],
                tickangle=45,
            ),
            hovermode='closest'
        )
        
        return fig