import streamlit as st

st.title("Site top")
st.write("teste dos sites locos do paranaue")
st.image('dog.jpg', caption='dog fofo')

st.header('botao')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')
