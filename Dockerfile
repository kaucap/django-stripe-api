FROM python:3.8

WORKDIR /src
RUN pip install -r requirements.txt
COPY . /src