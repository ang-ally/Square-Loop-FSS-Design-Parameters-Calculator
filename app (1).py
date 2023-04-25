# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 21:18:02 2023

@author: Angelyn Sweety Isaac
"""

import pickle
import pandas as pd

import streamlit as st

model_d = pickle.load(open('d_prediction.sav','rb'))

st.title("Synthesis of Square Loop FSS using ML")

st.header('For FR-4 Substrate')

st.caption('The Range for Resonant Frequency: 0 < fr < 5') 
st.caption('The Range for Lower-cutoff Frequency: 0 < fl < 5')
st.caption('The Range for Higher-cutoff Frequency: 0 < fh < 5')

h = st.selectbox('Height of the Substrate in mm (h)',(0.8,1.6,3.2))
fr = st.text_input("Resonant Frequency in GHz (fr)")
fl = st.text_input("Lower-cutoff Frequency in GHz (fl)")
fh = st.text_input("Higher-cutoff Frequency in GHz (fh)")
bw = st.text_input("Bandwidth in GHz (bw)")
fbw = st.text_input("Fractional bandwidth (fbw)")
g = st.selectbox('Inter-gap Element spacing in mm (g)',(0.25,0.375,0.5))


# code for Prediction
msg1 = list()
msg1.append("Track-length (d) is")


# creating a button for Prediction    
if st.button("Predict"):
    d_pred = model_d.predict([[h,fr,fl,fh,bw,fbw,g]])
    #st.success('Track-length (d) is')
    msg1.append(d_pred)
    st.success(msg1) 
    
  

                 
      






