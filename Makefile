PY = python3
RM = rm -rf
TWINE = twine
TOX = tox
LINT = pylint --rcfile=./.pylintrc

.PHONY: all check dist sdist test tox tox-seq tox-report lint doc upload clean

all: dist check test

dist: sdist

test: tox lint

sdist:
	$(PY) setup.py $@

tox:
	- $(TOX) -p -- --cov-report=term-missing --cov-append

tox-seq:
	$(TOX) -e py{36,37,38}

tox-report: tox
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
	- ( cd docs ; make clean )
	- $(PY) setup.py clean -a
	- $(RM) build dist .tox .coverage htmlcov *.egg-info *.so __pycache__
