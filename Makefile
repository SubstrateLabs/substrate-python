.PHONY: lint, format, test-all, test-unit, test-e2e, ensure, sync, publish

poetry.lock: pyproject.toml
	poetry lock

ensure: poetry.lock
	poetry install

sync:
	poetry run python scripts/sync_codegen.py

notebook:
	poetry run marimo edit examples/notebook.py

dist/: pyproject.toml poetry.lock substrate/_version.py
	poetry build -C=dist

lint:
	poetry run ruff check .

format:
	poetry run ruff format .
	poetry run ruff check --fix .

test-unit:
	poetry run pytest -m unit

test-e2e:
	poetry run pytest -m e2e

test-all: test-unit test-e2e

publish: dist/
	poetry config pypi-token.pypi ${PYPI_TOKEN}
	poetry publish
