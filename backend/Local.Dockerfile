FROM python:2.7-slim

WORKDIR /app/backend

COPY ./requirement.txt ./requirement.txt
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
RUN easy_install pip==20.3.4
RUN pip install -r ./requirement.txt
