# Cryptocurrency Volatility Prediction

## Project Overview
This project predicts cryptocurrency volatility using machine learning models trained on historical market data.

The dataset contains historical OHLC prices, trading volume, and market capitalization for multiple cryptocurrencies.

## Features
- Data preprocessing
- Feature engineering
- Exploratory Data Analysis
- Machine Learning model training
- Model evaluation
- Streamlit deployment

## Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Streamlit

## Machine Learning Model
Random Forest Regressor

## Evaluation Metrics
RMSE
MAE
R² Score

## Project Structure

data/
dataset.csv

notebooks/
volatility_prediction.ipynb

src/
preprocessing.py
feature_engineering.py
train_model.py

app/
streamlit_app.py

model/
volatility_model.pkl

reports/
EDA_Report.pdf
HLD_Document.pdf
LLD_Document.pdf
Final_Report.pdf

## Running the Project

Install dependencies

pip install -r requirements.txt

Run the Streamlit app

streamlit run streamlit_app.py
