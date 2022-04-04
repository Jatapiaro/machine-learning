FROM python:slim-buster

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
COPY datasets /usr/datasets/

# See https://towardsdatascience.com/how-to-build-slim-docker-images-fast-ecc246d7f4a7
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN pip install --no-cache-dir -r requirements.txt