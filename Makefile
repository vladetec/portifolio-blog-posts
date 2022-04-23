define USAGE
Super awesome hand-crafted build system ⚙️
By Vladetec.

Commands:
	create    create project directories and files.
	init      Install Python dependencies with venv
	serve     Run app in dev environment.
	check     cat -e -t -v  makefile
endef

export USAGE
help:
	@echo "$$USAGE"

create:
	mkdir -p templates static
	touch app.py database.py Procfile

init:
	pip install -U pip
	pip install -U setuptools wheel
	pip install -r requirements.txt

serve:
	FLASK_APP=app 
	FLASK_ENV=development
	flask run

check:
	cat -e -t -v  Makefile
