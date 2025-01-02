import streamlit as st
import pickle
import pandas as pd

st.title("Eathquake Predictor")
st.divider()
st.subheader("Regressor Models")
with st.container(border=True):
    col1,col2,col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.subheader("Linear Regressor")
            st.write("Enter data into all fields")
            with st.form("Linear Regression Form"):
                lat = st.number_input("Latitude",-90.00,90.00,25.00)
                long = st.number_input("Longitude",-180.00,180.00,25.00)
                depth = st.number_input("Depth(km)",0.00,700.00,10.00)
                stations = st.number_input("No of Stations",0,200,0)
                if st.form_submit_button("Predict"):
                    with open("./data/aiModel/linear_regressor.pkl", "rb") as file:
                        loaded_reg = pickle.load(file)
                        inp = [[lat,long,depth,stations]]
                        result = loaded_reg.predict(inp)
                        st.success(f"Prediction magnitude: {round(result[0],2)}")
    with col2:
        with st.container(border=True):
            st.subheader("SVM")
            st.write("Enter data into all fields")
            with st.form("SVM Form"):
                lat = st.number_input("Latitude",-90.00,90.00,25.00)
                long = st.number_input("Longitude",-180.00,180.00,25.00)
                depth = st.number_input("Depth(km)",0.00,700.00,10.00)
                stations = st.number_input("No of Stations",0,200,0)
                if st.form_submit_button("Predict"):
                    with open("./data/aiModel/svm_model.pkl", "rb") as file:
                        loaded_reg = pickle.load(file)
                        inp = [[lat,long,depth,stations]]
                        result = loaded_reg.predict(inp)
                        st.success(f"Prediction magnitude: {round(result[0],2)}")
    with col3:
        with st.container(border=True):
            st.subheader("Random Forest")
            st.write("Enter data into all fields")
            with st.form("Random Forest Form"):
                lat = st.number_input("Latitude",-90.00,90.00,25.00)
                long = st.number_input("Longitude",-180.00,180.00,25.00)
                depth = st.number_input("Depth(km)",0.00,700.00,10.00)
                stations = st.number_input("No of Stations",0,200,0)
                if st.form_submit_button("Predict"):
                    with open("./data/aiModel/random_forest_model.pkl", "rb") as file:
                        loaded_reg = pickle.load(file)
                        inp = [[lat,long,depth,stations]]
                        result = loaded_reg.predict(inp)
                        st.success(f"Prediction magnitude: {round(result[0],2)}")

legend_data = {
    "Magnitude Range": ["0 < Magnitude ≤ 5", "5 < Magnitude ≤ 6", "6 < Magnitude ≤ 7", "7 < Magnitude"],
    "Magnitude_Category": ["Minor", "Moderate", "Strong", "Major"],
    "Encoded Value (Magnitude_Category_Encoded)": [0, 1, 2, 3]
}
df = pd.DataFrame(legend_data)
st.subheader("Classifier Models")
with st.container(border=True):
    with st.container(border=True):
        st.subheader("Naive Bayes")
        st.write("Used for categorical classification")
        with st.form("Naive Bayes Form"):
            lat = st.number_input("Latitude",-2.00,2.00,0.00)
            long = st.number_input("Longitude",-2.00,2.00,0.00)
            stations = st.number_input("No of Stations",0,200,0)
            if st.form_submit_button("Predict"):
                    with open("./data/aiModel/naive_bayes_model.pkl", "rb") as file:
                        loaded_reg = pickle.load(file)
                        inp = [[lat,long,stations]]
                        result = loaded_reg.predict(inp)
                        st.success(f"Prediction magnitude: {round(result[0],2)}")
            st.markdown("#### Legend")
            st.dataframe(df)