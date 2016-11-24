APP=factory
VENV_HOME=~/venvs
VENV_DIR=$(VENV_HOME)/$(APP)
VENV_BIN=virtualenv
PYTHON_BIN=$(VENV_DIR)/bin/python
PIP_BIN=$(VENV_DIR)/bin/pip
RUN_IP="0.0.0.0:8888"

clean:
	rm -rf $(VENV_DIR)

venv:
	test -d $(VENV_HOME) || mkdir -p $(VENV_HOME)
	test -d $(VENV_DIR)  || $(VENV_BIN) $(VENV_DIR)
	$(PIP_BIN) install --upgrade pip

install: venv
	$(PIP_BIN) install -r requirements.txt

migrate:
	$(PYTHON_BIN) manage.py migrate --noinput

start: migrate
	$(PYTHON_BIN) manage.py runserver $(RUN_IP)
