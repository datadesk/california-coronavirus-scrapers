# Import aliases
include ./utils/variables.make

MAKENAME = vaccine-demographics-by-county

scrape: ## Scrape data files. Example: make -f ./vaccine-demographics-by-county/Makefile
	$(call start,$(MAKENAME))
	$(call python,./vaccine-demographics-by-county/scrape.py)
	$(call finish)

help: ## Show this help. Example: make -f ./vaccine-demographics-by-county/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
