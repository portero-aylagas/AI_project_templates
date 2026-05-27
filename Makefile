.PHONY: verify structure

PYTHON ?= python3

verify: structure

structure:
	$(PYTHON) scripts/verify_templates.py

