# ⚡ India EV Market (2001–2024): In-Depth Dashboard with Streamlit

Welcome to a comprehensive visual and analytical dashboard built using **Streamlit** to explore the evolution of the **Electric Vehicle (EV) market in India from 2001 to 2024**. This project includes KPIs, trend analytics, and manufacturer insights across 5 key datasets.

![App Screenshot](screenshots/ev_category.png)

---

## 🚀 Features

- 📊 8–10 Key Performance Indicators (KPIs) per dataset
- 🗃️ Five structured, filterable tabs:
  - EV Category Overview
  - EV Makers by Place
  - Sales by Maker & Category
  - Charging Infrastructure
  - Vehicle Class Insights
- 📅 Interactive time & category filters
- 🌐 Streamlit-powered web UI with consistent theming
- 📍 Geospatial view of maker headquarters
- ⚙️ Modular, extensible, and fully open-source

---

## 📂 Project Structure

India_EV_Market_Analysis/
├── .streamlit/
│ └── config.toml
├── cleaned/
│ ├── cleaned_ev_cat.csv
│ ├── cleaned_ev_maker_place.csv
│ ├── cleaned_ev_sales_by_maker_cat.csv
│ ├── cleaned_operational_pc.csv
│ └── cleaned_vehicle_class_all.csv
├── streamlit_app/
│ ├── main.py
│ ├── tabs/
│ │ ├── tab_ev_cat.py
│ │ ├── tab_ev_maker_place.py
│ │ ├── tab_ev_sales_by_maker_cat.py
│ │ ├── tab_operational_pc.py
│ │ └── tab_vehicle_class.py
│ └── utils/
│ ├── kpi_ev_cat.py
│ ├── kpi_ev_maker_place.py
│ ├── kpi_ev_sales_by_maker_cat.py
│ ├── kpi_operational_pc.py
│ └── kpi_vehicle_class.py
├── run.sh
├── requirements.txt
└── README.md
## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/India_EV_Market_Analysis.git
cd India_EV_Market_Analysis
2. Set Up Python Virtual Environment

python -m venv venv
source venv/bin/activate       # On Windows use: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

🏃 Running the Application

From the project root, run:

streamlit run streamlit_app/main.py

The app will launch in your default browser at http://localhost:8501.
⚙️ Configuration

The app uses a minimalistic theme and custom title set in .streamlit/config.toml. The favicon is an EV-themed icon from Flaticon.

If you want to customize, modify .streamlit/config.toml:

[theme]
primaryColor = "#0D47A1"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"
textColor = "#212121"
font = "sans serif"

[server]
headless = true
enableCORS = false

[global]
title = "India EV Market In Depth"

[browser]
favicon = "https://cdn-icons-png.flaticon.com/512/1236/1236953.png"

📊 Data Overview

The datasets are cleaned and stored under the /cleaned folder:
    cleaned_ev_cat.csv: Monthly EV sales by category (2001–2024)
    cleaned_ev_maker_place.csv: EV manufacturers and their headquarters locations
    cleaned_ev_sales_by_maker_cat.csv: Sales by manufacturer and EV category (2015–2024)
    cleaned_operational_pc.csv: Public charging stations by state
    cleaned_vehicle_class_all.csv: Vehicle class registrations (latest)
Each dataset powers a corresponding tab in the dashboard with dedicated KPIs and visualizations.

## 🧭 App Structure

India_EV_Market_Analysis/
│
├── .streamlit/ # Streamlit config folder
│ └── config.toml
│
├── cleaned/ # Cleaned CSV datasets
│ ├── cleaned_ev_cat.csv
│ ├── cleaned_ev_maker_place.csv
│ ├── cleaned_ev_sales_by_maker_cat.csv
│ ├── cleaned_operational_pc.csv
│ └── cleaned_vehicle_class_all.csv
│
├── streamlit_app/
│ ├── main.py # Main Streamlit app
│ ├── tabs/ # Individual tab UI scripts
│ │ ├── tab_ev_cat.py
│ │ ├── tab_ev_maker_place.py
│ │ ├── tab_ev_sales_by_maker_cat.py
│ │ ├── tab_operational_pc.py
│ │ └── tab_vehicle_class.py
│ └── utils/ # KPI + plotting utility modules
│ ├── kpi_ev_cat.py
│ ├── kpi_ev_maker_place.py
│ ├── kpi_ev_sales_by_maker_cat.py
│ ├── kpi_operational_pc.py
│ └── kpi_vehicle_class.py
│
├── requirements.txt
└── README.md


---

## 🧩 Features

- 🧮 **8–10 Key Performance Indicators** per tab for actionable insights.
- 🗓️ **Multi-filter support** by Year, Month, Manufacturer, State, and Category.
- 📊 **Dynamic Visualizations** with Plotly & Matplotlib.
- 📍 **Geographic Trends** by state and manufacturer location.
- 🚘 **Vehicle Class Comparison** with EV sales for alignment analysis.
- 📈 **Time Series Analysis** for EV sales over years.
- 🧼 Clean and minimal UI with consistent styling across tabs.

---

## 🖥️ Tabs Overview

| Tab Name                  | Dataset                        | Highlights                                         |
|---------------------------|--------------------------------|----------------------------------------------------|
| EV Category Overview      | `cleaned_ev_cat.csv`           | Category-wise trends, sales trend over time        |
| EV Makers by Place        | `cleaned_ev_maker_place.csv`   | Maker HQ map, region-wise distribution             |
| EV Sales by Maker & Cat   | `cleaned_ev_sales_by_maker_cat`| Maker/category filters, top contributors           |
| Charging Stations Overview| `cleaned_operational_pc.csv`   | State-wise distribution, averages                  |
| Vehicle Class Overview    | `cleaned_vehicle_class_all.csv`| Class-wise total EVs, compared with category sales |

## 🚀 Deployment

To deploy the app locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/India_EV_Market_Analysis.git
   cd India_EV_Market_Analysis

    Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # macOS/Linux

Install dependencies:

pip install -r requirements.txt

Run the app:
    double click `run.bat`

🛠️ Tech Stack
    Language: Python 3.x
    Framework: Streamlit
    Data Viz: Plotly, Matplotlib, Pandas
    UI Theming: Streamlit config + responsive layout
    Data Sources: Ministry of Road Transport & Highways (India)

🙌 Acknowledgements
    📊 VAHAN Dashboard
    🌍 Flaticon for EV icons
    ❤️ Open-source tools & the Streamlit community

📬 Contact
For any suggestions, issues, or contributions:
    GitHub Issues tab
    Email: sakshamrao2004@gmail.com

