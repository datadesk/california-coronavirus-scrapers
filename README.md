# california-coronavirus-scrapers

The open-source web scrapers that feed the [Los Angeles Times' California coronavirus tracker](https://www.latimes.com/projects/california-coronavirus-cases-tracking-outbreak/).

## Scrapers

The scrapers are written using Python and Jupyter notebooks, scheduled and run via GitHub Actions and then archived using git.

| module                  | status                                                                                                                                                                                                                                                   | maintainer  |
|:----------------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| [bed-surges](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/bed-surges) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/bed-surges.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/bed-surges.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [cases-deaths-demographics](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-demographics) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-demographics.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-demographics.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [cases-deaths-tests](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/cases-deaths-tests) | [![C](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/cases-deaths-tests.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [homeless-impact](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/homeless-impact) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/homeless-impact.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/homeless-impact.yaml) | [Jennifer Lu](https://www.latimes.com/people/jennifer-lu) |
| [hopkins](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hopkins) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hopkins.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hopkins.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [hospital-patients](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-patients) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-patients.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-patients.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [hospital-capacity](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-capacity) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-capacity.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-capacity.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [hospital-locations](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/hospital-locations) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-locations.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/hospital-locations.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [local-adult-detention-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/local-adult-detention-facilities) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-adult-detention-facilities.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-adult-detention-facilities.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [local-juvenile-detention-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/local-juvenile-detention-facilities) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-juvenile-detention-facilities.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/local-juvenile-detention-facilities.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [reopening-tiers](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/reopening-tiers) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/reopening-tiers.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/reopening-tiers.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [school-reopenings](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/school-reopenings) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/school-reopenings.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/school-reopenings.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [skilled-nursing-facilities](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/skilled-nursing-facilities) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/skilled-nursing-facilities.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/skilled-nursing-facilities.yaml) | [Ben Welsh](https://www.latimes.com/people/ben-welsh) |
| [state-prisons](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/state-prisons) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/state-prisons.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/state-prisons.yaml) | [Iris Lee](https://www.latimes.com/people/iris-lee) |
| [vaccine-doses-on-hand](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-doses-on-hand) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-doses-on-hand.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-doses-on-hand.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-progress](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-progress) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-progress.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-hpi](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-hpi) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-hpi.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-hpi.yml)| [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-demographics](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics.yml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics.yml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-shipped-delivered](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-shipped-delivered) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-shipped-delivered.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-shipped-delivered.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [variant-proportions-states](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-proportions-states) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-shipped-delivered.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variant-proportions-states.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [variant-toplines-ca](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/variant-toplines-ca) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variants-in-ca.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/variants-in-ca.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [vaccine-zip-codes](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-zip-codes) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-zip-codes.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-zip-codes.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |
| [vaccine-zip-codes](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-zip-codes) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-zip-codes.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-zip-codes.yaml) | [Matt Stiles](https://www.latimes.com/people/matt-stiles) |
| [vaccine-demographics-by-county](https://github.com/datadesk/california-coronavirus-scrapers/tree/main/vaccine-demographics-by-county) | [![](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics-by-county.yaml/badge.svg)](https://github.com/datadesk/california-coronavirus-scrapers/actions/workflows/vaccine-demographics-by-county.yaml) | [Sean Greene](https://www.latimes.com/people/sean-greene) |

## Installation

Clone the repository and install the Python dependencies.

```zsh
pipenv install
```

Then install the Node.js dependencies.

```zsh
npm install
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
