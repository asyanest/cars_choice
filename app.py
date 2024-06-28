import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

data = pd.read_csv('vehicles_us.csv')

data['price'] = data['price'].fillna(data['price'].mean())
data['model_year'] = data['model_year'].fillna(data['model_year'].mode()[0])
data['condition'] = data['condition'].fillna('unknown')  # or use another appropriate fill method
data['odometer'] = data['odometer'].fillna(data['odometer'].median())

cleaned_data = data.drop_duplicates().reset_index(drop=True)

cleaned_data['price'] = cleaned_data['price'].astype(int)

st.title('Choose your car!')
st.subheader('Use this app to select the best car for your needs')

img = Image.open("car_image.jpg")
st.image(img)

st.caption('Choose your parameters here')

price_range = st.slider("What is your price range?", value=(1, 375000))
actual_range = list(range(price_range[0], price_range[1] + 1))

last_years = st.checkbox('Newer than 2010 only')

if last_years:
    filtered_data = cleaned_data[cleaned_data.price.isin(actual_range) & (cleaned_data.model_year >= 2010)]
else:
    filtered_data = cleaned_data[cleaned_data.price.isin(actual_range)]

st.write('Here are your options with a split by price and year')
fig = px.scatter(filtered_data, x="price", y="model_year")
st.plotly_chart(fig)

st.write('Condition VS Year')
fig2 = px.histogram(filtered_data, x='model_year', color='condition')
st.write(fig2)

st.write('Here is the list of recommended cars')
st.dataframe(filtered_data.sample(20))
