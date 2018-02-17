FROM ubuntu:latest

RUN apt update && \
	apt install -y software-properties-common && \
	apt update && \
	apt install -y python3 nginx

VOLUME ["/etc/letsencrypt", "/etc/nginx/dhparam"]

EXPOSE 80 443

ADD server /srv/server
ADD client /var/www/html/concord
COPY nginx.conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
