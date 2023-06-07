The open-source web scrapers that feed the [Los Angeles Times' California coronavirus tracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/).

Processed data ready for analysis is available at [datadesk/california-coronavirus-data](https://github.com/datadesk/california-coronavirus-data).

## Scrapers

The scrapers are written using Python and Jupyter notebooks, scheduled and run via GitHub Actions and then archived using git.

| module                  | status                                                                                                                                                                                                                                                   | maintainer  |
|:----------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| [bed-surges](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/bed-surges) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [cases-deaths-demographics](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-demographics) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [cases-deaths-tests](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-tests) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [cdc-community-levels](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cdc-community-levels) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [demographics-age](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/demographics-age) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [demographics-race-by-county](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/demographics-race-by-county) | Retired | [Rahul Mukherjee](https://www.latimes.com/people/rahul-mukherjee) |
| [demographics-race-statewide](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/demographics-race-statewide) | Retired | [Aida Ylanan](https://www.latimes.com/people/aida-ylanan) |
| [federal-prisons](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/federal-prisons) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [homeless-impact](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/homeless-impact) | Retired | [Jennifer Lu](https://www.latimes.com/people/jennifer-lu) |
| [hopkins](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hopkins) | [Retired](https://hub.jhu.edu/2023/02/10/coronavirus-resource-center-ending-tracking/) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [hospital-patients](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-patients) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-patients.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-patients.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [hospital-capacity](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-capacity) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [hospital-locations](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-locations) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [ice-detainees](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/ice-detainees) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [icu-capacity](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/icu-capacity) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [local-adult-detention-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/local-adult-detention-facilities) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [local-juvenile-detention-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/local-juvenile-detention-facilities) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [places](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/places) | Retired | _Et al._ |
| [probable-cases](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/probable-cases) |Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [reopening-tiers](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/reopening-tiers) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [school-reopenings](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/school-reopenings) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [skilled-nursing-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/skilled-nursing-facilities) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [skilled-nursing-totals](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/skilled-nursing-totals) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [state-prisons](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/state-prisons) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [vaccine-breakthrough-cases](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-breakthrough-cases) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-cdc-state-totals](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-cdc-state-totals) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [vaccine-doses-on-hand](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-doses-on-hand) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-progress](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-progress) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-hpi](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-hpi) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-demographics-by-county](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics-by-county) | Retired| [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-demographics-statewide](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics-statewide) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-shipped-delivered](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-shipped-delivered) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [variant-proportions-states](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-proportions-states) | Retired | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [variant-toplines-ca](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-toplines-ca) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-toplines-ca.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-toplines-ca.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [vaccine-zip-codes](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-zip-codes) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene), [Matt Stiles](https://www.latimes.com/people/matt-stiles) |

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
make -f vaccine-hpi/Makefile
```
