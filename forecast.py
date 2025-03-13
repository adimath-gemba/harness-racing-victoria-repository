# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt
# import math


# # ----------------- Prediction Functions -----------------
# def predict_optimal_starters(WT, R, ARH, HORSE_ID, HTR, DBR, NR, PM, SW):
#     intercept = 0.0003
#     beta_WT = -0.1259
#     beta_R = 2.08
#     beta_ARH = 26.80
#     beta_HORSE_ID = 19.09
#     beta_HTR = 49.58
#     beta_DBR = -43.19
#     beta_NR = -130.46
#     beta_PM = -0.15

#     S = (intercept +
#          (beta_WT * WT) +
#          (beta_R * SW * R) +
#          (beta_ARH * ARH) +
#          (beta_HORSE_ID * HORSE_ID) +
#          (beta_HTR * HTR) +
#          (beta_DBR * DBR) +
#          (beta_NR * NR) +
#          (beta_PM * PM))

#     return math.ceil(S)

# def calculate_races(sum_of_starters, avg_starters_per_race):
#     return math.ceil(sum_of_starters / avg_starters_per_race)

# def calculate_meetings(num_races, races_per_meeting):
#     return math.ceil(num_races / races_per_meeting)

# def plot_forecast_chart(ax, years, values, forecast_year, forecast_value,
#                         title, ylabel, color):
#     ax.plot(years, values, marker='o', linestyle='-', color=color, linewidth=2, label="Historical Data")
#     ax.plot([years[-1], forecast_year], [values[-1], forecast_value], marker='o', linestyle='dotted', color=color, linewidth=2, label="2025 Forecast")
#     ax.set_xlabel("Year", fontsize=14)
#     ax.set_ylabel(ylabel, fontsize=14)
#     ax.set_title(title, fontsize=16, fontweight='bold')
#     ax.set_xticks(list(years) + [forecast_year])
#     ax.legend(fontsize=12)
#     ax.grid(True, linestyle="--", alpha=0.6)

# # ----------------- Home Page -----------------

# def show():
#     st.title("Forecast")

#     # Input Fields
#     avg_starters_per_race = st.number_input("Enter the average starters per race:", min_value=1.0, value=9.16, help = "The average number of starters you would like to achieve")
#     races_per_meeting = st.number_input("Enter the number of races per meeting:", min_value=1.0, value=9.24, help = "The average number of races per meeting you would like achieve")
#     season_weighting = st.number_input("Enter the winter to summer race ratio (%):", min_value=0, value=5, help = "The ratio of winter to summer races you would like achieve, eg: 5% would mean 5% more races in winter than summer")

#     # Constants
#     WT, R, ARH, HORSE_ID, HTR, DBR, NR, PM = 232879.18, 3179, 14.37, 3376, 4.41, 18.44, 53.04, 19434.311
#     SW = 1.10 - (season_weighting / 100)

#     #submit instructions
#     st.markdown("<h6 style='text-align: center;'>To visualise optimised outputs please adjust metrics above and press submit</h6>", unsafe_allow_html=True)
#     # st.text("To visualise optimised outputs please adjust metrics above and press submit")
#     if st.button("Submit"):
#         # Predictions
#         predicted_starters = predict_optimal_starters(WT, R, ARH, HORSE_ID, HTR, DBR, NR, PM, SW)
#         num_races = calculate_races(predicted_starters, avg_starters_per_race)
#         num_meetings = calculate_meetings(num_races, races_per_meeting)

#         # # Ensure session state exists
#         # if "saved_results" not in st.session_state:
#         #     st.session_state["saved_results"] = []

#         # # Count existing predictions for 2025
#         # prediction_count = sum(1 for entry in st.session_state["saved_results"] if "2025 Prediction" in entry["Year"])
#         # next_prediction_number = prediction_count + 1

#         # New user input dictionary
#         # new_inputs = {
#         #     "Year": f"2025 Prediction {next_prediction_number}",
#         #     "Avg Starters per Race": avg_starters_per_race,
#         #     "Races per Meeting": races_per_meeting,
#         #     "Predicted Starters": predicted_starters,
#         #     "Number of Races": num_races,
#         #     "Number of Meetings": num_meetings,
#         #     "Season Weighting": season_weighting,
#         # }

#         # # Check if an entry with the same core values already exists
#         # core_values = {
#         #     "Avg Starters per Race": avg_starters_per_race,
#         #     "Races per Meeting": races_per_meeting,
#         #     "Predicted Starters": predicted_starters,
#         #     "Number of Races": num_races,
#         #     "Number of Meetings": num_meetings,
#         #     "Season Weighting": season_weighting,
#         # }

#         # duplicate_found = any(
#         #     {k: v for k, v in entry.items() if k != "Year"} == core_values for entry in st.session_state["saved_results"]
#         # )

#         # # Store the new input only if it's unique (excluding Year)
#         # if not duplicate_found:
#         #     st.session_state["saved_results"].append(new_inputs)

#         # # Limit stored inputs to last 10 entries
#         # st.session_state["saved_results"] = st.session_state["saved_results"][-10:]

#         # Create 3 columns for KPIs (aligned with charts)
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             st.markdown(f"<h4 style='text-align: center;'>Predicted Starters</h4>", unsafe_allow_html=True)
#             st.markdown(f"<h3 style='text-align: center; color: black;'>{predicted_starters:,}</h3>", unsafe_allow_html=True)

#         with col2:
#             st.markdown(f"<h4 style='text-align: center;'>Optimal Number of Races</h4>", unsafe_allow_html=True)
#             st.markdown(f"<h3 style='text-align: center; color: black;'>{num_races:,}</h3>", unsafe_allow_html=True)

#         with col3:
#             st.markdown(f"<h4 style='text-align: center;'>Optimal Number of Meetings</h4>", unsafe_allow_html=True)
#             st.markdown(f"<h3 style='text-align: center; color: black;'>{num_meetings:,}</h3>", unsafe_allow_html=True)



#         # Historical Data
#         years = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
#         starters = np.array([32515, 32433, 35003, 35217, 36175, 37557, 34133])
#         races = np.array([3853, 3842, 4029, 4001, 4164, 4163, 3753])
#         meetings = np.array([437, 438, 472, 437, 439, 442, 427])

#         forecast_year = [2025]

#         # Create 3 columns for graphs
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             fig, ax = plt.subplots()
#             plot_forecast_chart(ax, years, starters, forecast_year, predicted_starters, "Starters", "Starters", "crimson")
#             ax.set_title("")
#             st.pyplot(fig, use_container_width=True)

#         with col2:
#             fig, ax = plt.subplots()
#             plot_forecast_chart(ax, years, races, forecast_year, num_races, "Races", "Races", "darkblue")
#             ax.set_title("")
#             st.pyplot(fig, use_container_width=True)

#         with col3:
#             fig, ax = plt.subplots()
#             plot_forecast_chart(ax, years, meetings, forecast_year, num_meetings, "Meetings", "Meetings", "darkgreen")
#             ax.set_title("")
#             st.pyplot(fig, use_container_width=True)
