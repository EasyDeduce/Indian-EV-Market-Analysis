import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(path='./cleaned/cleaned_ev_sales_by_maker_cat.csv'):
    df = pd.read_csv(path)
    return df

def calculate_kpis(df):
    total_evs = df['EV_Count'].sum()
    sales_by_year = df.groupby('Year')['EV_Count'].sum()
    top_makers = df.groupby('Maker')['EV_Count'].sum().sort_values(ascending=False).head(5)
    top_cats = df.groupby('Cat')['EV_Count'].sum().sort_values(ascending=False).head(5)
    top_combos = df.groupby(['Maker', 'Cat'])['EV_Count'].sum().sort_values(ascending=False).head(5)
    growth_pct = ((sales_by_year.loc[2024] / sales_by_year.loc[2015]) - 1) * 100
    peak_year = sales_by_year.idxmax()
    avg_sales_maker = df.groupby('Maker')['EV_Count'].mean().sort_values(ascending=False).head(5)
    top3_makers = top_makers.index[:3]
    df_top3 = df[df['Maker'].isin(top3_makers)]
    sales_top3_yearly = df_top3.groupby(['Year', 'Maker'])['EV_Count'].sum().unstack()
    top3_cats = top_cats.index[:3]
    df_top3_cats = df[df['Cat'].isin(top3_cats)]
    sales_top3_cats_yearly = df_top3_cats.groupby(['Year', 'Cat'])['EV_Count'].sum().unstack()

    kpis = {
        "total_evs": total_evs,
        "sales_by_year": sales_by_year,
        "top_makers": top_makers,
        "top_cats": top_cats,
        "top_combos": top_combos,
        "growth_pct": growth_pct,
        "peak_year": peak_year,
        "avg_sales_maker": avg_sales_maker,
        "sales_top3_yearly": sales_top3_yearly,
        "sales_top3_cats_yearly": sales_top3_cats_yearly
    }
    return kpis

def plot_sales_by_year(sales_by_year):
    plt.figure(figsize=(8,4))
    sns.lineplot(x=sales_by_year.index, y=sales_by_year.values, marker='o')
    plt.title("Total EV Sales by Year (2015-2024)")
    plt.xlabel("Year")
    plt.ylabel("EV Sales")
    plt.tight_layout()
    return plt.gcf()

def plot_top_makers(top_makers):
    plt.figure(figsize=(8,4))
    sns.barplot(x=top_makers.values, y=top_makers.index, palette="viridis")
    plt.title("Top 5 EV Manufacturers by Sales (2015-2024)")
    plt.xlabel("Total EV Sales")
    plt.ylabel("Manufacturer")
    plt.tight_layout()
    return plt.gcf()

def plot_top_categories(top_cats):
    plt.figure(figsize=(8,4))
    sns.barplot(x=top_cats.values, y=top_cats.index, palette="magma")
    plt.title("Top 5 Vehicle Categories by Sales (2015-2024)")
    plt.xlabel("Total EV Sales")
    plt.ylabel("Vehicle Category")
    plt.tight_layout()
    return plt.gcf()

def plot_top3_makers_trend(sales_top3_yearly):
    plt.figure(figsize=(10,5))
    sns.lineplot(data=sales_top3_yearly, markers=True)
    plt.title("Yearly EV Sales Trend for Top 3 Manufacturers")
    plt.xlabel("Year")
    plt.ylabel("EV Sales")
    plt.legend(title='Maker')
    plt.tight_layout()
    return plt.gcf()

def plot_top3_categories_trend(sales_top3_cats_yearly):
    plt.figure(figsize=(10,5))
    sns.lineplot(data=sales_top3_cats_yearly, markers=True)
    plt.title("Yearly EV Sales Trend for Top 3 Vehicle Categories")
    plt.xlabel("Year")
    plt.ylabel("EV Sales")
    plt.legend(title='Category')
    plt.tight_layout()
    return plt.gcf()
