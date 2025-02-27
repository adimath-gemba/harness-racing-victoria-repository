import streamlit as st
# import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu

# Set the page layout to wide mode for full-screen charts
st.set_page_config(layout="wide")

def authenticate_user():
    """Handles user authentication."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    
    if not st.session_state["authenticated"]:
        with st.sidebar:
            st.sidebar.title("Login")
            username = st.sidebar.text_input("Username")
            password = st.sidebar.text_input("Password", type="password")
            login_button = st.sidebar.button("Login")
            
            # Replace with actual authentication logic
            if login_button:
                if username == "gemba_test" and password == "@gemba#1":
                    st.session_state["authenticated"] = True
                    st.sidebar.success("Login successful!")
                    st.experimental_rerun()
                else:
                    st.sidebar.error("Invalid username or password.")
    
    return st.session_state["authenticated"]


# Ensure authentication before loading the app
if authenticate_user():

    def apply_custom_styles():
        st.markdown(
            """
            <style>
            .css-1d391kg { background-color: #003366 !important; } /* Dark blue header */
            .css-18e3th9 { background-color: #003366 !important; } /* Sidebar background */
            .css-1v3fvcr { color: white !important; } /* Sidebar text */
            .css-1v3fvcr:hover { background-color: #00A19A !important; } /* Sidebar hover effect changed to green */
            .css-1v3fvcr a { color: white !important; text-decoration: none; font-weight: bold; } /* Sidebar links */
            .css-1v3fvcr .icon { color: white !important; } /* Sidebar icons */
            .css-1v3fvcr .nav-link.active { background-color: #0055A4 !important; border-radius: 10px; } /* Active tab color */
            .css-1v3fvcr .menu-title { color: white !important; font-weight: bold; } /* Navigation title in white */
            </style>
            """,
            unsafe_allow_html=True
        )

    def predict_optimal_starters(WT, R, ARH, HORSE_ID, HTR, DBR, NR, PM, SW):
        """
        Predicts the optimal number of starters based on OLS regression results.
        """
        # Regression coefficients
        intercept = 0.0003
        beta_WT = -0.1259
        beta_R = 2.08
        beta_ARH = 26.80
        beta_HORSE_ID = 19.09
        beta_HTR = 49.58
        beta_DBR = -43.19
        beta_NR = -130.46
        beta_PM = -0.15	
        # SW = 1.05

        # Compute the number of starters using the formula
        S = (intercept +
            (beta_WT * WT) +
            (beta_R * SW * R) +
            (beta_ARH * ARH) +
            (beta_HORSE_ID * HORSE_ID) +
            (beta_HTR * HTR) +
            (beta_DBR * DBR) +
            (beta_NR * NR) +
            (beta_PM * PM))

        return math.ceil(S)

    # Predefined values
    WT = 232879.18  # Average Wagering Turnover
    R = 3179  # Total Races Per Year
    ARH = 14.37  # Avg Races Per Horse
    HORSE_ID = 3376  # Total Horses Registered
    HTR = 4.41  # Horse-to-Trainer Ratio
    DBR = 18.44  # Avg Days Between Races
    NR = 53.04  # Average National Rating
    PM = 19434.311  # Average Race Prize Money
    SW = 1.10

    def calculate_races(sum_of_starters, avg_starters_per_race):
        if avg_starters_per_race <= 0:
            return "Average starters per race must be greater than zero."
        return math.ceil(sum_of_starters / avg_starters_per_race)

    def calculate_meetings(num_races, races_per_meeting):
        if races_per_meeting <= 0:
            return "Number of races per meeting must be greater than zero."
        return math.ceil(num_races / races_per_meeting)

    def plot_forecast_chart(ax, years, values, forecast_year, forecast_value, title, ylabel, color):
        """Generates a large line chart with a dotted forecast section."""
        ax.plot(years, values, marker='o', linestyle='-', color=color, label="Historical Data", linewidth=2)
        ax.plot([years[-1], forecast_year], [values[-1], forecast_value], marker='o', linestyle='dotted', color=color, label="2025 Forecast", linewidth=2)
        ax.set_xlabel("Year", fontsize=14)
        ax.set_ylabel(ylabel, fontsize=14)
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xticks(list(years) + [forecast_year])
        ax.legend(fontsize=12)
        ax.grid(True, linestyle="--", alpha=0.6)

    def home():
        st.title("Race Scheduling Optimiser")

        # Predefined values
        WT = 232879.18  # Average Wagering Turnover
        R = 3179  # Total Races Per Year
        ARH = 14.37  # Avg Races Per Horse
        HORSE_ID = 3376  # Total Horses Registered
        HTR = 4.41  # Horse-to-Trainer Ratio
        DBR = 18.44  # Avg Days Between Races
        NR = 53.04  # Average National Rating
        PM = 19434.311  # Average Race Prize Money
        SW = 1.10
        
        # image_path = r"C:\Users\LintaroMiyashin\OneDrive - Tenka\Desktop\HRV\Screenshot 2025-02-18 154427.png"
        # st.image(image_path, caption="Model Driver Tree - Calculation", use_container_width=True)
        
        # if "dataset" not in st.session_state:
        #     st.session_state["dataset"] = None
        # if "saved_results" not in st.session_state:
        #     st.session_state["saved_results"] = []
        
        # User input for avg starters per race
        avg_starters_per_race = st.number_input("Enter the average starters per race:", min_value=1.0, value=9.16)

        # User input for number of races per meeting
        races_per_meeting = st.number_input("Enter the number of races to be conducted per meeting:", min_value=1.0, value=9.24)

        # User input for season_weighting of races per meeting
        season_weighting = st.number_input("Enter the season weghting (%):", min_value=0, value=5)
        season_weighting_final = SW - (season_weighting/100)

        # Get prediction
        predicted_starters = predict_optimal_starters(WT, R, ARH, HORSE_ID, HTR, DBR, NR, PM, season_weighting_final)

        # Calculate number of races
        num_races = calculate_races(predicted_starters, avg_starters_per_race)

        # Calculate number of meetings
        num_meetings = calculate_meetings(num_races, races_per_meeting)


        # Display results
        st.write(f"Predicted Starters: {predicted_starters}")
        st.write(f"Optimal number of races to be conducted: {num_races}")
        st.write(f"Optimal number of meetings to be conducted: {num_meetings}")

        # Historical Data
        years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
        starters = np.array([32515, 32433, 35003, 35217, 36175, 37557, 34133])
        races = np.array([3853, 3842, 4029, 4001, 4164, 4163, 3753])
        meetings = np.array([437, 438, 472, 437, 439, 442, 427])

        # # Historical Data
        # years = np.array([2021, 2022, 2023, 2024])
        # starters = np.array([35217, 36175, 37557, 34133])
        # races = np.array([4001, 4164, 4163, 3753])
        # meetings = np.array([437, 439, 442, 427])

        # Add forecasted values
        years_extended = np.append(years, [2025])
        starters_extended = np.append(starters, [predicted_starters])
        races_extended = np.append(races, [num_races])
        meetings_extended = np.append(meetings, [num_meetings])

        forecast_year = 2025

        # Full-width container for max chart size
        with st.container():
            fig, axes = plt.subplots(1, 3, figsize=(16, 6))

            plot_forecast_chart(axes[0], years, starters, forecast_year, predicted_starters, "Starters", "Starters", "crimson")
            plot_forecast_chart(axes[1], years, races, forecast_year, num_races, "Races", "Races", "darkblue")
            plot_forecast_chart(axes[2], years, meetings, forecast_year, num_meetings, "Meetings", "Meetings", "darkgreen")

            plt.tight_layout()  # Adjust layout for best fit
            st.pyplot(fig, use_container_width=True)



        
        # uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
        # if uploaded_file is not None:
        #     df = pd.read_csv(uploaded_file)
        #     df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces in column names
        #     st.session_state["dataset"] = df
        #     st.success("Dataset uploaded successfully!")
        
        # if st.session_state["dataset"] is not None:
        #     df = st.session_state["dataset"]
            

                    
            # # Save results for comparison, preventing duplicates
            # new_result = {
            #     "Avg Starters per Race": avg_starters_per_race,
            #     "Races per Meeting": races_per_meeting,
            #     "Predicted Sum of Starters": sum_of_starters,
            #     "Optimal Races": num_races,
            #     "Optimal Meetings": num_meetings
            # }
            
            # if new_result not in st.session_state["saved_results"]:
            #     if st.button("Save Result"):
            #         st.session_state["saved_results"].append(new_result)

    def forecast():
        st.title("Forecast for 2026")

        # Predefined values
        WT = 232879.18  # Average Wagering Turnover
        R = 3179  # Total Races Per Year
        ARH = 14.37  # Avg Races Per Horse
        HORSE_ID = 3255  # Total Horses Registered
        HTR = 4.41  # Horse-to-Trainer Ratio
        DBR = 18.44  # Avg Days Between Races
        NR = 53.04  # Average National Rating
        PM = 19434.311  # Average Race Prize Money
        SW = 1.10
        
        # image_path = r"C:\Users\LintaroMiyashin\OneDrive - Tenka\Desktop\HRV\Screenshot 2025-02-18 154427.png"
        # st.image(image_path, caption="Model Driver Tree - Calculation", use_container_width=True)
        
        # if "dataset" not in st.session_state:
        #     st.session_state["dataset"] = None
        # if "saved_results" not in st.session_state:
        #     st.session_state["saved_results"] = []
        
        # User input for avg starters per race
        avg_starters_per_race = st.number_input("Enter the average starters per race:", min_value=1.0, value=9.16)

        # User input for number of races per meeting
        races_per_meeting = st.number_input("Enter the number of races to be conducted per meeting:", min_value=1.0, value=9.24)

        # User input for season_weighting of races per meeting
        season_weighting = st.number_input("Enter the season weghting (%):", min_value=0, value=5)
        season_weighting_final = SW - (season_weighting/100)

        # Get prediction
        predicted_starters = predict_optimal_starters(WT, R, ARH, HORSE_ID, HTR, DBR, NR, PM, season_weighting_final)

        # Calculate number of races
        num_races = calculate_races(predicted_starters, avg_starters_per_race)

        # Calculate number of meetings
        num_meetings = calculate_meetings(num_races, races_per_meeting)


        # Display results
        st.write(f"Predicted Starters: {predicted_starters}")
        st.write(f"Optimal number of races to be conducted: {num_races}")
        st.write(f"Optimal number of meetings to be conducted: {num_meetings}")

            # Historical Data
        years = np.array([2021, 2022, 2023, 2024])
        starters = np.array([35000, 36000, 35500, 34500])
        races = np.array([4001, 4164, 4163, 3753])
        meetings = np.array([450, 460, 455, 440])

        # Add forecasted values
        years_extended = np.append(years, [2025, 2026])
        starters_extended = np.append(starters, [predicted_starters, predicted_starters - 2000])
        races_extended = np.append(races, [num_races, num_races - 300])
        meetings_extended = np.append(meetings, [num_meetings, num_meetings - 40])

        forecast_year = 2025

        # Generate charts with a dotted 2025 forecast
        plot_forecast_chart(years, starters, forecast_year, predicted_starters, "Target Total Starters Per Annum", "Total Starters", "crimson")
        plot_forecast_chart(years, races, forecast_year, num_races, "Target Total Races Per Annum", "Total Races", "darkblue")
        plot_forecast_chart(years, meetings, forecast_year, num_meetings, "Target Total Meetings Per Annum", "Total Meetings", "darkgreen")


    # def data_comparison():
    #     st.title("Comparison: Benchmark vs. Saved Results")
        
    #     if st.session_state["dataset"] is None:
    #         st.warning("No data uploaded. Please upload a CSV file in the Home page first.")
    #     else:
    #         df = st.session_state["dataset"]
    #         required_columns = ["Year", "Average of STARTERS", "Avg Number of Races", "Sum of STARTERS", "Count of RACE_MEETING_CODE", "Count of RACE_CODE"]
            
    #         # Check if all required columns exist
    #         missing_columns = [col for col in required_columns if col not in df.columns]
    #         if missing_columns:
    #             st.error(f"The dataset is missing the following required columns: {', '.join(missing_columns)}")
    #             return
            
    #         years = df["Year"].unique()
    #         selected_year = st.selectbox("Select Benchmark Year", sorted(years, reverse=True))  # Dropdown for Year Selection
    #         st.subheader(f"Benchmark Year: {selected_year}")  # Display it as text
            
    #         benchmark_data = df[df["Year"] == selected_year][required_columns].copy()
    #         benchmark_data["Year"] = benchmark_data["Year"].astype(str)
            
    #         if not st.session_state["saved_results"]:
    #             st.warning("No saved results found. Try saving some results in the Home page.")
    #             return

    #         saved_results_df = pd.DataFrame(st.session_state["saved_results"])
            
    #         for col in saved_results_df.columns:
    #             saved_results_df[col] = pd.to_numeric(saved_results_df[col], errors="coerce")
            
    #         st.subheader("Comparison Table")
    #         st.dataframe(saved_results_df)
                
    #         st.subheader("Benchmark Data")
    #         st.dataframe(benchmark_data)

    def model_logic():
        st.title("Model Logic")
        st.write("Coming Soon...")

    apply_custom_styles()

    with st.sidebar:
        # selected = option_menu("Navigation", ["HOME", "Data Comparison", "Model Logic", "Forecast"],
        selected = option_menu("Navigation", ["HOME"],
                            icons=["house", "table", "cpu"],
                            menu_icon="cast", default_index=0, styles={
                                "container": {"padding": "5px", "background-color": "#003366"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "white"},
                                "nav-link-selected": {"background-color": "#0055A4", "border-radius": "10px"},
                                "nav-link:hover": {"background-color": "#00A19A"},
                                "menu-title": {"color": "white", "font-weight": "bold"}
                            })

    if "selected" in locals() and selected == "HOME":
        home()
    elif "selected" in locals() and selected == "Data Comparison":
        data_comparison()
    elif "selected" in locals() and selected == "Model Logic":
        model_logic()
    elif "selected" in locals() and selected == "Forecast":
        forecast()
