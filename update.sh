#!/bin/sh
set -ex


git checkout master
git pull
docker rm -f $(docker ps -a -q)
docker-compose build --no-cache
docker-compose up -d
