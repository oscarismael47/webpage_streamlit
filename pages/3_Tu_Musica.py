import streamlit as st

def embed_youtube(video_id, width=340, height=190):
    """
    Inserta un video de YouTube con el ID de video dado
    """
    return f"""
        <iframe width="{width}" 
                height="{height}" 
                src="https://www.youtube.com/embed/{video_id}" 
                frameborder="0" 
                allowfullscreen>
        </iframe>
    """

st.title("🎵 Nuestras Canciones Especiales")
st.write("Una colección de canciones que cuentan nuestra historia...")

# Crear columnas para los videos
col1, col2 = st.columns(2)

# https://www.youtube.com/watch?v=2IrzQXPzXsI  canción con papas

# Diccionario de canciones con IDs de video y descripciones
songs = {
    "Nuestra Primera Canción": {
        "video_id": "5Xtc5ony-as",  # Reemplazar con el ID de video de YouTube real
        "description": "La canción con la que nos identificamos"
    },
    "Tu Canción Favorita": {
        "video_id": "3FYZcppWk5w",  # Reemplazar con el ID de video de YouTube real
        "description": "La canción que siempre te hace sonreír..."
    },
    "Nuestra Canción de Boda": {
        "video_id": "2IrzQXPzXsI",  # Reemplazar con el ID de video de YouTube real
        "description": "La melodía que bailamos con los papás"
    },
    "La canción que pienso cuando te veo": {
        "video_id": "odyrlzEutYg",  # Reemplazar con el ID de video de YouTube real
        "description": "Lo que significas para mí"
    }
}

# Mostrar videos en columnas alternas
for i, (title, song_info) in enumerate(songs.items()):
    with col1 if i % 2 == 0 else col2:
        st.subheader(title)
        st.markdown(embed_youtube(song_info["video_id"]), unsafe_allow_html=True)
        st.write(song_info["description"])
        st.markdown("---")

# Agregar una nota personal
st.markdown(""" 
### 💝 Por Qué Estas Canciones Son Especiales
Cada una de estas canciones lleva un pedazo de nuestra historia, un momento que hemos compartido, 
o un sentimiento que me recuerda a ti...
""")