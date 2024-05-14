import streamlit as st

import base64

#adiciona imagem de fundo
@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('mont.png')

st.title("Site top")
st.write("teste dos sites locos do paranaue")
st.image('dog.jpg', caption='dog fofo')

st.header('botao')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')
