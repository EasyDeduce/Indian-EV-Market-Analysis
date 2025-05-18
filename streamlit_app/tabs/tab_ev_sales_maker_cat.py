import streamlit as st
import pandas as pd
from utils.kpi_ev_sales_maker_cat import compute_kpis, plot_yearly_sales_by_maker, plot_category_distribution

def render_ev_sales_maker_cat_tab(df):
    st.header("📈 EV Sales by Maker & Category (2015–2024)")

    df = pd.read_csv("./cleaned/cleaned_ev_sales_by_maker_cat.csv")
    kpis = compute_kpis(df)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total EVs", kpis["Total EVs (2015–2024)"])
    col2.metric("Top EV Maker", kpis["Top EV Maker"])
    col3.metric("Top Category", kpis["Top Vehicle Category"])

    col4, col5 = st.columns(2)
    col4.metric("Year with Max Sales", kpis["Year with Max Sales"])
    col5.metric("Avg Sales / Year", kpis["Average Sales per Year"])

    with st.expander("Top 5 Makers"):
        st.bar_chart(kpis["Top 5 Makers"])

    with st.expander("Top 5 Categories"):
        st.bar_chart(kpis["Top 5 Categories"])

    st.subheader("🧭 EV Sales Trends by Maker")
    st.pyplot(plot_yearly_sales_by_maker(df))

    st.subheader("🧭 Category-wise EV Distribution")
    st.pyplot(plot_category_distribution(df))
