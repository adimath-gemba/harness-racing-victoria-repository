import os
from PIL import Image
import streamlit as st

def show():
    st.title("Race Schedule Optimisation Logic")
    show_hrv_model_driver_tree()
    show_hrv_feature_selection()
    show_hrv_horse_population_analysis()

def show_hrv_model_driver_tree():
    image_path = "HRV_model_driver_tree.png"
    st.header("Model Driver Tree")
    st.markdown("The model driver tree is used to determine the optimal number of total starters using the features from the A and B indices. Once the total starters are determined, they are divided by 9.16 (customisable) to calculate the optimal number of races to be run. This number is then further divided by 9.24 (customisable) to determine the optimal number of meetings to be conducted.")
    display_image(image_path)

def show_hrv_feature_selection():
    image_path = "HRV_feature_selection.png"
    st.header("Model Feature Selection")
    st.markdown("The features on the left have been identified as those with the highest correlation to the number of starters. These features are utilised by the model to find the optimal number of starters")
    display_image(image_path)

def show_hrv_horse_population_analysis():
    image_path = "HRV_horse_population_analysis.png"
    st.header("Horse Population Forecasting")
    st.markdown("The number of eligible horses for 2025 and 2026 has been projected based on a historical analysis of age distribution trends")
    display_image(image_path)

def display_image(image_path):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=os.path.basename(image_path))
    else:
        st.warning(f"Image '{image_path}' not found.")
