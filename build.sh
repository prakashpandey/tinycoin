# Author: github.com.prakashpandey

set -ex

# docker hub username
USERNAME=prakashpandey
# image name
IMAGE=tinycoin
sudo docker build -t $USERNAME/$IMAGE:latest .