import streamlit as st
import pandas as pd
from utils.kpi_ev_maker_place import compute_kpis, plot_state_distribution, get_places_by_state

def render_ev_maker_place_tab(df):
    st.header("EV Manufacturers by Place")
    df = pd.read_csv("./cleaned/cleaned_ev_maker_place.csv")

    kpis = compute_kpis(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Manufacturers", kpis["Total Manufacturers"])
    col2.metric("Total Locations", kpis["Total Locations"])
    col3.metric("Top Manufacturer", kpis["Top Manufacturer"])

    col4, col5 = st.columns(2)
    col4.metric("State w/ Max Makers", kpis["State with Max Manufacturers"])
    col5.metric("States w/ ≥5 Plants", kpis["States with ≥5 Plants"])

    st.markdown("### 🌍 Top States (Plant Count)")
    st.dataframe(kpis["Top States"].reset_index().rename(columns={'index': 'State', 'state': 'Count'}))

    st.markdown("### 🏙️ Top Cities/Towns")
    st.dataframe(kpis["Top Places"].reset_index().rename(columns={'index': 'Place', 'place': 'Count'}))

    st.markdown("### 📈 State-wise Distribution")
    st.pyplot(plot_state_distribution(df))

    st.markdown("### 🔍 Explore Places by State")
    states = df['state'].unique().tolist()
    selected_state = st.selectbox("Select a state", sorted(states))
    places = get_places_by_state(df, selected_state)
    st.bar_chart(places)
