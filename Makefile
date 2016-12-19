# convenience Makefile to set up local development
all: venv/bin/cryptoyaml

tests: venv/bin/py.test
	@venv/bin/py.test

venv/bin/python venv/bin/pip:
	python3.5 -m venv venv
	venv/bin/pip install --upgrade pip

venv/bin/cryptoyaml venv/bin/py.test venv/bin/devpi: venv/bin/python venv/bin/pip setup.py
	venv/bin/python setup.py dev
	@touch $@

upload: setup.py venv/bin/py.test venv/bin/devpi
	PATH=${PWD}/venv/bin:${PATH} venv/bin/devpi upload --no-vcs --with-docs

clean:
	git clean -fXd

.PHONY: clean tests upload
