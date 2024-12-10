import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv(r'C:/Users/joshu/OneDrive/Documents/S4Project/S4-Project/vehicles_us.csv')

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

# histogram distribution of vehicle types by the manufacturer
st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)
 
# histogram of condition vs model year
st.header("Histogram of 'condition' vs 'model_year'")
st.write(px.histogram(df, x='model_year', color='condition'))