import os

import pytube
import streamlit as st
from moviepy.editor import AudioFileClip


def download_mp3(url, key):
    try:
        youtube = pytube.YouTube(url)
        audio_stream = youtube.streams.filter(only_audio=True).first()

        # Clean the title so it's valid as a filename
        title = "".join(c if c.isalnum() else "_" for c in youtube.title)

        mp4_file = audio_stream.download(output_path="mp3", filename=title)
        mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"
        audio = AudioFileClip(mp4_file)
        audio.write_audiofile(mp3_file)
        os.remove(mp4_file)  # remove the original .mp4 file

        # Provide a download button for the MP3 file
        with open(mp3_file, "rb") as f:
            bytes = f.read()
            st.download_button(
                label="下載MP3",
                data=bytes,
                file_name=f"{title}.mp3",
                mime="audio/mpeg",
            )

        return True
    except Exception as e:
        st.error(f"Error downloading MP3: {str(e)}")
        return False


def add_text_area():
    if "num_text_areas" not in st.session_state:
        st.session_state.num_text_areas = 1
    else:
        st.session_state.num_text_areas += 1


def main():
    st.title("YouTube轉MP3下載器")

    st.button("新增", on_click=add_text_area)

    for i in range(st.session_state.get("num_text_areas", 1)):
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                url = st.text_area(f"Paste a YouTube URL here #{i+1}:", key=f"url_{i}")
            with col2:
                download_button_key = f"download_button_{i}"
                if st.button("轉換", key=download_button_key):
                    download_mp3(url, download_button_key)

            if url:
                st.video(url)


if __name__ == "__main__":
    main()
