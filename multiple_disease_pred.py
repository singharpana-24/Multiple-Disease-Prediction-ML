# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 18:50:42 2025

@author: singh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open('C:/Users/singh/OneDrive/Desktop/ML2/diabetes_trained_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/singh/OneDrive/Desktop/ML2/heart_trained_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/singh/OneDrive/Desktop/ML2/parkinsons_trained_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction',
         'Heart Disease Prediction',
         'Parkinsons Disease Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# ---------------- Diabetes ----------------
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]])
            diab_diagnosis = 'The person is Diabetic' if diab_prediction[0] == 1 else 'The person is not Diabetic'
        except Exception:
            diab_diagnosis = '⚠️ Please enter valid numeric values for all fields.'

    st.success(diab_diagnosis)

# ---------------- Heart ----------------
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain Types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0=normal; 1=fixed defect; 2=reversable defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            heart_prediction = heart_model.predict([[
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang),
                float(oldpeak), float(slope), float(ca), float(thal)
            ]])
            heart_diagnosis = 'The person has Heart Disease' if heart_prediction[0] == 1 else 'The person does not have Heart Disease'
        except Exception:
            heart_diagnosis = '⚠️ Please enter valid numeric values for all fields.'

    st.success(heart_diagnosis)

# ---------------- Parkinsons ----------------
if selected == 'Parkinsons Disease Prediction':
    st.title('Parkinsons Disease Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Disease Test Result'):
        try:
            parkinsons_prediction = parkinsons_model.predict([[
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                float(Shimmer_APQ3), float(Shimmer_APQ5), float(APQ), float(DDA), float(NHR),
                float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2),
                float(D2), float(PPE)
            ]])
            parkinsons_diagnosis = 'The person has Parkinsons Disease' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinsons Disease'
        except Exception:
            parkinsons_diagnosis = '⚠️ Please enter valid numeric values for all fields.'

    st.success(parkinsons_diagnosis)


