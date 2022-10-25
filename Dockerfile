# syntax=docker/dockerfile:1

# Base Image
FROM python:3.9

LABEL maintainer="overbergsoftware@gmail.com"

# (generate pyc) faster startup times.
ENV PYTHONDONTWRITEBYTECODE=1

# Immediatley stream log messages
ENV PYTHONUNBUFFERED=1

# Specify a working directory.
WORKDIR /code

# Copy requirements.txt and Makefile file to /code directory.
COPY requirements.txt /code/
COPY Makefile /code/

# Install all dependencies into virtual environment (venv) from requirements.txt file.
RUN python3 -m venv /venv
RUN /venv/bin/pip install -r requirements.txt

# Add virtual environment (venv) to environment variables.
ENV PATH="/venv/bin:$PATH"

COPY . /code/
