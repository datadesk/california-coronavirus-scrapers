# california-coronavirus-scrapers

An experiment in open-sourcing the web scrapers that feed the [Los Angeles Times' California coronavirus tracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/). The scrapers are written using Python and Jupyter notebooks, scheduled and run via GitHub Actions and then archived using git.

## Scrapers

| module                  | status                                                                                                                                                                                                                                                   | maintainer  |
|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| [cases-deaths-demographics](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-demographics) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-demographics.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-demographics.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [cases-deaths-tests](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-tests) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [school-reopenings](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/school-reopenings) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/school-reopenings.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/school-reopenings.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [vaccine-doses-on-hand](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-doses-on-hand) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-doses-on-hand.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-doses-on-hand.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-progress](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-progress) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-hpi](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-hpi) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-hpi.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-hpi.yml)| [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-demographics](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics.yml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-shipped-delivered](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-shipped-delivered) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-shipped-delivered.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-shipped-delivered.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [variant-proportions-states](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-proportions-states) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-shipped-delivered.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-proportions-states.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [variant-toplines-ca](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-toplines-ca) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-toplines-ca.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-toplines-ca.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |

## Installation

Clone the repository and install the Python dependencies.

```zsh
pipenv install
```

Run all of the scraper commands.

```zsh
make
```
![make all](./.github/img/make.gif)

Run one of the scraper commands.

```zsh
make -f vaccine-doses-on-hand/Makefile
```
