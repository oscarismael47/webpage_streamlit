import streamlit as st
from PIL import Image
st.header("🌟 Nuestro Futuro Juntos")


st.subheader("Nuestro primer bebé")

gallery_col1, gallery_col2 = st.columns(2)

photos = [
    'images/bebe (1).jpeg',
    'images/bebe (2).jpeg',
    'images/bebe (3).jpeg',
    'images/bebe (4).jpeg'
]

for idx, photo_path in enumerate(photos):
    try:
        with [gallery_col1, gallery_col2][idx % 2]:
            img = Image.open(photo_path)
            st.image(img)
    except FileNotFoundError:
        continue


video1 =  "videos/video1.mp4"
video2 =  "videos/video2.mp4"
video_col1, video_col2 = st.columns(2)

with video_col1:
    st.video(video1)

with video_col2:
    st.video(video2)