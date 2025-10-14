.PHONY: build clean setup

build: setup
	jupyter-book build gallery
	python code/inject_paths_into_notebooks.py --reverse

setup:
	python code/setup_credentials_and_cesm.py
	python code/inject_paths_into_notebooks.py

clean:
	python code/inject_paths_into_notebooks.py --reverse
	rm -f data_paths_loc.json
	jupyter-book clean gallery --all