import streamlit as st
import layout

# Logo URL
logo_url = "https://www.thetrots.com.au/hrv/includes/themes/MuraBootstrap3/images/logo.svg"

def authenticate_user():
    """Handles user authentication with a properly positioned login form."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # Apply aesthetics (reuse existing sidebar styling)
    layout.apply_aesthetics()

    if not st.session_state["authenticated"]:
        # Custom CSS to remove excessive white space and fine-tune positioning
        st.markdown(
            """
            <style>
                .login-wrapper {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: flex-start;
                    position: relative;
                    top: -50px; /* Moves everything up */
                }
                .login-container {
                    width: 320px; /* Restrict width */
                    padding: 20px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }
                .logo-container {
                    background-color: #0373DA; /* Blue background for logo */
                    padding: 15px;
                    border-radius: 10px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin-bottom: 10px;
                }
                .logo-container img {
                    width: 200px;
                }
                .stTextInput > label {
                    text-align: center !important;
                    display: block;
                    width: 100%;
                    font-weight: bold;
                }
                .stTextInput > div {
                    width: 250px !important;
                    margin: auto;
                }
                .stButton>button {
                    width: 250px !important; /* Reduce button width */
                    background-color: #005bb5 !important;
                    color: #ffffff !important;
                    border-radius: 5px !important;
                    text-align: center;
                }
                .stButton>button:hover {
                    background-color: #00A19A !important;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Wrap everything in a div that positions it correctly
        st.markdown("<div class='login-wrapper'>", unsafe_allow_html=True)

        # Display the logo at the top
        st.markdown(
            f"""
            <div class="logo-container">
                <img src="{logo_url}">
            </div>
            """,
            unsafe_allow_html=True
        )

        # Title
        st.markdown("<h1 style='text-align: center;'>HRV Race Schedule Optimisation</h1>", unsafe_allow_html=True)

        # Login Form (Higher on Page)
        # st.markdown("<div class='login-container'>", unsafe_allow_html=True)

        # Centered Input Fields
        username = st.text_input("Username", key="username_input")
        password = st.text_input("Password", type="password", key="password_input")
        login_button = st.button("Login", key="login_button")

        if login_button:
            if username == "hrv_test" and password == "@gemba#1":
                st.session_state["authenticated"] = True
                st.rerun()  # Refresh UI after login
            else:
                st.error("Invalid username or password.")

        # Close the container
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state["authenticated"]
