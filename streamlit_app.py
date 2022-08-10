 
import streamlit
import pandas

streamlit.title("My parents' new healthy diner")
streamlit.header("Breakfast Favorites")
streamlit.text("🥣  Omega-3 & blueberry oatmeal")
streamlit.text("🥗 Kale, spinach, and rocket smoothie")
streamlit.text("🐔 Hard-boiled free-range egg")
streamlit.text("🥑🍞 Avocado toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
