import streamlit as st
import streamlit.components.v1 as components

st.subheader("🎥 Enter YouTube Video ID:")

# Create input field and store the value
video_id = st.text_input("Video Link ID", key="linkid")

# Only embed when input is not empty
if video_id:
    embed_url = f"https://www.youtube.com/embed/{video_id}?rel=0"

    # Embed using HTML
    components.html(f"""
        <iframe width="700" height="400"
        src="{embed_url}"
        frameborder="0"
        allowfullscreen>
        </iframe>
    """, height=400)
