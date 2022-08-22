 
import streamlit
import snowflake.connector
import pandas
import requests
from urllib.error import URLError

def get_clothes_list():
 with my_cnx.cursor() as my_cur:
   my_cur.execute("select color_or_style from catalog_for_website")
   clothes = [row[0] for row in my_cur.fetchall()]
   return clothes

def get_clothes_details(clothes_choice):
 with my_cnx.cursor() as my_cur:
  my_cur.execute("select direct_url from catalog_for website where color_or_style = '"+clothes_choice+"')")
  streamlit.write(my_cur.fetchall())

streamlit.title("Zena's Amazing Athleisure Catalog")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
clothes_choice = streamlit.selectbox('Pick a sweatsuit color or style', get_clothes_list())

streamlit.stop()
                 
                 
                 
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# Display the table on the page.

streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
  streamlit.error('Please select a fruit to get information.')
 else:
  streamlit.write('The user entered ', fruit_choice)
  fruityvice_normalized = get_fruityvice_data(fruit_choice)
  streamlit.dataframe(fruityvice_normalized)

except URLError as e:
 streamlit.error()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
streamlit.header("View our fruit list - Add your favorites!")
if streamlit.button('Get fruit list'):
 my_data_rows = get_fruit_load_list()
 streamlit.dataframe(my_data_rows)

try:
 add_my_fruit = streamlit.text_input('What fruit would you like to add?')
 if streamlit.button('Add fruit to list'):
  if not add_my_fruit:
   streamlit.error('Enter a fruit to add to list')
  else:
   function_message = insert_fruit_into_load_list(add_my_fruit)
   streamlit.write(function_message)

except URLError as e:
 streamlit.error()

my_cnx.close()
