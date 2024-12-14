import streamlit as st
from PIL import Image
image_path = "images/image (14).jpg"
message = "Feliz cumpleaños amor, Te amo"

# Establecer un fondo romántico
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://example.com/tu_fondo_romantico.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Agregar título con estilo
st.markdown("<h1 style='text-align: center; color: white;'>Feliz Cumpleaños, Amor! ❤️</h1>", unsafe_allow_html=True)

# Mostrar imagen
image = Image.open(image_path)
st.image(image, caption="Una imagen especial para ti")

# Mostrar mensaje con estilo
st.markdown("<h2 style='text-align: center; color: white;'>Te amo más de lo que las palabras pueden expresar! 💖</h2>", unsafe_allow_html=True)