# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:51:37 2022

@author: Tilshini
"""

    
import streamlit as st

import joblib

def main():
   
    
    
   html_temp = """
   <div style="backgroun-color:lightblue;padding:16px">
   <h2 style="color:black";text-align:center>Heart Failure Prediction Using ML</h2>
   </div>

   """
   
   st.markdown(html_temp,unsafe_allow_html=True)
   
 
 
   
    
    # load the model
   model = joblib.load('model_joblib')
    
   p1 = st.slider("Enter Your Age",18,100)
    
   s1=st.selectbox("Sex",("Male","Female"))
   
   if s1=="Male":
        p2=1
   else:
        p2=0
    
   p3 =st.number_input("Enter Your Resting blood preasure")
   p4 =st.number_input("Enter Your Cholesterol level")
   
     
    
   s2=st.selectbox("RestingECG",("Normal","ST"))
   if s2=="Yes":
        p5=1
   else:
        p5=0
   p6 =st.number_input("Enter Your MaxHR")
        
   s3=st.selectbox("ExerciseAngina",("Yes","No"))
   if s2=="Yes":
        p7=1
   else:
        p7=0
    
   s4=st.selectbox("EFastingBS",("Yes","No"))
   if s2=="Yes":
         p8=1
   else:
         p8=0
         
    
   if st.button('Predict'):
       prediction = model.predict([[p1,p2,p3,p4,p5,p6,p7,p8]])
       st.balloons()       
       st.success('HeartDisease of New Customer is {} '.format(round(prediction[0],2)))

   
if __name__ == '__main__':

    main()