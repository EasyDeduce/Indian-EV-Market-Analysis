import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("./plots", exist_ok=True)

df = pd.read_csv("./cleaned/cleaned_ev_maker_place.csv")

sns.set_theme(style="whitegrid")

top_states = df['state'].value_counts().head(10).reset_index()
top_states.columns = ['state', 'num_plants']

plt.figure(figsize=(12, 7))
sns.barplot(data=top_states, y='state', x='num_plants', palette='mako')
plt.title('Top 10 Indian States by Number of EV Manufacturing Plants', fontsize=16)
plt.xlabel('Number of Plants', fontsize=14)
plt.ylabel('State', fontsize=14)
plt.tight_layout()
plt.savefig("./plots/top_10_states_ev_plants.png")
plt.close()
top_places = df['place'].value_counts().head(10).reset_index()
top_places.columns = ['place', 'num_plants']

plt.figure(figsize=(12, 7))
sns.barplot(data=top_places, y='place', x='num_plants', palette='rocket')
plt.title('Top 10 Cities by Number of EV Manufacturing Plants', fontsize=16)
plt.xlabel('Number of Plants', fontsize=14)
plt.ylabel('City/Place', fontsize=14)
plt.tight_layout()
plt.savefig("./plots/top_10_places_ev_plants.png")
plt.close()
state_counts = df['state'].value_counts()
top_8_states = state_counts.head(8)
others = state_counts.iloc[8:].sum()

pie_data = pd.concat([top_8_states, pd.Series({'Others': others})])

plt.figure(figsize=(10, 10))
pie_data.plot.pie(autopct='%1.1f%%', startangle=140, cmap='tab20', legend=False)
plt.title('Distribution of EV Manufacturing Plants by State (Top 8 + Others)', fontsize=16)
plt.ylabel('')
plt.tight_layout()
plt.savefig("./plots/pie_distribution_states_ev_plants.png")
plt.close()

