PY = python3
RM = rm -rf
LINT = pylint --rcfile=./.pylintrc
TWINE = twine

.PHONY: all check dist sdist test lint doc upload clean

all: dist check test

dist: sdist

sdist:
	$(PY) setup.py $@

check:
	$(TWINE) check dist/*
	# $(PY) setup.py check -r -s

test: lint

lint:
	$(LINT) ckip_classic

doc:
	( cd docs ; make clean ; make html )

upload: dist check
	ls dist/*.tar.gz
	$(TWINE) upload --repository-url https://test.pypi.org/legacy/ dist/*.tar.gz --verbose

clean:
	( cd docs ; make clean )
	$(PY) setup.py clean -a
	$(RM) build dist *.egg-info *.so __pycache__
