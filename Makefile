PY = python3
RM = rm -rf
TWINE = twine
TOX = tox
LINT = pylint --rcfile=./.pylintrc

.PHONY: all check dist sdist test tox tox-v tox-report lint doc upload clean

all: dist check test

dist: sdist

test: tox lint

sdist:
	$(PY) setup.py $@

tox:
	$(TOX) -p -e py{36,37,38}

tox-v:
	$(TOX) -e py{36,37,38}

tox-report:
	- $(TOX) -p -e clean,py36,report -- --cov-report=term-missing --cov-append
	python3.7 -m http.server --directory .test/htmlcov/ 3000

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
	- $(TOX) -e clean
	- $(RM) build dist .tox .test __pycache__
