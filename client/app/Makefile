component=./node_modules/component-hooks/node_modules/.bin/component
client = $(shell find .. -type f) $(shell find . -type f)

../../public/app.js: node_modules components $(client)
	@$(MAKE) build

build:
	@node build.js
	@du -H ../../public/app.*
	@touch ../../public/

node_modules:
	@npm install

components:
	@$(component) install

distclean:
	@rm -rf components

.PHONY: distclean build
