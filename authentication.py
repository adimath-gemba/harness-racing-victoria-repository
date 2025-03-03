import streamlit as st
import layout


# Logo URL
logo_url = "https://www.thetrots.com.au/hrv/includes/themes/MuraBootstrap3/images/logo.svg"


def authenticate_user():
    """Handles user authentication with a styled login page."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # Apply aesthetics (styles should also affect login page)
    layout.apply_aesthetics()

    if not st.session_state["authenticated"]:
        # Display the logo using Streamlit's image function (Ensures proper rendering)
        st.image(logo_url, width=250)

        # Title for the login page
        st.markdown("<h1 style='text-align: center;'>HRV Optimisation App</h1>", unsafe_allow_html=True)

        # Centered login form
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        login_container = st.container()
        with login_container:
            username = st.text_input("Username", key="username_input")
            password = st.text_input("Password", type="password", key="password_input")
            login_button = st.button("Login", key="login_button")

            if login_button:
                if username == "gemba_test" and password == "@gemba#1":
                    st.session_state["authenticated"] = True  # Save login state
                    st.rerun()  # Force refresh to remove login form
                else:
                    st.error("Invalid username or password.")

        st.markdown("</div>", unsafe_allow_html=True)  # Close the centered div

    return st.session_state["authenticated"]