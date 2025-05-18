import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('.\\data\\Vehicle Class - All.csv')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print("✅ Cleaned columns:", df.columns.tolist())  

df['total_registration'] = df['total_registration'].str.replace(',', '')
df['total_registration'] = pd.to_numeric(df['total_registration'], errors='coerce')

df.dropna(subset=['vehicle_class', 'total_registration'], inplace=True)

df.sort_values(by='total_registration', ascending=False, inplace=True)

total_all = df['total_registration'].sum()
avg_all = df['total_registration'].mean()
top_class = df.iloc[0]

print("\n📈 KPIs:")
print(f"🚗 Total Vehicles Registered (All Classes): {total_all:,}")
print(f"📊 Average Registrations per Class: {int(avg_all):,}")
print(f"🏆 Highest Registered Class: {top_class['vehicle_class']} ({top_class['total_registration']:,})")

plt.figure(figsize=(14, 6))
sns.barplot(
    x='total_registration',
    y='vehicle_class',
    data=df,
    palette='cubehelix'
)
plt.title("Vehicle Class-wise Total Registrations (2001–2024)")
plt.xlabel("Total Registrations")
plt.ylabel("Vehicle Class")
plt.tight_layout()
plt.savefig('.\\plots\\vehicle_class_all.png', dpi=300)
plt.close()

df.to_csv('.\\cleaned\\cleaned_vehicle_class_all.csv', index=False)
