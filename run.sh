#!/bin/bash

set -e

NAME=spark-submit
TAG=0.1
IMAGE=$NAME:$TAG
NETWORK=hadoop_network

./build.sh
echo building $IMAGE in $(pwd)
docker build -t $IMAGE .
docker run -it --name $NAME --env-file ./config --network $NETWORK --rm $IMAGE ./submit.sh