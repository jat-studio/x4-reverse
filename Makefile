venv_create:
	python3 -m venv venv

venv_activate: venv_create
	venv/bin/activate
	pip install -r requirements.txt

run: venv_activate
	python3 -m src.main

tests: venv_activate
	pytest -vv --cov-config=.coveragerc --cov=src --cov-report term-missing:skip-covered tests
