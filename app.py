import pandas as pd
import streamlit as st
import plotly.express as px

data=pd.read_csv('vehicles_us.csv')

cleaned_data = data.dropna()
cleaned_data = cleaned_data.drop_duplicates()
cleaned_data = cleaned_data.reset_index(drop=True)

cleaned_data['price'] = cleaned_data['price'].astype(int)
cleaned_data['model_year'] = cleaned_data['model_year'].astype(int)

st.title('Choose your car!')
st.subheader('Use this app to select the best car for your needs')

from PIL import Image
img = Image.open("car_image.jpg")
st.image(img)

st.caption('Choose your parameteres here')

price_range = st.slider("What is your price range?",value=(1,375000))
actual_range=list(range(price_range[0],price_range[1]+1))

last_years = st.checkbox('Newer than 2010 only')

if last_years:
    filtered_data=cleaned_data[cleaned_data.price.isin(actual_range) & (cleaned_data.model_year >= 2010)]
else:
    filtered_data=cleaned_data[cleaned_data.price.isin(actual_range)]
    
st.write('Here are your options with a split by price and year')
fig = px.scatter(filtered_data, x="price", y="model_year")
st.plotly_chart(fig)

st.write('Condition VS Year')
fig2 = px.histogram(filtered_data, x='model_year',color='condition')
st.write(fig2)

st.write('Here is the list of recomended cars')
st.dataframe(filtered_data.sample(20))