.PHONY: build clean setup

build: setup
	jupyter-book build gallery
	python code/inject_paths.py --reverse

setup:
	python code/setup_env.py
	python code/inject_paths.py

clean:
	python code/inject_paths.py --reverse
	rm -f data_paths_loc.json
	jupyter-book clean gallery --all