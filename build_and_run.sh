#!/bin/sh
set -ex


sudo docker build -t 'concord' .
sudo docker rm -f concord || :
sudo docker run \
	-d \
	--name 'concord' \
	--volume '/etc/letsencrypt:/etc/letsencrypt' \
	--volume '/etc/nginx/dhparam:/etc/nginx/dhparam' \
	-p 80:80 \
	-p 443:443 \
	concord
