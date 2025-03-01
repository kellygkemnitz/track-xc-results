import plotly.graph_objects as go
import pandas as pd

class CrossCountry:
    def __init__(self):
        self._cross_country_data = 'data/xc-results.json'
        self._cross_country_df = self._convert_to_df(self._cross_country_data)
        self._race_times = self._times_to_seconds(self._cross_country_df)
        self._create_cross_country_plots = self._create_cross_country_plots(self._race_times)

    def _convert_to_df(self, file_path):
        try:
            df = pd.read_json(self._cross_country_data)
            return df
        except FileNotFoundError as e:
            print (f'Error {e}')
            return None
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None
        
    def _times_to_seconds(self, cross_country_df):
        cross_country_df['Seconds'] = cross_country_df['Time'].apply(lambda x: int(x.split(':')[0]) * 60 + float(x.split(':')[1]))
        return cross_country_df

    def _create_cross_country_plots(self, cross_country_results):
        fig = go.Figure()

        cross_country_results = cross_country_results.sort_values('Date')

        hover_text = cross_country_results.apply(lambda row:
            f"Date: {row['Date']}<br>" +
            f"Grade: {row['Grade']}<br>" +
            f"Race: {row['Meet']}<br>" +
            f"Time: {row['Time']}", axis=1)

        fig.add_trace(go.Scatter(
            x=cross_country_results['Date'],
            y=cross_country_results['Seconds'],
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
                tickvals=cross_country_results['Date'],
                ticktext=cross_country_results['Date'],
                tickangle=45,
            ),
            hovermode='closest'
        )
        
        return fig