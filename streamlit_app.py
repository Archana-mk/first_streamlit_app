import streamlit
import pandas



streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & blueberry oatmeal')
streamlit.text('kale, spinach & rocket smoothie')
streamlit.text('hard-boiled free-ranged egg')

streamlit.header('build your own fruit smoothie')
# streamlit.text('apple milkshake')
# streamlit.text('U+1F34C banana milkshake')
# streamlit.text('orange juice')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#picker works but with numbers. lets give options to pick fruits by name
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
streamlit.header('Fruityvice Fruit advice!')


#new section to display fruityvice api response

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
