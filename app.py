import pandas as pd
import streamlit as st
import plotly.express as px
import urllib.request
from PIL import Image

data=pd.read_csv('vehicles_us.csv')

st.title('Choose your car!')
st.subheader('Use this app to select the best car for your needs')

image_url = 'https://www.pencilkings.com/wp-content/uploads/2013/08/PK_AE_2000x1040_Car_Caricature_Lineart-1024x532.jpg'
urllib.request.urlretrieve(image_url, 'car_image.jpg')
img = Image.open('car_image.jpg')
st.image(img)

st.caption(':blue[Choose your parametres here]')

price_range = st.slider("What is your price range?",value=(1,375000))
actual_range=list(range(price_range[0],price_range[1]+1))

last_years = st.checkbox('Newer than 2010 only')

if last_years:
    filtered_data=data[data.price.isin[actual_range]]
    filtered_data=filtered_data[data.model_year >= 2010]
else:
    filtered_data=data[data.price.isin(actual_range)]
    
st.write('Here are your options with a split by price and year')

fig = px.scatter(filtered.data, x="price", y="model_year")
st.plotly_chart(fig)

st.write('Condition VS Year')
fig2 = px.histogram(filtered.data, x='model_year',color='condition')
st.write(fig2)

st.write('Here is the list of recomended cars')
st.dataframe(filtered.data.sample(20))