# Docker image for tinycoin
# Ubuntu version used 18.04 LTS (Bionic Beaver)

FROM Ubuntu:18.04
LABEL MAINTAINER="https://github.com/prakashpandey"

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    apt install python3-pip && \
    apt-get clean

RUN git clone https://github.com/prakashpandey/tinycoin /home/tinycoin && \
    cd /home/tinycoin && \
    pip3 install -r requirement.txt && \
    ./start.sh

EXPOSE 5000
