# Import aliases
include ./utils/variables.make

MAKENAME = ice-detainees

scrape: ## Scrape data files. Example: make -f ./ice-detainees/Makefile
	$(call start,$(MAKENAME))
	$(call jupyter,./ice-detainees/scrape.ipynb)
	$(call finish)

help: ## Show this help. Example: make -f ./ice-detainees/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
