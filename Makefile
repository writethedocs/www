ROOT_DIR = $(shell pwd)
VIRTUALENV = virtualenv
VIRTUALENV_DIR = $(ROOT_DIR)/lib/virtualenv
BIN_DIR = $(VIRTUALENV_DIR)/bin
PIP = $(BIN_DIR)/pip
PIP_REQUIREMENTS = $(ROOT_DIR)/etc/pip/requirements.txt
SPHINX_BUILD = $(BIN_DIR)/sphinx-build


virtualenv:
	if [ ! -d $(VIRTUALENV_DIR) ]; then mkdir -p $(VIRTUALENV_DIR); fi
	if [ ! -x $(PIP) ]; then $(VIRTUALENV) --distribute --no-site-packages $(VIRTUALENV_DIR); fi


dependencies:
	if [ ! -x $(SPHINX_BUILD) ]; then $(PIP) install -r $(PIP_REQUIREMENTS); fi


develop: virtualenv dependencies


documentation:
	mkdir -p $(ROOT_DIR)/var/docs
	make --directory=docs clean html
