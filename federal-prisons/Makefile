# Import aliases
include ./utils/variables.make

MAKENAME = federal-prisons

scrape: ## Scrape data files. Example: make -f ./federal-prisons/Makefile
	$(call start,$(MAKENAME))
	$(call python,./federal-prisons/scrape.py)
	$(call finish)

help: ## Show this help. Example: make -f ./homeless-impact/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: scrape help
