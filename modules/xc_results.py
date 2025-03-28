import plotly.graph_objects as go
import pandas as pd

class CrossCountry:
    def __init__(self):
        self.xc_data = 'data/xc-results.json'
        self.xc_df = self._convert_to_df(self.xc_data)
        self.xc_results = self._times_to_seconds(self.xc_df)

    def _convert_to_df(self, xc_data):
        try:
            df = pd.read_json(xc_data)
            return df
        except FileNotFoundError as e:
            print (f'Error {e}')
            return None
        except Exception as e:
            print(f'An unexpected error occurred: {e}')
            return None
        
    def _times_to_seconds(self, xc_df):
        xc_df['Seconds'] = xc_df['Time'].apply(lambda x: int(x.split(':')[0]) * 60 + float(x.split(':')[1])).copy()
        return xc_df

    def create_cross_country_plots(self):
        xc_fig = go.Figure()
        xc_results = self.xc_results.sort_values('Date')

        for grade in xc_results['Grade'].unique():
            grade_results = xc_results[xc_results['Grade'] == grade]

            hover_text = grade_results.apply(lambda row:
                f"Time: {row['Time']}<br>" +
                f"Date: {row['Date'].strftime('%Y-%m-%d')}<br>" +
                f"Meet: {row['Meet']}<br>" +
                f"Grade: {row['Grade']}", axis=1)

            xc_fig.add_trace(go.Scatter(
                x=grade_results['Date'],
                y=grade_results['Seconds'],
                mode='lines+markers',
                name=f'Grade {grade}',
                line=dict(),
                marker=dict(size=8),
                text=hover_text,
                hoverinfo='text'
            ))

            xc_fig.update_layout(
                title='Cross Country Results',
                xaxis_title='Meet',
                yaxis_title='Time (seconds)',
                xaxis=dict(
                    type='category',
                    tickmode='array',
                    tickvals=xc_results['Date'],
                    ticktext=xc_results['Meet'],
                    tickangle=45,
                ),
                hovermode='closest'
            )

        return xc_fig