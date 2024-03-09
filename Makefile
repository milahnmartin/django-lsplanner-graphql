# Makefile for FastAPI project

# Variables
PYTHON = python
PIP = pip
DOCKER_COMPOSE = docker-compose

# Targets
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install       Install project dependencies"
	@echo "  run           Run the FastAPI application"
	@echo "  stop          Stop running containers"
	@echo "  compose-up    Start containers defined in docker-compose.yml"
	@echo "  compose-build Build or rebuild services defined in docker-compose.yml"
	@echo "  clean         Remove generated files and dependencies"

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) -m uvicorn main:app --host 0.0.0.0 --port 8000

stop:
	$(DOCKER_COMPOSE) down

start:
	$(DOCKER_COMPOSE) up -d --build

compose-up:
	$(DOCKER_COMPOSE) up -d

compose-build:
	$(DOCKER_COMPOSE) build

restart:
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) up -d --build

docker-clean:
	$(DOCKER_COMPOSE) down --rmi all --volumes

clean:
	rm -rf __pycache__ *.pyc

dev:
	uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

dev-compose-up:
	docker-compose -f docker-compose.dev.yml up -d
