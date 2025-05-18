import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compute_kpis(df: pd.DataFrame) -> dict:
    """Compute 8-10 KPIs for OperationalPC dataset."""
    kpis = {}
    kpis['Total Charging Stations'] = df['charging_stations'].sum()
    kpis['Total States'] = df['state'].nunique()
    kpis['Max Stations in a State'] = df['charging_stations'].max()
    kpis['Min Stations in a State'] = df['charging_stations'].min()
    kpis['Average Stations per State'] = round(df['charging_stations'].mean(), 2)
    kpis['States with >100 Stations'] = (df['charging_stations'] > 100).sum()
    kpis['States with <10 Stations'] = (df['charging_stations'] < 10).sum()
    kpis['Median Stations per State'] = df['charging_stations'].median()
    return kpis


def plot_statewise_distribution(df: pd.DataFrame) -> plt.Figure:
    """Plot horizontal bar chart of charging stations by state."""
    plt.figure(figsize=(12, 8))
    df_sorted = df.sort_values(by='charging_stations', ascending=True)
    sns.barplot(x='charging_stations', y='state', data=df_sorted, palette='viridis')
    plt.title('Charging Stations by State')
    plt.xlabel('Number of Charging Stations')
    plt.ylabel('State')
    plt.tight_layout()
    fig = plt.gcf()
    return fig
