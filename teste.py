import streamlit as st

st.title("Site muito foda")
st.write("teste dos sites locos do paranaue")
st.image('dog.jpg', caption='dog fofo')

st.header('st.button')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')
