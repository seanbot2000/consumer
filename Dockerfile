FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE=1

RUN pip3 install pika

COPY . .


CMD ["python3", "-u", "./consumer.py"]