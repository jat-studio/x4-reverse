venv_create:
	python3 -m venv venv

venv_activate: venv_create
	venv/bin/activate
	pip install -r requirements.txt

tests: venv_activate
	pytest -vv --cov=src tests
