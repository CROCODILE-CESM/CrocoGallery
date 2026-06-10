.PHONY: build clean inject reverse

inject:
	python -m crocogallery

reverse:
	python -m crocogallery --reverse

build: inject
	cd gallery && jupyter-book build --html
	python -m crocogallery --reverse

clean:
	python -m crocogallery --reverse
	cd gallery && jupyter-book clean . --all
