import os

import pytube
import streamlit as st
from moviepy.editor import AudioFileClip


def download_mp3(url):
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
                label=f"Download {title}.mp3",
                data=bytes,
                file_name=f"{title}.mp3",
                mime="audio/mpeg",
            )

        return True
    except Exception as e:
        st.error(f"Error downloading MP3: {str(e)}")
        return False


def main():
    st.title("YouTube to MP3 Downloader")

    urls = st.text_area("Enter YouTube URLs (one URL per line):")
    urls = urls.strip().split("\n")

    if st.button("Download MP3"):
        for url in urls:
            if download_mp3(url):
                st.success(f"MP3 downloaded successfully for URL: {url}")


if __name__ == "__main__":
    main()
