install:
	pip install -r requirements.txt
format:
	black *.py
lint:
	pylint --disable=R,C --ignore-patterns=test_main.py main.py
test:
	python -m pytest -vv --cov=main test_main.py
all: install format test lint