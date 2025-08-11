import streamlit as st



st.title("Subtitles :blue[Generator] :tv:")


#Upload file
uploaded_file = st.file_uploader(":red[Upload a video file]", type=["mp4", "mov", "avi"])
if uploaded_file is not None:
#read file as bytes:
    video_bytes = uploaded_file.read()
    st.video(video_bytes)




    


