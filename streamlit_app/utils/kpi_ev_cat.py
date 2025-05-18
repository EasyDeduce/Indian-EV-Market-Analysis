import pandas as pd
import plotly.express as px

def preprocess_date(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month_name()
    return df

def compute_kpis(df):
    if df.empty:
        return { "No data available": "—" }

    total_ev = df['Total_EVs'].sum()
    yearly_total = df.groupby('Year')['Total_EVs'].sum()
    avg_per_month = df['Total_EVs'].mean()
    peak_month = df.loc[df['Total_EVs'].idxmax(), 'Date']
    lowest_month = df.loc[df['Total_EVs'].idxmin(), 'Date']
    latest = df[df['Date'] == df['Date'].max()]['Total_EVs'].values[0]

    return {
        "Total EV Registrations": int(total_ev),
        "Avg EVs/Month": round(avg_per_month),
        "Peak Month": peak_month.strftime("%b %Y"),
        "Lowest Month": lowest_month.strftime("%b %Y"),
        "Latest Month Sales": int(latest),
        "Total Years Covered": df['Year'].nunique(),
        "Months Covered": df['Date'].dt.to_period('M').nunique(),
        "Max Year": df['Year'].max()
    }

def plot_sales_trend(df):
    fig = px.line(df, x="Date", y="Total_EVs", title="EV Sales Over Time")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="EV Registrations",
        title_font=dict(size=20),
        template="plotly_white"
    )
    return fig

def plot_ev_by_type(df):
    if df.empty:
        return px.bar(title="No data to display")

    latest_df = df[df['Date'] == df['Date'].max()]
    ev_types = latest_df.drop(columns=['Date', 'Year', 'Month', 'Total_EVs'])
    ev_type_sum = ev_types.T.reset_index()
    ev_type_sum.columns = ['EV Type', 'Units']

    fig = px.bar(ev_type_sum.sort_values('Units', ascending=False),
                 x='EV Type', y='Units',
                 title="EV Breakdown by Type (Latest Month)",
                 text_auto=True,
                 template="plotly_white")
    fig.update_traces(marker_color='indigo')
    return fig
