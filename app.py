import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Custom CSS for styling
custom_css = """
<style>
body {
    background: rgba(0, 0, 0, 0.8) url("https://images.pexels.com/photos/730252/pexels-photo-730252.jpeg") no-repeat center center fixed;
    background-size: cover;
    color: #e0e0e0;
}
.main {
    padding: 2rem;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.7);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}
.stTextInput, .stNumberInput, .stSelectbox, .stSlider {
    margin-bottom: 1rem;
}
.stButton > button {
    margin-top: 1rem;
}
h1, h2 {
    text-align: center;
    color: #ffffff;
}
table {
    border-collapse: collapse;
    width: 100%;
}
th, td {
    border: 1px solid #ffffff;
    text-align: left;
    padding: 8px;
}
tr:nth-child(even) {
    background-color: #333333;
}
tr:nth-child(odd) {
    background-color: #444444;
}
th {
    background-color: #555555;
    color: #ffffff;
}
footer {
    text-align: center;
    margin-top: 2rem;
    color: #ffffff;
    font-size: 0.9rem;
}
</style>
"""

# Apply the custom CSS to the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Title of the Streamlit app
st.title("Student Performance Predictor")

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
st.write(input_df.style.set_table_attributes('class="table"'))

# Load prediction pipeline
predict_pipeline = PredictPipeline()

# Make predictions
if st.button("Predict"):
    prediction = predict_pipeline.predict(input_df)
    st.subheader("Prediction")
    st.write(f"Predicted Math Score: {prediction[0]}")

# Footer with author's name
st.markdown("<footer>Created by Jai Dixit</footer>", unsafe_allow_html=True)
