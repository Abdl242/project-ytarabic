import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
import warnings
warnings.filterwarnings("ignore")
import IPython.display as ipd
from transformers import pipeline
from pydub import AudioSegment
import json


from yt_dlp import YoutubeDL

#from moviepy.editor import VideoFileClip
from vosk import Model, KaldiRecognizer


import nltk
import re
import textwrap
from nltk.tokenize import sent_tokenize

# تحميل ملفات NLTK المطلوبة
nltk.download('punkt')

import re
#from textblob import TextBlob

from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer

def voice_recognition(filename):
    FRAME_RATE = 16000
    CHANNELS=1
    model = Model(model_name="vosk-model-ar-0.22-linto-1.1.0")
    rec = KaldiRecognizer(model, FRAME_RATE)
    rec.SetWords(True)

    mp3 = AudioSegment.from_mp3(filename)
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



youtube_url = 'https://www.youtube.com/watch?v=6Yc37c5suaw&t=271s'

# Define the output file name
audio_output = 'chaar_jahily'

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
    ydl.download([youtube_url])

print(f'Audio has been saved as {audio_output}')

transcript_test = voice_recognition("الخمر في الديانات الثلاث.mp3")
with open("totranslate.txt", "w") as file:
    file.write(transcript_test)
