import streamlit as st

def embed_youtube(video_id, width=340, height=190):
    """
    Embeds a YouTube video with the given video ID
    """
    return f"""
        <iframe width="{width}" 
                height="{height}" 
                src="https://www.youtube.com/embed/{video_id}" 
                frameborder="0" 
                allowfullscreen>
        </iframe>
    """

st.title("🎵 Our Special Songs")
st.write("A collection of songs that tell our story...")

# Create columns for the videos
col1, col2 = st.columns(2)

# https://www.youtube.com/watch?v=2IrzQXPzXsI  cancion con papas



# Dictionary of songs with video IDs and descriptions
songs = {
    "Our First Song": {
        "video_id": "5Xtc5ony-as",  # Replace with actual YouTube video ID
        "description": "The song con la que nos identificamos"
    },
    "Your Favorite Song": {
        "video_id": "3FYZcppWk5w",  # Replace with actual YouTube video ID
        "description": "The song that always makes you smile..."
    },
    "Our Wedding Song": {
        "video_id": "YOUR_VIDEO_ID_3",  # Replace with actual YouTube video ID
        "description": "The melody that sealed our love..."
    },
    "La cancion que pienso cuando te veo": {
        "video_id": "odyrlzEutYg",  # Replace with actual YouTube video ID
        "description": "Lo que significas para mi"
    }
}

# Display videos in alternating columns
for i, (title, song_info) in enumerate(songs.items()):
    with col1 if i % 2 == 0 else col2:
        st.subheader(title)
        st.markdown(embed_youtube(song_info["video_id"]), unsafe_allow_html=True)
        st.write(song_info["description"])
        st.markdown("---")

# Add a personal note
st.markdown("""
### 💝 Why These Songs Are Special
Each of these songs carries a piece of our story, a moment we've shared, 
or a feeling that reminds me of you...
""")