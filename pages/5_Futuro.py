import streamlit as st
from PIL import Image
st.header("🌟 Our Future Together")
st.write("""
Share your dreams and plans for the future...
""")

st.subheader("Our first baby")

img = Image.open("images/bebe.jpg")
st.image(img)