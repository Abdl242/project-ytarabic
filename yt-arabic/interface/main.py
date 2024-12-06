import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import warnings
warnings.filterwarnings("ignore")
import IPython.display as ipd
from transformers import pipeline
from pydub import AudioSegment
import json
from google.cloud import translate_v2 as translate

from yt_dlp import YoutubeDL

#from moviepy.editor import VideoFileClip
from vosk import Model, KaldiRecognizer
import openai

import nltk
import re
import textwrap
from nltk.tokenize import sent_tokenize
client_gpt = openai.OpenAI()
# تحميل ملفات NLTK المطلوبة
nltk.download('punkt')

import re
#from textblob import TextBlob

from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from gpt import ask_chatgpt,application_gpt
from txt2md import parse_to_markdown




vosk_models = {"ar":"vosk-model-ar-0.22-linto-1.1.0",
               "en":"vosk-model-en-us-0.22",
               "fr":"vosk-model-fr-0.22"
    }

def voice_recognition(filename,language):
    FRAME_RATE = 16000
    CHANNELS=1
    model = Model(model_name=vosk_models[language])
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    mp3 = AudioSegment.from_mp3("test.mp3")
    mp3 = mp3.set_channels(CHANNELS)
    mp3 = mp3.set_frame_rate(FRAME_RATE)

    step = 45000
    transcript = ""
    for i in range(0, len(mp3), step):
        print(f"Progress: {i / len(mp3):.2%}")
        segment = mp3[i:i+step]
        rec.AcceptWaveform(segment.raw_data)
        result = rec.Result()
        text = json.loads(result)["text"]
        transcript += text

    return transcript



# youtube_url = 'https://www.youtube.com/watch?v=6Yc37c5suaw&t=271s'

# # Define the output file name
# audio_output = 'chaar_jahily'

# # Download the audio directly using yt-dlp
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'outtmpl': audio_output,
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
# }

# with YoutubeDL(ydl_opts) as ydl:
#     ydl.download([youtube_url])
#     info_dict = ydl.extract_info(youtube_url, download=False)
#     video_title = info_dict.get('title', None)

# print(f'Audio has been saved as {audio_output}')

# client = translate.Client()
# response = client.detect_language(video_title)
# language= response['language']


# transcript_test = voice_recognition(f"{video_title}.mp3")


def youtube_main(yt_url):
    # Define the output file name


    audio_output = f'test'

    # Download the audio directly using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': audio_output,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])
        info_dict = ydl.extract_info(yt_url, download=False)
        video_title = info_dict.get('title', None)

    print(f'Audio has been saved as {audio_output}')

    client = translate.Client()
    response = client.detect_language(video_title)
    language= response['language']



    transcript_test = voice_recognition(f"{video_title}.mp3",language)

    with open(f"{video_title}.txt", "w") as file:
        file.write(transcript_test)
    return video_title,transcript_test


if __name__=="__main__":

    while True:
        print("Please paste your youtube URL : ")
        yt_url=input()






        video_title,transcript_test = youtube_main(yt_url)
        summary = application_gpt(transcript_test,client_gpt)

        parse_to_markdown(f"{video_title}",summary)
