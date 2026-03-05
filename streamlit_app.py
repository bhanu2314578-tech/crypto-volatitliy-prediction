# import streamlit as st
# import pickle
# import numpy as np

# model = pickle.load(open("volatility_model.pkl","rb"))

# st.title("Cryptocurrency Volatility Predictor")

# open_price = st.number_input("Open Price")
# high_price = st.number_input("High Price")
# low_price = st.number_input("Low Price")
# close_price = st.number_input("Close Price")
# volume = st.number_input("Volume")
# market_cap = st.number_input("Market Cap")

# if st.button("Predict Volatility"):
    
#     data = np.array([[open_price, high_price, low_price, close_price, volume, market_cap]])
    
#     prediction = model.predict(data)
    
#     st.success(f"Predicted Volatility: {prediction[0]}")




import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("volatility_model.pkl","rb"))

st.title("Cryptocurrency Volatility Predictor")

# Input fields for all 10 features required by the model
open_price = st.number_input("Open Price")
close_price = st.number_input("Close Price")
low_price = st.number_input("Low Price")
high_price = st.number_input("High Price")
ma_7 = st.number_input("7-day Moving Average")
ma_21 = st.number_input("21-day Moving Average")
liquidity_ratio = st.number_input("Liquidity Ratio")
market_cap = st.number_input("Market Cap")
upper_band = st.number_input("Upper Bollinger Band")
lower_band = st.number_input("Lower Bollinger Band")

if st.button("Predict Volatility"):
    
    # Ensure the order of features matches the training data
    data = np.array([[
        open_price, close_price, low_price, high_price,
        ma_7, ma_21, liquidity_ratio, market_cap,
        upper_band, lower_band
    ]])
    
    prediction = model.predict(data)
    
    st.success(f"Predicted Volatility: {prediction[0]}")