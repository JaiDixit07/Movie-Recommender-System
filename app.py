import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Title of the Streamlit app
st.title("Student Performance Prediction")

# Sidebar for user input features
st.sidebar.header("Input Features")

# Function to get user input
def get_user_input():
    gender = st.sidebar.selectbox("Gender", ["male", "female"])
    race_ethnicity = st.sidebar.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
    parental_level_of_education = st.sidebar.selectbox("Parental Level of Education", ["some high school", "high school", "associate's degree", "some college", "bachelor's degree", "master's degree"])
    lunch = st.sidebar.selectbox("Lunch", ["standard", "free/reduced"])
    test_preparation_course = st.sidebar.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.sidebar.slider("Reading Score", 0, 100, 50)
    writing_score = st.sidebar.slider("Writing Score", 0, 100, 50)

    # Create an instance of CustomData
    custom_data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score,
    )

    # Return data as DataFrame
    return custom_data.get_data_as_data_frame()

# Get user input data
input_df = get_user_input()

# Display user input features
st.subheader("User Input Features")
st.write(input_df)

# Load prediction pipeline
predict_pipeline = PredictPipeline()

# Make predictions
if st.button("Predict"):
    prediction = predict_pipeline.predict(input_df)
    st.subheader("Prediction")
    st.write(f"Predicted Math Score: {prediction[0]}")


