SHELL := /bin/bash

pdf:
	python make.py compile
	python make.py clean

bib:
	python make.py bib