import plotly.graph_objects as go
import pandas as pd

class Track:
    def __init__(self):
        self.track_data = 'data/track-results.json'
        self.track_df = self._convert_to_df(self.track_data)
        self.track_results = self._times_to_seconds(self.track_df)

    def _convert_to_df(self, track_data):
        try:
            df = pd.read_json(track_data)
            return df
        except FileNotFoundError as e:
            print (f'Error {e}')
            return None
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None
        
    def _times_to_seconds(self, track_df):
        track_df['Seconds'] = track_df['Individual Time'].apply(lambda x: int(x.split(':')[0]) * 60 + float(x.split(':')[1]) if pd.notna(x) else x).copy()
        return track_df

    def create_track_plots(self, event_name):
        track_fig = go.Figure()

        # Filter data by the specific event
        track_results = self.track_results[self.track_results['Event'] == event_name].sort_values('Date')

        if track_results.empty:
            print(f"No data available for event: {event_name}")
            return None

        # Loop through each unique grade within the event
        for grade in track_results['Grade'].unique():
            grade_results = track_results[track_results['Grade'] == grade]

            # Create hover text for this grade
            hover_text = grade_results.apply(lambda row:
                f"Time: {row['Individual Time']}<br>" +
                f"Date: {row['Date'].strftime('%Y-%m-%d')}<br>" +
                f"Meet: {row['Meet']}<br>" +
                f"Grade: {row['Grade']}", axis=1
            )

            # Add a trace for each grade
            track_fig.add_trace(go.Scatter(
                x=grade_results['Date'],
                y=grade_results['Seconds'],
                mode='lines+markers',
                name=f'Grade {grade}',
                line=dict(),
                marker=dict(size=8),
                text=hover_text,
                hoverinfo='text'
            ))

        # Update layout for the graph
        track_fig.update_layout(
            title=f'{event_name} Results',
            xaxis_title='Meet',
            yaxis_title='Time (seconds)',
            xaxis=dict(
                type='category',
                tickmode='array',
                tickvals=track_results['Date'],
                ticktext=track_results['Meet'],
                tickangle=45
            ),
            hovermode='closest'
        )

        return track_fig