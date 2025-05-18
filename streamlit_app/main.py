import streamlit as st

import pandas as pd
from tabs.tab_ev_cat import render_ev_cat_tab
from tabs.tab_ev_maker_place import render_ev_maker_place_tab
from tabs.tab_ev_sales_maker_cat import render_ev_sales_maker_cat_tab
from tabs.tab_operational_pc import render_operational_pc_tab
from tabs.tab_vehicle_class import render_vehicle_class_tab

df_ev_cat = pd.read_csv("./cleaned/cleaned_ev_cat.csv")
df_ev_maker_place = pd.read_csv("./cleaned/cleaned_ev_maker_place.csv")
df_ev_sales_maker_cat = pd.read_csv("./cleaned/cleaned_ev_sales_by_maker_cat.csv")
df_operational_pc = pd.read_csv("./cleaned/cleaned_operational_pc.csv")
df_vehicle_class = pd.read_csv("./cleaned/cleaned_vehicle_class_all.csv")

st.set_page_config(page_title="India EV Market Analysis (2001–2024)", layout="wide",page_icon="https://cdn-icons-png.flaticon.com/512/1236/1236953.png")

tabs = {
    "EV Category Overview": lambda: render_ev_cat_tab(df_ev_cat),
    "EV Makers by Place": lambda: render_ev_maker_place_tab(df_ev_maker_place),
    "EV Sales by Maker & Category": lambda: render_ev_sales_maker_cat_tab(df_ev_sales_maker_cat),
    "Operational Public Charging Stations": lambda: render_operational_pc_tab(df_operational_pc),
    "Vehicle Class Overview": lambda: render_vehicle_class_tab(df_vehicle_class, df_ev_sales_maker_cat),
}

selected_tab = st.sidebar.radio("📁 Navigate", list(tabs.keys()))
tabs[selected_tab]()
