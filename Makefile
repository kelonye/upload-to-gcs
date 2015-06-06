default:
	@$(MAKE) --no-print-directory -C client/app
	@$(MAKE) --no-print-directory -C server

run:
	@clear
	@dev_appserver.py . --clear_datastore yes --port 3000 --admin_port 7000 --host 0.0.0.0

clean:
	@rm -rf public $(shell find . -name "*.pyc")

.PHONY: clean gen-pm gen-i-end gen-i gen-a test index deploy run default
