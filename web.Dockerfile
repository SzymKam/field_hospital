FROM python:3.11

LABEL authors="SzymKam"

WORKDIR src

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY pyproject.toml .

RUN mkdir -p /staticfiles

RUN pip install --upgrade pip && pip install poetry && poetry install --no-cache

COPY src/ /src/
