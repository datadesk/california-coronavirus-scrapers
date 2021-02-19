# california-coronavirus-scrapers

An experiment in open-sourcing the web scrapers that feed the [Los Angeles Times' California coronavirus tracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/). The scrapers are written using Python and Jupyter notebooks, scheduled and run via GitHub Actions and then archived using git.

## Getting started

Clone the repository and install the Python dependencies.

```zsh
pipenv install
```

Run all of the scraper commands.

```zsh
make
```
![make all](./img/make.gif)

Run one of the scraper commands.

```zsh
make -f vaccine-doses-on-hand/Makefile
```

## Scrapers

| module                  | status                                                                                                                                                                                                                                                   | maintainer  |
|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| [vaccine-doses-on-hand](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-doses-on-hand) | [![Vaccine doses on hand](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-doses-on-hand.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-doses-on-hand.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
