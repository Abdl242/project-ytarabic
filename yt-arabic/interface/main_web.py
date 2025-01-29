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

from functions import *
from params import *
from tonotion import to_notion
from toicloud import save_to_local_icloud


if __name__=="__main__":

    while True:
        print("Please paste your  URL : ")
        web_url=input()

        #playlist_name, video_urls = get_playlist_details(web_url)


        print(f"Processing video {web_url}")
        video_title,transcript_test = youtube_main(web_url)
        summary = application_gpt(transcript_test,client_gpt)



        # parse_to_markdown(f"data/{playlist_name}/{video_title}",summary)
        # to_notion(f"data/{playlist_name}/{video_title}.md",NOTION_PATH[playlist_name],video_title)
        # save_to_local_icloud(f"data/{playlist_name}/{video_title}.md")
