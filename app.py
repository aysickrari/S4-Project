import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

df=pd.read_csv(r'C:/Users/joshu/OneDrive/Documents/S4Project/S4-Project/vehicles_us.csv')

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

# Header for the Dashboard
st.title("Car Advertisement Data Analysis")
st.markdown("""
This dashboard provides visual insights into the car advertisement data. 
Below are some interactive histograms and scatterplots based on the dataset.
""")

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

# histogram of prices by manufacturer
st.subheader("Distribution of Car Prices By Manufacturer")
fig_manufacturer_hist = px.histogram(
    df,
    x='price',
    color='manufacturer',
    barmode='overlay',
    labels={'price': 'Price ($)', 'manufacturer': 'Manufacturer'},
    nbins=50,
    color_discrete_sequence=px.colors.qualitative.Set3
)
# Limit x-axis range to 100,000
fig_manufacturer_hist.update_layout(xaxis_range=[0, 100000])
st.plotly_chart(fig_manufacturer_hist)

# Histogram of Model Year
st.subheader("Distribution of Car Model Years By Manufacturer")
fig_year_hist = px.histogram(
    df, 
    x='model_year', 
    labels={'model_year': 'Model Year'},
    color='manufacturer',
    barmode='overlay',
    nbins=30,
    color_discrete_sequence=px.colors.qualitative.Set3
)
# Limit x-axis range from 1960 to 2024
fig_year_hist.update_layout(xaxis_range=[1960, 2020])
st.plotly_chart(fig_year_hist)

# Scatterplot: Price vs Odometer
st.subheader("Price vs Odometer")
fig_price_odometer = px.scatter(
    df, 
    x='odometer', 
    y='price',
    labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
    color='condition',
    hover_data=['model', 'fuel'],
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_price_odometer)

# Scatterplot: Price vs Model Year
st.subheader("Price vs Model Year")
fig_price_model_year = px.scatter(
    df, 
    x='model_year', 
    y='price', 
    labels={'model_year': 'Model Year', 'price': 'Price ($)'},
    color='fuel',
    hover_data=['model', 'transmission'],
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_price_model_year)

# histogram distribution of vehicle types by the manufacturer
st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)
 
# histogram of condition vs model year
st.header("Histogram of 'condition' vs 'model_year'")
st.write(px.histogram(df, x='model_year', color='condition'))

# compare price distibution between manufacturers
st.header('Compare price distribution between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())

# get user's inputs from a dropdown menu
manufacturer_1 = st.selectbox(
                              label='Select manufacturer 1', # title of the select box  
                              options=manufac_list, # options listed in the select box
                              index=manufac_list.index('chevrolet') # default pre-selected option
                              )
manufacturer_2 = st.selectbox(
                              label='Select manufacturer 2',  
                              options=manufac_list,
                              index=manufac_list.index('hyundai') 
                              )

# filter the dataframe
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm = 'percent'
else:
    histnorm = None
# create a plotly histogram figure
st.write(px.histogram(df_filtered, x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay'))