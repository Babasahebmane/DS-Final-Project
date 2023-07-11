

import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load
import pickle
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler


logistic_r = LogisticRegression(solver='lbfgs')
scaler= load(open('scaler.sav', 'rb'))

loaded_model = load(open('kmeans.sav', 'rb'))


# creating a function for Prediction

def db_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    input_data_reshaped=scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'low spendings and low income '
    elif (prediction[0] == 1):
      return 'high spendings and high income '
    elif (prediction[0] == 2):
      return 'low spendings and average income '
    else :
      return 'average spendings and average income '
    
  
def main():
    
    
    # giving a title
    st.title('Customer Personality Analysis App')
    
    
    # getting the input data from the user
    
    
    number1 = st.number_input('Insert Income')
    number2 = st.number_input('Insert Kidhome')
    number3 = st.number_input('Insert Teenhome')
    number4 = st.number_input('Insert Age')
    number5 = st.number_input('Insert Spent')
    number6 = st.number_input('Insert Living_With')
    number7 = st.number_input('Insert Clusters')
    number8 = st.number_input('Insert NumWebVisitsMonth') 
    number9 = st.number_input('Insert Complain')
    number10 = st.number_input('Insert Response')
    number11 = st.number_input('Insert NumDealsPurchases')
    number12 = st.number_input('Insert Is_Parent')
    number13 = st.number_input('Insert Recency')
    number14 = st.number_input('Insert NumWebPurchases')
    number15 = st.number_input('Insert Education')
    number16 = st.number_input('Insert NumCatalogPurchases')
    number17 = st.number_input('Insert NumStorePurchases')
    number18 = st.number_input('Insert Family_Size')
    number19 = st.number_input('Insert Children')
    
    
    
    
    
    
#     # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Customer Personality Test Result'):
        diagnosis = db_prediction([number1, number2, number3,number4,number5,number6,number7,number8,number9,number10,
                                  number11,number12,number13,number14,number15,number16,number17,number18,number19])
        
        
    st.success(diagnosis)
    
   
    
if __name__ == '__main__':
    main()
    

        
