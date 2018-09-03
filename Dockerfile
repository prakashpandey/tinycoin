# Docker image for tinycoin
# Ubuntu version used 18.04 LTS (Bionic Beaver)

FROM ubuntu:18.04
LABEL MAINTAINER="https://github.com/prakashpandey"

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    apt-get install -y  git && \
    apt install python3-pip -y && \
    apt-get clean -y

RUN git clone https://github.com/prakashpandey/tinycoin /home/tinycoin && \
    cd /home/tinycoin && \
    pip3 install -r requirements.txt && \
    ./start.sh

EXPOSE 5000
