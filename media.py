import streamlit as st

st.image('https://cdn.analyticsvidhya.com/wp-content/uploads/2021/06/39595st.jpeg', caption='Ini adalah Streamlite')

audio_url = 'http://www.nch.com.au/acm/8k16bitpcm.wav'
st.audio(audio_url, format='audio/mp3')

video_url = 'https://youtu.be/-EfcNj6xFPw?si=HfG4vcDS4-gAHcOW'
st.video(video_url, format='video/mp4')

st.write("Dibuat oleh Muhammad Hanif Annafi ( 21537141009 )")