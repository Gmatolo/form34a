install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
    #python -m pytest -vv --cov=myrepolib tests/*.py
    #python -m pytest --nbval notebook.ipynb

#validate that change run on circleci remote build
validate-circle:
	circleci config process .circleci/config.yml

#simulate circle locally	
run-circleci-local:
	circleci local execute

lint:
	pylint --disable=R,C main.py

all: install lint test