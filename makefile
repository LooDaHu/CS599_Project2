.PHONY:
	run

SHELL :=/bin/bash

VENV_NAME?=venv
VENV_ACTIVATE=./${VENV_NAME}/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help:
	@echo "make run"
	@echo "       run project and create figures"

# enter virtual environment
rvenv:
	source ./venv/bin/activate


run:
	source ./venv/bin/activate
	python figure1.py ./text_gcn/data/mr
	python figure2.py ./text_gcn/data/R8
