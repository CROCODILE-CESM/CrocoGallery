.PHONY: build clean setup

build: setup
	jupyter-book build gallery

setup:
	python code/setup_credentials_and_cesm.py
	python code/inject_paths_into_notebooks.py

clean:
	python code/inject_paths_into_notebooks.py --reverse
	jupyter-book clean gallery --all