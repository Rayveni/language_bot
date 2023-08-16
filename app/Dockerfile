FROM python:3.9.16-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


ADD /libs /app/external_libs
ADD /db/manager /app/external_libs/db_manager

COPY app/requirements.txt /
RUN pip3 install --no-cache-dir -r /requirements.txt

WORKDIR /app/app

