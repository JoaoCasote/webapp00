import streamlit as st

st.title("A vida não é sobre quão duro você é capaz de bater, mas sobre quão duro você é capaz de apanhar e continuar indo em frente.")
st.write("Rocky Balboa")
from PIL import Image

# Título da página
st.title('Exemplo de Carregamento de Imagem')

# Carregar a imagem
image = Image.open('example_image.jpg')

# Exibir a imagem
st.image(image, caption='Imagem de exemplo', use_column_width=True)
