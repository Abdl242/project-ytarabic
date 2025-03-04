FROM python:3.10



COPY requirements.txt .
RUN pip install -r requirements.txt

COPY yt-arabic/ .

CMD ["streamlit", "run", "yt-arabic/interface/streamlit.py", "--server.enableCORS", "false", "--browser.serverAddress", "0.0.0.0", "--browser.gatherUsageStats", "false", "--server.port", "8080"]
