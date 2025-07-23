VENV=.venv
PYTHON=$(VENV)/bin/python

.PHONY: install dev format lint test clean requirements requirements-dev

install:
	uv sync

dev:
	uv run uvicorn run:app --reload --host 0.0.0.0 --port 8000

format:
	uv run isort .
	uv run black .

lint:
	uv run flake8 app tests

test:
	uv run pytest

clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

requirements:
	uv export --format requirements-txt --output-file requirements.txt
 
requirements-dev:
	uv export --format requirements-txt --output-file requirements-dev.txt --all-extras

# uv 환경 동기화
sync:
	uv sync --upgrade

add:
	@echo "Usage: make add PKG=package_name"
	@if [ -z "$(PKG)" ]; then echo "Please specify PKG=package_name"; exit 1; fi
	uv add $(PKG)

add-dev:
	@echo "Usage: make add-dev PKG=package_name"
	@if [ -z "$(PKG)" ]; then echo "Please specify PKG=package_name"; exit 1; fi
	uv add --dev $(PKG)

remove:
	@echo "Usage: make remove PKG=package_name"
	@if [ -z "$(PKG)" ]; then echo "Please specify PKG=package_name"; exit 1; fi
	uv remove $(PKG)