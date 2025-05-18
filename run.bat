@echo off
call venv\Scripts\activate
streamlit run streamlit_app\main.py --server.headless false
