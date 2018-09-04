# Author: github.com.prakashpandey

set -ex

# docker hub username
USERNAME=prakashpandey
# image name
IMAGE=tinycoin
# ensure we're up to date
git pull

# bump version
# sudo docker run --rm -v "$PWD":/home/tinycoin prakashpandey/tinycoin patch
version=`cat VERSION`
echo "version: $version"
# run build
./build.sh

# tag it
git add -A
git commit -m "version $version"
git tag -a "$version" -m "version $version"
git push
git push --tags

sudo docker tag $USERNAME/$IMAGE:latest $USERNAME/$IMAGE:$version
