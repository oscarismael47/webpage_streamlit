import streamlit as st
from PIL import Image

def main():
    st.title("Image Display Demo")
    
    # You can display an image from a file
    try:
        image = Image.open('images/image - copia (2).png')  # Replace with your image path
        st.image(image, caption='Your Image Caption', use_column_width=True)
    except FileNotFoundError:
        st.error("Please make sure the image file exists at the specified path")

    # Alternatively, you can also display an image from URL
    # st.image('https://example.com/image.jpg', caption='Image from URL')

if __name__ == '__main__':
    main()
