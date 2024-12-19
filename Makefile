.PHONY: install run destroy

install:
	bash install.sh

run:
	bash run.sh

build:
	bash build.sh

run-docker:
	docker-compose up

destroy:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm .env

