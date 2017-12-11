FROM alpine:latest
MAINTAINER Frazier Baker <fraziernb@gmail.com>

RUN apk update
RUN apk add bash python python-pip python-dev
RUN pip install tensorflow

RUN mkdir /openai
WORKDIR /openai
RUN git clone https://github.com/openai/gym
WORKDIR /openai/gym
RUN pip install -e .