PY = python3
RM = rm -rf
TWINE = twine
TOX = tox
LINT = pylint --rcfile=./.pylintrc

.PHONY: all check dist sdist test tox tox-cov lint doc upload clean

all: dist check test

dist: sdist

test: tox lint

sdist:
	$(PY) setup.py $@

tox:
	$(TOX)

tox-cov:
	- $(TOX) -e ws -- --cov-report=html:htmlcov/ws
	- $(TOX) -e parser -- --cov-report=html:htmlcov/parser
	python3.7 -m http.server --directory htmlcov/ 3000

lint:
	$(LINT) ckip_classic

check:
	$(TWINE) check dist/*
	# $(PY) setup.py check -r -s

doc:
	( cd docs ; make clean ; make html )

upload: dist check
	ls dist/*.tar.gz
	$(TWINE) upload --repository-url https://test.pypi.org/legacy/ dist/*.tar.gz --verbose

clean:
	( cd docs ; make clean )
	$(PY) setup.py clean -a
	$(RM) build dist *.egg-info *.so __pycache__
