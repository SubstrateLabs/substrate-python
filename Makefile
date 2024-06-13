.DEFAULT_GOAL := help
.PHONY: help, lint, format, test-all, test-unit, test-e2e, ensure, sync, publish, notebook, dist, clean
SHELL := /bin/bash

default: help;

help:
	@echo "꩜ Substrate Python SDK"
	@echo "See DEVELOPING.md for more info."
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Main targets:"
	@echo "  develop             Install dependencies"
	@echo "  sync                Sync generated code & bump version"
	@echo "  sync-version        Sync SDK version to project"
	@echo "  clean               Remove all build, test, coverage and Python artifacts"
	@echo "  dist                Builds source and wheel package"
	@echo "  publish             Publish to pypi"
	@echo ""


poetry.lock: pyproject.toml
	poetry lock

ensure: poetry.lock
	poetry install

sync: sync-version sync-codegen format

sync-version:
	poetry run python scripts/sync_version.py

sync-codegen:
	poetry run python scripts/sync_codegen.py

notebook:
	poetry run marimo edit examples/notebook.py

dist: pyproject.toml poetry.lock substrate/_version.py
	poetry build -C=dist && poetry run twine check dist/*

lint:
	poetry run ruff check .

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr site/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

format:
	poetry run ruff format .
	poetry run ruff check --fix .

test-unit:
	poetry run pytest -m unit

test-e2e:
	poetry run pytest -m e2e

test-all: test-unit test-e2e

publish: dist/
	poetry run twine upload dist/*
