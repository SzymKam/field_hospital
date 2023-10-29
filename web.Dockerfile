FROM python:3.11

LABEL authors="SzymKam"

WORKDIR src

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN mkdir -p /staticfiles

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /src/
