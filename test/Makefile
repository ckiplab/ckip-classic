RM = rm -rf
TOX = tox

.PHONY: tox tox-v tox-report clean

tox:
	NO_COV= $(TOX) -p -e py36-client --
	NO_COV= $(TOX) -p -e py{36,37,38} --

tox-v:
	NO_COV= $(TOX) -e py36-client -- -v
	NO_COV= $(TOX) -e py{36,37,38} -- -v

tox-vv:
	NO_COV= $(TOX) -e py36-client -- -vv
	NO_COV= $(TOX) -e py{36,37,38} -- -vv

tox-report:
	- $(TOX) -p -e clean,py36,py36-client,report -- --cov-append
	python3.7 -m http.server --directory .test/htmlcov/ 3000

clean:
	- $(RM) .tox .test .lookup
