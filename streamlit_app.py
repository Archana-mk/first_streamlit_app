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

streamlit.dataframe(my_fruit_list)
