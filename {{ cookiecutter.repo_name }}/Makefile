.DEFAULT_GOAL := help

.PHONY: help
help:  ## show all make commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'
