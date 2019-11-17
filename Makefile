.PHONY: help install test lint run clean

VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3
.RECIPEPREFIX +=

.DEFAULT: help
help:
    @echo "make install"
    @echo "       install dependencies"
    @echo "make test"
    @echo "       run test script"
    @echo "make lint"
    @echo "       run pylint"
    @echo "make run"
    @echo "       run project"

install:
    python3 -m pip install virtualenv
    test -d tmp || mkdir tmp
    test -d out || mkdir out
    $(MAKE) venv

# change in requirements.txt -> re-run installation of dependencies.
venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: requirements.txt
    test -d venv || virtualenv venv
    . venv/bin/activate; ${PYTHON} -m pip install -Ur requirements.txt
    touch venv/bin/activate

test: venv
    ${PYTHON} -m test

# pylint blows, don't run, I didn't even include the dependency
lint: venv
    ${PYTHON} -m pylint

run: venv
    ${PYTHON} -m download

clean:
    rm -rf out
    rm -rf tmp
    rm -rf __pycache__

