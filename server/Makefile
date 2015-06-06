jade=./node_modules/.bin/jade
JADE=$(shell find templates -name "*.jade" -type f)
HTML=$(JADE:.jade=.html)

default: node_modules $(HTML)

node_modules:
	@npm install

%.html: %.jade
	$(jade) -P < $< --path $< > $@
	@touch $@

clean:
	@rm -f $(shell find . -name *.pyc) $(shell find . -name *.html)
 
.PHONY: clean default
