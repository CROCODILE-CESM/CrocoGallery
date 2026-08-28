.PHONY: build clean inject reverse

inject:
	python -m crocogallery inject

reverse:
	python -m crocogallery inject --reverse

build: inject
	jupyter-book build --html
	python -m crocogallery inject --reverse

clean:
	python -m crocogallery inject --reverse
	jupyter-book clean . --all
