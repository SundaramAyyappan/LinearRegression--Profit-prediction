# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 15:54:46 2023

@author: Sundar
"""

import numpy as np
import pickle
import pandas as pd

import streamlit as st 


from PIL import Image

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Profit_prediction(RnD_Spend, Administration, Marketing_Spend):
    
    prediction=classifier.predict([[RnD_Spend, Administration, Marketing_Spend]])
    print(prediction)
    
    return prediction



def main():
    
    st.title('Profit prediction Web App')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Profit Prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    
    RnD_Spend = st.number_input('Insert RnD_Spend')
    Administration = st.number_input('Insert Administration')
    Marketing_Spend = st.number_input('Insert Marketing_Spend')
    
    
    #code for prediction (the result of prediction will return in this empty string)
    Profit = ''
    
    #creating button for prediction
    if st.button('Profit Result'):
        Profit = Profit_prediction(RnD_Spend, Administration, Marketing_Spend)
    
    
    st.success('The Profit will be {} '.format(Profit))
    
    
    
if __name__ == '__main__':
    main()

