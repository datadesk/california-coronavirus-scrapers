# Makefile
# The master commands that update our coronavirus tracker's data supply


# Import global variables
include ./utils/variables.make

all: scrape          \
     clean_notebooks

scrape: ## Verify that our notebooks can be parsed and run. Example: make scrape
	$(call banner,🔪 Scraping data 🔪)
	@$(MAKE) --no-print-directory -f vaccine-doses-on-hand/Makefile
	@$(MAKE) --no-print-directory -f vaccine-doses-administered/Makefile


clean_notebooks: ## Remove all temporary notebook outputs created by the our commands. Example: make clean_notebooks
	@find . -type f -name '*-output.ipynb' -delete


lint_notebooks: ## Verify that our notebooks can be parsed and run. Example: make lint_notebooks
	@pipenv run jupyter nbconvert ./**/*.ipynb --to=html --stdout > /dev/null


help: ## Show this help. Example: make help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


# Mark all the command that don't have a target
.PHONY: all             \
        scrape          \
        lint_notebooks  \
        help
