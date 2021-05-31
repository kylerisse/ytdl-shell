FROM python:3.9.5-buster
COPY src/ /app
WORKDIR /app
RUN apt update; apt install -y ffmpeg
RUN pip install -r requirements.txt
