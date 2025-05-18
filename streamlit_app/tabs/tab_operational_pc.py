import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.kpi_operational_pc import compute_kpis, plot_statewise_distribution

def render_operational_pc_tab(df):
    st.header("🔌 Operational Public Charging Stations Overview")

    df = pd.read_csv('./cleaned/cleaned_operational_pc.csv')
    kpis = compute_kpis(df)

    with st.container():
        st.markdown("### 📊 Key Performance Indicators")
        cols = st.columns(4)
        cols[0].metric("Total Charging Stations", f"{kpis['Total Charging Stations']:,}")
        cols[1].metric("Total States", kpis['Total States'])
        cols[2].metric("Max Stations in a State", f"{kpis['Max Stations in a State']:,}")
        cols[3].metric("Min Stations in a State", f"{kpis['Min Stations in a State']:,}")

        st.markdown("---")

        cols2 = st.columns(4)
        cols2[0].metric("Average Stations per State", f"{kpis['Average Stations per State']:.2f}")
        cols2[1].metric("States with >100 Stations", kpis['States with >100 Stations'])
        cols2[2].metric("States with <10 Stations", kpis['States with <10 Stations'])
        cols2[3].metric("Median Stations per State", f"{kpis['Median Stations per State']:,}")

    st.markdown("---")
    with st.container():
        st.markdown("### 🔎 Filter States")
        states_selected = st.multiselect(
            "Select States to Display",
            options=sorted(df['state'].unique()),
            default=sorted(df['state'].unique()),
            help="Filter the states to view charging station data."
        )
        df_filtered = df[df['state'].isin(states_selected)]
    with st.container():
        st.markdown("### 📍 Statewise Charging Stations Distribution")
        fig = plot_statewise_distribution(df_filtered)
        st.pyplot(fig, use_container_width=True)
