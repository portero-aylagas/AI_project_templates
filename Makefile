.PHONY: verify verify-full structure

PYTHON ?= python3

verify: structure

structure:
	$(PYTHON) scripts/verify_templates.py

verify-full: verify
	@set -eu; \
	for template in templates/*; do \
		if [ -d "$$template" ]; then \
			echo "==> $$template"; \
			$(MAKE) -C "$$template" verify; \
		fi; \
	done
