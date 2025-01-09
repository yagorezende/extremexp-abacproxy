.PHONY: install run destroy run-docker build docker-destroy

install:
	bash install.sh

run:
	bash run.sh

build:
	bash build.sh

run-docker:
	docker-compose up --build

docker-destroy:
	docker-compose down
	docker-compose rm -f
	docker container prune
	docker image prune -a

destroy:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm .env

