
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('.\\cleaned\\cleaned_ev_cat.csv')

Total_EVs = df['Total_EVs'].sum()
avg_per_Month = df['Total_EVs'].mean()
top_Month = df.loc[df['Total_EVs'].idxmax()]

print("📊 KPIs for EV Category (2001–2024)")
print(f"🔋 Total EVs Manufactured: {Total_EVs:,}")
print(f"📆 Average Monthly Production: {int(avg_per_Month):,}")
print(f"🏆 Peak Production Month: {top_Month['Month']}/{int(top_Month['Year'])} with {int(top_Month['Total_EVs']):,} EVs")

plt.figure(figsize=(14, 6))
sns.lineplot(x=pd.to_datetime(df[['Year', 'Month']].assign(day=1)), y='Total_EVs', data=df, marker='o')
plt.title("Monthly EV Production in India (2001–2024)")
plt.xlabel("Date")
plt.ylabel("Total EVs Produced")
plt.grid(True)
plt.tight_layout()

plt.savefig('.\\plots\\ev_cat_Monthly_trend.png', dpi=300)
plt.close()
