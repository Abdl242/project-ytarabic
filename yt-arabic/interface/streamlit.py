import streamlit as st
from functions import *
# Function to summarize the video (replace this with your actual summarization function)
def summarize_video(url, language="french"):
    # Placeholder for video summarization logic
    # For demonstration purposes, we will return a mock summary
    return f"Summary of the video at {url}: This is a mock summary."

# Set up the Streamlit app layout
st.title("YouTube Video Summarizer")

# Create a form for user input
with st.form(key='my_form'):
    youtube_url = st.text_input("Enter YouTube Video URL:")

    language = st.radio("Select summary language:", ("English", "French"))


    submit_button = st.form_submit_button(label='Summarize')

# Process the input when the user submits the form
if submit_button:
    if youtube_url:
        # Call your summarization function
        print(f"Processing video {youtube_url}")
        video_title,transcript_test = youtube_main(youtube_url)
        summary = application_gpt_2(transcript_test,client_gpt,language)

        # Display the summary on the page
        st.subheader("Video Summary:")
        st.write(summary)
    else:
        st.warning("Please enter a valid YouTube URL.")
