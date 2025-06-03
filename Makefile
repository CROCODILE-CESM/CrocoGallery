.PHONY: build clean data

build: data
	jupyter-book build gallery

data:
	python code/generate_data.py

clean:
	jupyter-book clean gallery --all