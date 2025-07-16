# Makefile for PV Simulator

PROJECT_NAME = pv_simulator
DOCKER_COMPOSE = docker-compose
PYTHON = python3.12

.PHONY: help build up down logs test lint clean reset

help:
	@echo "Usage:"
	@echo "  make build      Build all Docker images"
	@echo "  make up         Start all services"
	@echo "  make down       Stop all services"
	@echo "  make logs       View logs from services"
	@echo "  make test       Run unit tests"
	@echo "  make lint       Run flake8 linting"
	@echo "  make op     tails output file"

build:
	$(DOCKER_COMPOSE) build --no-cache

up:
	$(DOCKER_COMPOSE) up

down:
	$(DOCKER_COMPOSE) down

logs:
	$(DOCKER_COMPOSE) logs -f

test:
	pytest tests/

lint:
	$(DOCKER_COMPOSE) run --rm pv_simulator flake8 .

op:
	$(DOCKER_COMPOSE) exec -T pv_simulator tail -f output/pv_output.csv