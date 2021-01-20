PY = python3
RM = rm -rf
TWINE = twine
TOX = tox
LINT = pylint --rcfile=./.pylintrc

.PHONY: all check dist sdist test tox tox-v tox-vv tox-report lint doc upload clean

all: dist check test

dist: sdist

test: tox lint

sdist:
	$(PY) setup.py $@

lint:
	$(LINT) ckip_classic

check:
	$(TWINE) check dist/*
	# $(PY) setup.py check -r -s

tox tox-v tox-vv tox-report:
	( cd test ; make $@ )

doc:
	( cd docs ; make clean ; make html )

upload: dist check
	ls dist/*.tar.gz
	$(TWINE) upload --repository-url https://test.pypi.org/legacy/ dist/*.tar.gz --verbose

clean:
	- ( cd docs ; make clean )
	- ( cd test ; make clean )
	- $(PY) setup.py clean -a
	- $(RM) build dist *.egg-info .eggs .tox .test __pycache__
