ROOT_DIR = $(shell pwd)
VIRTUALENV = virtualenv
VIRTUALENV_DIR = $(ROOT_DIR)/lib/virtualenv
BIN_DIR = $(VIRTUALENV_DIR)/bin
PIP = $(BIN_DIR)/pip
PIP_REQUIREMENTS = $(ROOT_DIR)/etc/pip/requirements.txt
SPHINX_BUILD = $(BIN_DIR)/sphinx-build
NOSE = $(BIN_DIR)/nosetests


virtualenv:
	if [ ! -d $(VIRTUALENV_DIR) ]; then mkdir -p $(VIRTUALENV_DIR); fi
	if [ ! -x $(PIP) ]; then $(VIRTUALENV) --distribute --no-site-packages $(VIRTUALENV_DIR); fi


dependencies:
	if [ ! -x $(SPHINX_BUILD) ]; then $(PIP) install -r $(PIP_REQUIREMENTS) --use-mirrors; fi


develop: virtualenv dependencies


update:
	$(PIP) install -U -r $(PIP_REQUIREMENTS) --use-mirrors


docs/_static:
	mkdir -p docs/_static


var/docs:
	mkdir -p $(ROOT_DIR)/var/docs


documentation: docs/_static var/docs
	make --directory=docs clean html doctest


test:
	$(NOSE) --config=etc/nose.cfg


clean:
	find $(ROOT_DIR)/ -name "*.pyc" -delete


distclean: clean


maintainer-clean:
	rm -rf $(ROOT_DIR)/bin/ $(ROOT_DIR)/lib/
