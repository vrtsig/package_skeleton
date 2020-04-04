.DEFAULT_GOAL := help

.PHONY: help
help:  ## show all make commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: install-requirements
install-requirements:  ## install requirements
	pip install -r requirements.txt -U

.PHONY: install-test-requirements
install-test-requirements:  ## install test requirements
	pip install -r test_requirements.txt -U

.PHONY: install
install:  ## install package in dev mode
	pip install -e .

.PHONY: lint
lint:  ## lint python files
	flake8 {{ cookiecutter.package_name }} tests

.PHONY: test
test:  ## run tests
	pytest tests