import streamlit as st
from PIL import Image


st.header("📸 Our Favorite Moments")
gallery_col1, gallery_col2, gallery_col3 = st.columns(3)

photos = [
    'images/image (1).jpg',
    'images/image (2).jpg',
    'images/image (3).jpg',
    'images/image (4).jpg',
    'images/image (5).jpg',
    'images/image (6).jpg',
    'images/image (7).jpg',
    'images/image (8).jpg',
    'images/image (9).jpg',
    'images/image (10).jpg',
    'images/image (11).jpg',
    'images/image (12).jpg',
    'images/image (13).jpg',
    'images/image (14).jpg',
    'images/image (15).jpg',
    'images/image (16).jpg',
    'images/image (17).jpg',
    'images/image (18).jpg',
]

for idx, photo_path in enumerate(photos):
    try:
        with [gallery_col1, gallery_col2, gallery_col3][idx % 3]:
            img = Image.open(photo_path)
            st.image(img)
    except FileNotFoundError:
        continue
