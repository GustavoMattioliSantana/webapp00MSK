import streamlit as st

page_bg_img = '''
<style>
body {
background-image: src("mont.png");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Site top")
st.write("teste dos sites locos do paranaue")
st.image('dog.jpg', caption='dog fofo')

st.header('botao')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')
