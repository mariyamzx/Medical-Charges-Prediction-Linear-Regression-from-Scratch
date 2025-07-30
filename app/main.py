import streamlit as st
import pandas as pd
import pickle
from LinearReg import LinearRegression  # important for unpickling!

# Configure the Streamlit page
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load the saved pipeline
@st.cache_data
def load_pipeline():
    with open("insurance_pipeline.pkl", "rb") as file:
        pipeline = pickle.load(file)
    return pipeline

pipeline = load_pipeline()

# Sidebar inputs
def add_sidebar():
    st.sidebar.header("Client Information")
    
    age = st.sidebar.slider("Age", 18, 100, 30)
    gender = st.sidebar.selectbox("Gender", ["male", "female"])
    bmi = st.sidebar.slider("BMI", 10.0, 50.0, 25.0)
    children = st.sidebar.slider("Number of Children", 0, 5, 1)
    smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
    region = st.sidebar.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

    user_data = {
        "age": age,
        "sex": gender,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }

    return pd.DataFrame([user_data])

# Main content
def main():
    with st.container():
        st.title("💰 Medical Insurance Cost Predictor")
        st.write(
            "This app predicts **medical insurance charges** based on a person's "
            "age, BMI, smoking habits, and more. It's built using a custom Linear Regression model "
            "trained on real-world data. Just input your details on the left!"
        )

    input_df = add_sidebar()

    st.subheader("Client Profile")
    st.write(input_df)

    if st.button("Predict Insurance Cost"):
        prediction = pipeline.predict(input_df)[0]
        st.success(f"💵 Estimated Insurance Cost: ${prediction:,.2f}")

if __name__ == "__main__":
    main()