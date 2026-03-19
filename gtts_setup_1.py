import streamlit as st
from gtts import gTTS

st.title("Bengali TTS - Prototype")
text = st.text_area("Type Bengali text here")

if st.button("Generate Audio"):
    tts = gTTS(text=text, lang='bn')
    tts.save("output.mp3")
    st.audio("output.mp3")
    st.download_button("Download", open("output.mp3", "rb"), "output.mp3")
