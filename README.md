The open-source web scrapers that feed the [Los Angeles Times' California coronavirus tracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/).

Processed data ready for analysis is available at [datadesk/california-coronavirus-data](https://github.com/datadesk/california-coronavirus-data).

## Scrapers

The scrapers are written using Python and Jupyter notebooks, scheduled and run via GitHub Actions and then archived using git.

| module                  | status                                                                                                                                                                                                                                                   | maintainer  |
|:----------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| [bed-surges](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/bed-surges) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/bed-surges.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/bed-surges.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [cases-deaths-demographics](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-demographics) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-demographics.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-demographics.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [cases-deaths-tests](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-tests) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [cdc-community-levels](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cdc-community-levels) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [demographics-age](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/demographics-age) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/demographics-age.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/demographics-age.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [demographics-race-by-county](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/demographics-race-by-county) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/demographics-race-by-county.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/demographics-race-by-county.yaml) | [Rahul Mukherjee](https://www.latimes.com/people/rahul-mukherjee) |
| [demographics-race-statewide](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/demographics-race-statewide) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/demographics-race-statewide.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/demographics-race-statewide.yaml) | [Aida Ylanan](https://www.latimes.com/people/aida-ylanan) |
| [federal-prisons](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/federal-prisons) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/federal-prisons.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/federal-prisons.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [homeless-impact](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/homeless-impact) | Retired | [Jennifer Lu](https://www.latimes.com/people/jennifer-lu) |
| [hopkins](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hopkins) | [Retired](https://hub.jhu.edu/2023/02/10/coronavirus-resource-center-ending-tracking/) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [hospital-patients](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-patients) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-patients.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-patients.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [hospital-capacity](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-capacity) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-capacity.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-capacity.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [hospital-locations](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-locations) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-locations.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-locations.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [ice-detainees](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/ice-detainees) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [icu-capacity](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/icu-capacity) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [local-adult-detention-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/local-adult-detention-facilities) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-adult-detention-facilities.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-adult-detention-facilities.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [local-juvenile-detention-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/local-juvenile-detention-facilities) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-juvenile-detention-facilities.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-juvenile-detention-facilities.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [places](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/places) | Retired | _Et al._ |
| [probable-cases](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/probable-cases) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/probable-cases.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/probable-cases.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [reopening-tiers](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/reopening-tiers) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [school-reopenings](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/school-reopenings) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [skilled-nursing-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/skilled-nursing-facilities) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [skilled-nursing-totals](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/skilled-nursing-totals) | Retired | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [state-prisons](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/state-prisons) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/state-prisons.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/state-prisons.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [vaccine-breakthrough-cases](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-breakthrough-cases) | [![Vaccine breakthrough cases, hospitalizations and deaths](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-breakthrough-cases.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-breakthrough-cases.yml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-cdc-state-totals](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-cdc-state-totals) | [![Vaccine CDC state totals](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-cdc-state-totals.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-cdc-state-totals.yml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [vaccine-doses-on-hand](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-doses-on-hand) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-progress](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-progress) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-hpi](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-hpi) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-hpi.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-hpi.yml)| [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-demographics-by-county](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics-by-county) | [![Vaccine demographics by county](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics-by-county.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics-by-county.yml)| [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-demographics-statewide](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics-statewide) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics-statewide.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics-statewide.yml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-shipped-delivered](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-shipped-delivered) | Retired | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [variant-proportions-states](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-proportions-states) | Retired | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [variant-toplines-ca](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-toplines-ca) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-toplines-ca.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-toplines-ca.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [vaccine-zip-codes](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-zip-codes) | [![Vaccine ZIP codes](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-zip-codes.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-zip-codes.yml) | [Sean Greene](https://www.latimes.com/people/sean-greene), [Matt Stiles](https://www.latimes.com/people/matt-stiles) |

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
