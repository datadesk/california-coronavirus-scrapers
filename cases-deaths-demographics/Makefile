# Import aliases
include ./utils/variables.make

MAKENAME = cases-deaths-demographics

scrape: ## Scrape data files. Example: make -f ./cases-deaths-demographics/Makefile
	$(call start,$(MAKENAME))
	$(call python,./cases-deaths-demographics/scrape.py)
	$(call finish)

help: ## Show this help. Example: make -f ./cases-deaths-demographics/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
