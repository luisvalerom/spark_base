#!/bin/bash

set -e

NAME=spark-base
TAG=0.1
IMAGE=$NAME:$TAG

echo building $IMAGE in $(pwd)
docker build -t $IMAGE ./base