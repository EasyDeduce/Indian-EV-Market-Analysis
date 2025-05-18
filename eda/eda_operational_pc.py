import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('.\\data\\OperationalPC.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("✅ Cleaned columns:", df.columns.tolist())  # Should be: ['state', 'no._of_operational_pcs']

df.rename(columns={'no._of_operational_pcs': 'charging_stations'}, inplace=True)


df.dropna(subset=['state', 'charging_stations'], inplace=True)

df['charging_stations'] = pd.to_numeric(df['charging_stations'], errors='coerce')
df.dropna(subset=['charging_stations'], inplace=True)

total_stations = df['charging_stations'].sum()
avg_stations = df['charging_stations'].mean()
max_state = df.loc[df['charging_stations'].idxmax()]

print("\n📈 KPIs:")
print(f"🔌 Total Public Charging Stations in India: {int(total_stations)}")
print(f"📍 Average Stations per State: {avg_stations:.2f}")
print(f"🏆 State with Max Stations: {max_state['state']} ({int(max_state['charging_stations'])})")

top_10_states = df.sort_values(by='charging_stations', ascending=False).head(10)
print("\n🔝 Top 10 States by Public Charging Stations:")
print(top_10_states[['state', 'charging_stations']])

plt.figure(figsize=(12, 6))
sns.barplot(
    x='charging_stations',
    y='state',
    data=top_10_states,
    palette='magma'
)
plt.title("Top 10 States by Operational Public Charging Stations")
plt.xlabel("Total Stations")
plt.ylabel("State")
plt.tight_layout()
plt.savefig('.\\plots\\operational_pc_top10.png', dpi=300)
plt.close()
df.to_csv('.\\cleaned\\cleaned_operational_pc.csv', index=False)
