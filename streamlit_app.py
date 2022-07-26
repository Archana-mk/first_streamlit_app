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

#create the repeatable code block(function):
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit advice!')
try:
  
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('please select a fruit to get information about.')
#streamlit.write('The user entered ', fruit_choice)
  else:
    back_from_function= get_fruityvice_data(fruit_choice)
    # converting normalized data into dataframe
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
    
streamlit.header("fruit_load_list contains:")
#snowflake related functon
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

#add a button to load the fruit
if streamlit.button('get fruit load list'):
  
  my_data_rows=get_fruit_load_list()
  streamlit.dataframe(my_data_rows)


#allow end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "Thanks for adding" + new_fruit
  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function=insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
