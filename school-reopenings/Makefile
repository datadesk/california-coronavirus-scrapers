# Import aliases
include ./utils/variables.make

MAKENAME = school-reopenings

scrape: ## Scrape data files. Example: make -f ./school-reopenings/Makefile
	$(call start,$(MAKENAME))
	$(call python,./school-reopenings/scrape.py)
	$(call jupyter,./school-reopenings/concatenate_districts.ipynb)
	$(call finish)

help: ## Show this help. Example: make -f ./school-reopenings/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
