# Import aliases
include ./utils/variables.make

MAKENAME = variant-zip-codes

scrape: ## Scrape data files. Example: make -f ./vaccine-zip-codes/Makefile
	$(call start,$(MAKENAME))
	$(call jupyter,./vaccine-zip-codes/scrape.ipynb)    
	$(call finish)

help: ## Show this help. Example: make -f ./vaccine-zip-codes/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
