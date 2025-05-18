import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def compute_kpis(df):
    total_makers = df['ev_maker'].nunique()
    total_locations = len(df)
    top_states = df['state'].value_counts().head(5)
    top_places = df['place'].value_counts().head(5)
    state_max_makers = df.groupby('state')['ev_maker'].nunique().idxmax()
    avg_plants_per_state = round(df.groupby('state').size().mean(), 2)
    top_maker = df['ev_maker'].value_counts().idxmax()
    states_with_5plus = (df['state'].value_counts() >= 5).sum()

    return {
        "Total Manufacturers": total_makers,
        "Total Locations": total_locations,
        "State with Max Manufacturers": state_max_makers,
        "Avg Plants per State": avg_plants_per_state,
        "Top Manufacturer": top_maker,
        "States with ≥5 Plants": states_with_5plus,
        "Top States": top_states,
        "Top Places": top_places
    }

def plot_state_distribution(df):
    state_counts = df['state'].value_counts()
    top_8 = state_counts.head(8)
    others = state_counts[8:].sum()
    pie_data = pd.concat([top_8, pd.Series({'Others': others})])

    fig, ax = plt.subplots(figsize=(6, 6))
    pie_data.plot.pie(autopct='%1.1f%%', ax=ax, startangle=90)
    ax.set_ylabel('')
    ax.set_title("State-wise Distribution of Manufacturing Plants")
    return fig

def get_places_by_state(df, selected_state):
    return df[df['state'] == selected_state]['place'].value_counts().head(10)
