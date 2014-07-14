MAIN_TREE := HEAD
MAIN_COMMIT := $(shell git rev-parse --verify $(MAIN_TREE))
PROG := pymongo

sources:
	@git archive --format=tar --prefix="$(PROG)/" $(MAIN_COMMIT) | gzip > "$(PROG).tar.gz"
