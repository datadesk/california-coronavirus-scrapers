# Import aliases
include ./utils/variables.make

MAKENAME = hospital-capacity

scrape: ## Scrape data files. Example: make -f ./hospital-capacity/Makefile
	$(call start,$(MAKENAME))
	$(call python,./hospital-capacity/scrape.py)
	$(call finish)

help: ## Show this help. Example: make -f ./hospital-capacity/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
