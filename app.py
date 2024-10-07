import warnings
import numpy as np
import streamlit as st
import pickle

warnings.filterwarnings('ignore')

def predicition(input_features: list|tuple):
    model = pickle.load(open("model.dat", 'rb'))
    ar_feat = np.asarray(input_features).reshape(1,-1)
    predict_ = model.predict(ar_feat)

    if predict_[0] == 0:
        return "The Preson is not Diabetic"
    return "Diabetic"

def main():
    st.title("Diabetes Predicition")
    #Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age

    pregnancies = st.text_input("No. of Pregnancies:")
    glucose = st.text_input("Glucose Level:")
    blood_pres = st.text_input("Blood Pressure Levels:")
    skin_thinkness = st.text_input("Skin Thinkness:")
    insulin = st.text_input("Insulin Levels:")
    bmi = st.text_input("BMI:")
    dia_ped = st.text_input("DiabetesPedigreeFunction:")
    age = st.text_input("Age:")

    result = ''
    if st.button("Diabetes Test Results"):
        result = predicition([pregnancies, glucose, blood_pres, skin_thinkness, insulin, bmi, dia_ped, age])

    st.success(result)

if __name__ == "__main__":
    main()