# Import aliases
include ./utils/variables.make

MAKENAME = bed-surges

all: scrape

scrape: ## Scrape data files. Example: make -f ./bed-surges/Makefile scrape
	$(call python,./bed-surges/scrape.py)

help: ## Show this help. Example: make -f ./bed-surges/Makefile help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Mark commands without a target
.PHONY: all scrape lint help
