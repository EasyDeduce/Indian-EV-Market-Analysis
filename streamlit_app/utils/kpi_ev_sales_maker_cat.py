import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def compute_kpis(df):
    total_evs = df['EV_Count'].sum()
    top_maker = df.groupby('Maker')['EV_Count'].sum().idxmax()
    top_cat = df.groupby('Cat')['EV_Count'].sum().idxmax()
    year_with_max_sales = df.groupby('Year')['EV_Count'].sum().idxmax()
    top_5_makers = df.groupby('Maker')['EV_Count'].sum().nlargest(5)
    top_5_cats = df.groupby('Cat')['EV_Count'].sum().nlargest(5)
    avg_sales_per_year = df.groupby('Year')['EV_Count'].mean().mean()

    return {
        "Total EVs (2015–2024)": f"{total_evs:,}",
        "Top EV Maker": top_maker,
        "Top Vehicle Category": top_cat,
        "Year with Max Sales": year_with_max_sales,
        "Average Sales per Year": int(avg_sales_per_year),
        "Top 5 Makers": top_5_makers,
        "Top 5 Categories": top_5_cats
    }

def plot_yearly_sales_by_maker(df):
    plt.figure(figsize=(10,6))
    sns.lineplot(data=df, x='Year', y='EV_Count', hue='Maker', estimator='sum', ci=None)
    plt.title("Yearly EV Sales by Maker")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

def plot_category_distribution(df):
    cat_dist = df.groupby('Cat')['EV_Count'].sum().sort_values(ascending=False)
    plt.figure(figsize=(10,6))
    sns.barplot(x=cat_dist.values, y=cat_dist.index, palette="viridis")
    plt.title("Total EV Sales by Vehicle Category")
    plt.xlabel("EV Units")
    plt.ylabel("Category")
    plt.tight_layout()
    return plt.gcf()
