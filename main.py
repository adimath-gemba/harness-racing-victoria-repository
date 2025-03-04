import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from streamlit_option_menu import option_menu

import model
import logic
import data_comparison
import forecast
import layout
import authentication


st.set_page_config(page_title="HRV OPTIMISATION APP", layout="wide")

# Logo URL
logo_url = "https://www.thetrots.com.au/hrv/includes/themes/MuraBootstrap3/images/logo.svg"

# ----------------- Main Function -----------------
def main():
    if authentication.authenticate_user():  # Ensure authentication before loading the app
        layout.apply_aesthetics()

        # Sidebar - Show content only after login
        with st.sidebar:
            layout.customize_sidebar(logo_url)

        if "page" not in st.session_state:
            st.session_state["page"] = "Model"

        # Route to the selected page
        if st.session_state["page"] == "Model":
            model.show()
        elif st.session_state["page"] == "Logic":
            logic.show()
        elif st.session_state["page"] == "Data Comparison":
            data_comparison.show()
        # elif st.session_state["page"] == "Forecast":
        #     forecast.show()

if __name__ == "__main__":
    main()
