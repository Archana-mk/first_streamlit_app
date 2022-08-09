import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit advice!')
try:
  
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information about.')
#streamlit.write('The user entered ', fruit_choice)
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # normalizing json data 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # converting normalized data into dataframe
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()
    







my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("fruit_load_list contains:")
streamlit.dataframe(my_data_rows)

#allow end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', add_my_fruit)
