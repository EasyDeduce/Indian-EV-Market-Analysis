import streamlit as st
from utils.kpi_vehicle_class import compute_kpis, plot_vehicle_distribution, compare_with_sales_data

def render_vehicle_class_tab(df_vehicle_class, df_ev_sales_maker_cat):
    st.title("🚘 Vehicle Class Overview")

    st.subheader("🔢 Key Performance Indicators")
    compute_kpis(df_vehicle_class) 

    st.subheader("📊 Total Vehicle Registrations by Class")
    fig1 = plot_vehicle_distribution(df_vehicle_class)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("🔁 EV Sales vs Registered Vehicles")
    fig2 = compare_with_sales_data(df_vehicle_class, df_ev_sales_maker_cat)
    if fig2:
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("Comparison chart could not be generated. Ensure EV Sales data has both category and sales columns.")
