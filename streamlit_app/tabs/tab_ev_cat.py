import streamlit as st
from utils.kpi_ev_cat import compute_kpis, plot_sales_trend, plot_ev_by_type, preprocess_date

def render_ev_cat_tab(df_ev_cat):
    st.markdown("## ⚡ EV Category Overview")
    df_ev_cat = preprocess_date(df_ev_cat)
    with st.sidebar:
        st.markdown("### 🔍 Filters")
        all_years = sorted(df_ev_cat['Year'].unique())
        selected_years = st.multiselect("Select Year(s)", all_years, default=all_years)

        months = df_ev_cat['Date'].dt.month_name().unique()
        selected_months = st.multiselect("Select Month(s)", months, default=list(months))

    df_filtered = df_ev_cat[
        (df_ev_cat['Year'].isin(selected_years)) &
        (df_ev_cat['Date'].dt.month_name().isin(selected_months))
    ]

    st.markdown("### 📊 Key Performance Indicators")
    kpis = compute_kpis(df_filtered)
    for label, value in kpis.items():
        st.metric(label=label, value=value)
        st.markdown("<br>", unsafe_allow_html=True)  

    st.divider()
    st.markdown("### 📈 EV Sales Trend")
    st.plotly_chart(plot_sales_trend(df_filtered), use_container_width=True)
    st.markdown("### 🚘 Latest Month EV Breakdown by Type")
    st.plotly_chart(plot_ev_by_type(df_filtered), use_container_width=True)

    st.caption("📊 Data Source: Ministry of Road Transport & Highways, India")
