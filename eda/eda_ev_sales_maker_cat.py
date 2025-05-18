import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("./plots", exist_ok=True)

df = pd.read_csv("./cleaned/cleaned_ev_sales_by_maker_cat.csv")

sns.set_theme(style="whitegrid")

yearly_totals = df.groupby('Year')['EV_Count'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_totals, x='Year', y='EV_Count', marker='o', color='b')
plt.title('Yearly Total EV Sales in India (2015–2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Total EVs Sold', fontsize=14)
plt.xticks(yearly_totals['Year'])
plt.tight_layout()
plt.savefig("./plots/yearly_total_ev_sales.png")
plt.close()

top_makers = df.groupby('Maker')['EV_Count'].sum().sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(12, 7))
sns.barplot(data=top_makers, y='Maker', x='EV_Count', palette='viridis')
plt.title('Top 10 EV Manufacturers by Total Sales (2015–2024)', fontsize=16)
plt.xlabel('Total EVs Sold', fontsize=14)
plt.ylabel('Manufacturer', fontsize=14)
plt.tight_layout()
plt.savefig("./plots/top_10_ev_makers.png")
plt.close()

top_categories = df.groupby('Cat')['EV_Count'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=top_categories, x='Cat', y='EV_Count', palette='coolwarm')
plt.title('EV Sales by Vehicle Category in India (2015–2024)', fontsize=16)
plt.xlabel('Vehicle Category', fontsize=14)
plt.ylabel('Total EVs Sold', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("./plots/ev_sales_by_category.png")
plt.close()

year_cat = df.groupby(['Year', 'Cat'])['EV_Count'].sum().unstack(fill_value=0)
plt.figure(figsize=(14, 8))
year_cat.plot(kind='bar', stacked=True, colormap='tab20', width=0.8)
plt.title('Yearly EV Sales by Vehicle Category in India (2015–2024)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of EVs Sold', fontsize=14)
plt.xticks(rotation=0)
plt.legend(title='Vehicle Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("./plots/yearly_ev_sales_by_category_stacked.png")
plt.close()
