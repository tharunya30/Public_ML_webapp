# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 15:07:42 2023

@author: Dell
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models

loaded_model_BS= pickle.load(open('C:\Users\Dell\OneDrive\Documents\ML webapp\trained_model_BC.sav','rb'))  #LOAD FUNCTION- to load the saved model

loaded_model_PD=pickle.load(open('C:C:\Users\Dell\OneDrive\Documents\ML webapp\trained_model_PD.sav','rb'))

#sidebar for navigation

with st.sidebar:
    selected = option_menu('DISEASE PREDICTION SYSTEM ', 
                           ['Breast Cancer prediction',
                            'Parkinson Disease Prediction']
                           icons=['house','heart','person'],
                           default_index=0)
    #BreastCancer prediction Page
    if(selected =='Breast Cancer prediction'):
        #page title
        st.title('Breast Cancer prediction using Ml')
        
        # getting the input data from the user
    col1, col2, col3 = st.columns(3)
        
    with col1:
        radius_mean = st.text_input('Mean radius of tumor')
        texture_mean = st.text_input('Mean value of texture')
        perimeter_mean = st.text_input('Mean perimeter of tumor')
        area_mean = st.text_input('Mean area of tumor')
        smoothness_mean = st.text_input('Mean smoothness of tumor')

    with col2:
        compactness_mean = st.text_input('Mean compactness of tumor')
        concavity_mean = st.text_input('Mean concavity of tumor')
        concave_points_mean = st.text_input('Mean concave points of tumor')
        symmetry_mean = st.text_input('Mean symmetry of tumor')
        fractal_dimension_mean = st.text_input('Mean fractal dimension of tumor')
        
    with col3:
        radius_se = st.text_input('Standard error of radius')
        texture_se = st.text_input('Standard error of texture')
        perimeter_se = st.text_input('Standard error of perimeter')
        area_se = st.text_input('Standard error of area')
        smoothness_se = st.text_input('Standard error of smoothness')
        compactness_se = st.text_input('Standard error of compactness')
        concavity_se = st.text_input('Standard error of concavity')
        concave_points_se = st.text_input('Standard error of concave points')
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        BS_prediction = loaded_model_BS.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave]])                          
        
        if(prediction[0]==1):
            return 'The Breast cancer is Malignant'

        else:
        return 'The Breast Cancer is Benign'
        
    st.success(breast_cancer_diagnosis)
    
    #parkinson prediction page
    if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
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
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
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
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        PD_prediction = loaded_model_PD.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
                           