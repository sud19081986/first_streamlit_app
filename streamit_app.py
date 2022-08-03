import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('2 Boiled Eggs ')
streamlit.text('1 Glass Milk')
streamlit.text('🥑 Fruits')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index)
streamlit.dataframe(my_fruit_list)
