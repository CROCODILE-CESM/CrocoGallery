.PHONY: build clean inject reverse

inject:
	python -m crocogallery

reverse:
	python -m crocogallery --reverse

build: inject
	jupyter-book build --html
	python -m crocogallery --reverse

clean:
	python -m crocogallery --reverse
	jupyter-book clean . --all
