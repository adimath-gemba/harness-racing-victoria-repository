import streamlit as st
 
# ----------------- Sidebar Customization -----------------
 
def customize_sidebar(logo_url):
    """
    Customizes the sidebar for navigation.
    """
    with st.sidebar:
        st.markdown(
            f"""
<div style="display: flex; justify-content: center; align-items: center;">
<img class='sidebar-logo' src='{logo_url}' alt='Logo' style="width: 100%; max-width: 250px;">
</div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<div class='sidebar-title'>HRV Race Schedule Optimisation</div>", unsafe_allow_html=True)
 
        if st.button("Model", key="home_button"):
            st.session_state["page"] = "Model"
        if st.button("Logic", key="logic_button"):
            st.session_state["page"] = "Logic"
        if st.button("Data Comparison", key="data_comparison_button"):
            st.session_state["page"] = "Data Comparison"
        # if st.button("Forecast", key="forecast_button"):
        #     st.session_state["page"] = "Forecast"
 
        st.markdown("<div class='powered-by'>Powered by Gemba</div>", unsafe_allow_html=True)
 
# ----------------- CSS Markdown Function -----------------
 
 
def apply_aesthetics():
    """
    Applies custom CSS styles for the sidebar and page aesthetics.
    """
    st.markdown("""
<style>
        .css-1d391kg {
            background-color: #ffffff !important;
            color: #ffffff !important;
        }
        [data-testid="stSidebar"] {
            background-color: #0373DA !important;
            color: #ffffff !important;
            padding-top: 10px !important;
        }
        .sidebar-title {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #A7C7E7 !important;
            margin: 10px auto !important;
            text-align: center !important;
        }
        .stButton>button {
            background-color: #005bb5 !important;
            color: #ffffff !important;
            border-radius: 5px !important;
            width: 90% !important;
            height: 40px !important;
            font-size: 16px !important;
            margin: 0px auto !important;
            display: block !important;
            border: none !important;
            transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out !important;
        }
        .stButton>button:hover {
            background-color: #00A19A !important;
            color: #ffffff !important;
        }
        .powered-by {
            text-align: center !important;
            font-size: 12px !important;
            color: #ffffff !important;
            margin-top: 20px !important;
        }
        div.block-container {
            padding-top: 80px !important;
        }
        /* Default color (grey) */
        button[data-testid="stNumberInputStepDown"],
        button[data-testid="stNumberInputStepUp"] {
            background-color: #F0F2F6 !important;
            color: black !important;
            border-radius: 5px !important;
            transition: background-color 0.2s ease-in-out;
        }
        /* Change color to green when clicked */
        button[data-testid="stNumberInputStepDown"]:active,
        button[data-testid="stNumberInputStepUp"]:active,
        button[data-testid="stNumberInputStepDown"]:hover,
        button[data-testid="stNumberInputStepUp"]:hover {
            background-color: #00A19A !important;
            color: white !important;
        }
        /* Reset color back to grey when mouse leaves */
        button[data-testid="stNumberInputStepDown"]:not(:active),
        button[data-testid="stNumberInputStepUp"]:not(:active) {
            background-color: #F0F2F6 !important;
            color: black !important;
        }
        /* Adjust the Streamlit top header bar */
        header[data-testid="stHeader"] {
            padding-top: 10px !important;
        }
        /* Ensure title container expands fully */
        .stHeading[data-testid="stHeading"] {
            width: 100% !important;
            max-width: none !important;
        }
        /* Fix the title width */
        .st-emotion-cache-1104ytp {
            width: 100% !important;
            max-width: 100% !important;
            text-align: left !important;
        }
        /* Fix the header and its surrounding elements */
        .st-emotion-cache-18netey {
            width: 100% !important;
            max-width: 100% !important;
        }
        /* Ensure title is visible */
        h1, h2, h3 {
            margin-top: 0px !important;
            padding-top: 20px !important;
        }
        /* Adjust body layout to prevent unintended shifts */
        body {
            margin: 0px !important;
            padding: 0px !important;
        }
        /* Hide the link and icon in the header */
        .st-emotion-cache-gi0tri {
            display: none !important;
        }
</style>
        """,
                unsafe_allow_html=True)