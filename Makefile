# Variables
PYTHON = python3
MANAGE = $(PYTHON) manage.py
PIP = $(PYTHON) -m pip
VENV_NAME = venv
VENV_ACTIVATE = . $(VENV_NAME)/bin/activate
SYSTEM_PYTHON = $(shell which python3)

# Comandos
.PHONY: all venv run migrate test coverage requirements clean setup help

all: setup

venv:
	test -d $(VENV_NAME) || $(SYSTEM_PYTHON) -m venv $(VENV_NAME)
	$(VENV_ACTIVATE) && $(PIP) install --upgrade pip

run: venv
	$(VENV_ACTIVATE) && $(MANAGE) runserver

migrate: venv
	$(VENV_ACTIVATE) && $(MANAGE) makemigrations
	$(VENV_ACTIVATE) && $(MANAGE) migrate

test: venv
	$(VENV_ACTIVATE) && $(MANAGE) test

coverage: venv
	$(VENV_ACTIVATE) && $(PIP) install coverage
	$(VENV_ACTIVATE) && coverage run --source='.' manage.py test
	$(VENV_ACTIVATE) && coverage report
	$(VENV_ACTIVATE) && coverage html

requirements: venv
	$(VENV_ACTIVATE) && $(PIP) freeze > requirements.txt

install: venv
	$(VENV_ACTIVATE) && $(PIP) install -r requirements.txt

clean:
	rm -rf $(VENV_NAME)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .coverage htmlcov

setup: venv install migrate

# Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make              : Configura el proyecto (crea venv, instala dependencias y migra)"
	@echo "  make venv         : Crea el entorno virtual"
	@echo "  make run          : Inicia el servidor de desarrollo"
	@echo "  make migrate      : Ejecuta las migraciones de la base de datos"
	@echo "  make test         : Ejecuta las pruebas"
	@echo "  make coverage     : Ejecuta las pruebas con cobertura"
	@echo "  make requirements : Actualiza el archivo requirements.txt"
	@echo "  make install      : Instala las dependencias del proyecto"
	@echo "  make clean        : Limpia archivos temporales, caché y el entorno virtual"
	@echo "  make setup        : Configura el proyecto (instala dependencias y migra)"
	@echo "  make help         : Muestra esta ayuda"