import streamlit as st

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
<h1> Teste do texto em html</h1>
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Site top")
st.write("teste dos sites locos do paranaue")
st.image('dog.jpg', caption='dog fofo')

st.header('st.button')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')
