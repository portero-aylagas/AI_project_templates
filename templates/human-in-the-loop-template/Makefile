.PHONY: verify test compile lint

PYTHON ?= python3

verify: compile lint test

compile:
	$(PYTHON) -m compileall -q src tests

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest -q

