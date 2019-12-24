.PHONY: help install setup test lint shell clean

VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python3
.RECIPEPREFIX +=

ifdef LIST
ARGS += -f $(LIST)
endif
ifdef DEST
ARGS += -d $(DEST)
endif

.DEFAULT: help
help:
	@echo "make install"
	@echo "       install dependencies"
	@echo "make test"
	@echo "       run test script"
	@echo "make shell"
	@echo "       run shell-like downloader"
	@echo "make shell LIST=[filename]"
	@echo "       run downloader on each line in [filename]"
	@echo "make shell DEST=[directory]"
	@echo "       run downloader and output mp3s to [directory]"
	@echo "make clean"
	@echo "       clean up directory"

install:
	python3 -m pip install virtualenv
	$(MAKE) venv

# change in requirements.txt -> re-run installation of dependencies.
venv: $(VENV_NAME)/bin/activate setup
$(VENV_NAME)/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; ${PYTHON} -m pip install -Ur requirements.txt
	touch venv/bin/activate
setup:
	@test -d tmp || mkdir tmp
	@test -d out || mkdir out

test: venv
	${PYTHON} -m test

# pylint blows, don't run, I didn't even include the dependency
lint: venv
	${PYTHON} -m pylint

shell: venv
	${PYTHON} -m shell $(ARGS)

clean:
	rm -rf out
	rm -rf tmp
	rm -rf __pycache__

