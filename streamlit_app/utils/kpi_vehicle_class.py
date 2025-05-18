import pandas as pd
import plotly.express as px
import streamlit as st

CATEGORY_MAP = {
    'TWO WHEELER(NT)': '2W',
    'TWO WHEELER(T)': '2W',
    'TWO WHEELER (INVALID CARRIAGE)': '2W',
    'THREE WHEELER(T)': '3W',
    'THREE WHEELER(NT)': '3W',
    'FOUR WHEELER (INVALID CARRIAGE)': 'LMV',
    'LIGHT MOTOR VEHICLE': 'LMV',
    'LIGHT PASSENGER VEHICLE': 'LMV',
    'LIGHT GOODS VEHICLE': 'LMV',
    'HEAVY GOODS VEHICLE': 'HMV',
    'HEAVY PASSENGER VEHICLE': 'HMV',
    'HEAVY MOTOR VEHICLE': 'HMV',
    'MEDIUM GOODS VEHICLE': 'MMV',
    'MEDIUM PASSENGER VEHICLE': 'MMV',
    'MEDIUM MOTOR VEHICLE': 'MMV',
    'OTHER THAN MENTIONED ABOVE': 'Others'
}

def compute_kpis(df_vehicle_class):
    total_registered = df_vehicle_class['total_registration'].sum()
    most_common_class = df_vehicle_class.loc[df_vehicle_class['total_registration'].idxmax()]
    least_common_class = df_vehicle_class.loc[df_vehicle_class['total_registration'].idxmin()]

    st.metric("🚗 Total Registered EVs", f"{int(total_registered):,}")
    st.metric("📈 Most Registered Class", f"{most_common_class['vehicle_class']} ({int(most_common_class['total_registration']):,})")
    st.metric("📉 Least Registered Class", f"{least_common_class['vehicle_class']} ({int(least_common_class['total_registration']):,})")

def plot_vehicle_distribution(df_vehicle_class):
    fig = px.bar(
        df_vehicle_class.sort_values("total_registration", ascending=False),
        x='vehicle_class',
        y='total_registration',
        title="Vehicle Class-wise Total EV Registrations",
        labels={'vehicle_class': 'Vehicle Class', 'total_registration': 'Registrations'},
        color='total_registration',
        color_continuous_scale='Blues'
    )
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def compare_with_sales_data(df_vehicle_class, df_ev_sales_maker_cat):
    df_vehicle_class['Category'] = df_vehicle_class['vehicle_class'].map(CATEGORY_MAP)
    reg_by_cat = df_vehicle_class.groupby('Category')['total_registration'].sum().reset_index()

    if 'Cat' not in df_ev_sales_maker_cat.columns:
        for col in df_ev_sales_maker_cat.columns:
            if 'cat' in col.lower():
                df_ev_sales_maker_cat = df_ev_sales_maker_cat.rename(columns={col: 'Cat'})
                break

    ev_units_col = None
    for col in df_ev_sales_maker_cat.columns:
        if 'ev_count' in col.lower():
            ev_units_col = col
            break

    if 'Cat' in df_ev_sales_maker_cat.columns and ev_units_col:
        sales_by_cat = df_ev_sales_maker_cat.groupby('Cat')[ev_units_col].sum().reset_index()
        merged_df = pd.merge(reg_by_cat, sales_by_cat, left_on='Category', right_on='Cat', how='inner')

        fig = px.scatter(
            merged_df,
            x='total_registration',
            y=ev_units_col,
            text='Category',
            title='EV Sales vs Registered Vehicles (By Category)',
            labels={'total_registration': 'Total Registered', ev_units_col: 'EV Sales'}
        )
        fig.update_traces(marker=dict(size=15, color='blue'), textposition='top center')
        return fig
    else:
        st.warning("❗ Required columns for comparison not found in EV sales dataset.")
        return None
