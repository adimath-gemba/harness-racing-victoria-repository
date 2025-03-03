import streamlit as st
import pandas as pd
import numpy as np
import io
# ----------------- Data Comparison Function -----------------


def show():
    st.title("Data Comparison")

    # Historical Data (Benchmark)
    historical_data = {
        "Year": np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024], dtype=int),
        "Avg Starters per Race": np.array([8.44, 8.44, 8.69, 8.80, 8.69, 9.02, 9.09]),
        "Races per Meeting": np.array([8.82, 8.77, 8.54, 9.16, 9.49, 9.42, 8.79]),
        "Predicted Starters": np.array([32515, 32433, 35003, 35217, 36175, 37557, 34133]),
        "Number of Races": np.array([3853, 3842, 4029, 4001, 4164, 4163, 3753]),
        "Number of Meetings": np.array([437, 438, 472, 437, 439, 442, 427]),
        "Season Weighting": np.array([0, 0, 0, 0, 0, 0, 0])
    }

    # Convert to DataFrame
    historical_df = pd.DataFrame(historical_data)
    historical_df["Year"] = historical_df["Year"].astype(str)  # Ensure Year is string

    # Check if there are saved results from home.py
    if "saved_results" not in st.session_state or not st.session_state["saved_results"]:
        st.warning("No saved predictions found. Submit values in the Race Scheduling Optimiser first.")
        saved_results_df = pd.DataFrame()  # Empty DataFrame for consistency
    else:
        saved_results_df = pd.DataFrame(st.session_state["saved_results"]).tail(10)

    # Display Historical Data Table with Selection
    st.subheader("Historical Data")
    selected_historical = st.data_editor(
        historical_df,
        hide_index=True,
        column_config={"Year": st.column_config.TextColumn("Year", width="medium")},
        use_container_width=True,
        num_rows="dynamic"
    )

    # Export Historical Data Selection
    if not selected_historical.empty:
        csv_buffer_hist = io.StringIO()
        selected_historical.to_csv(csv_buffer_hist, index=False)
        st.download_button(
            label="📥 Export Selected Historical Data",
            data=csv_buffer_hist.getvalue(),
            file_name="historical_data.csv",
            mime="text/csv"
        )

    # Display Saved Predictions Table with Selection
    st.subheader("Saved Predictions")
    selected_predictions = st.data_editor(
        saved_results_df,
        hide_index=True,
        column_config={"Year": st.column_config.TextColumn("Year", width="medium")},
        use_container_width=True,
        num_rows="dynamic"
    )

    # Export Saved Predictions Selection
    if not selected_predictions.empty:
        csv_buffer_saved = io.StringIO()
        selected_predictions.to_csv(csv_buffer_saved, index=False)
        st.download_button(
            label="📥 Export Selected Saved Predictions",
            data=csv_buffer_saved.getvalue(),
            file_name="saved_predictions.csv",
            mime="text/csv"
        )

    # Restart Button - Clears Data and Navigates to Home
    st.markdown("<br><br>", unsafe_allow_html=True)  # Add some space before the button
    if st.button("🔄 Clear Predictions & Go to Model"):
        st.session_state["saved_results"] = []  # Clear saved results
        st.session_state["page"] = "Model"  # Redirect to Home
        st.rerun()  # Refresh the page




