.PHONY: all
all: pull build migrate run


# Pulls git
pull:
	git checkout master
	git pull

# Build containers
# Images are automatically fetched, if necessary, from docker hub
build:
	docker-compose build

build_local:
	docker-compose -f docker-compose_local.yml build

# Start a new web container to run migrations
# Use --rm to remove the container when the command completes
migrate:
	docker-compose run --rm concord python manage.py migrate

# Run everything in the background with -d
run:
	docker-compose up -d
