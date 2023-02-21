"""
Download federal prisons numbers to add to CA's prison counts eventually
Source: https://www.bop.gov/coronavirus/
"""
import pathlib
import requests
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the government JSON file.
    """
    url = 'https://www.bop.gov/coronavirus/json/final.json'
    page = requests.get(url)
    j = page.json()

    # create df from second part with everything we need
    df1 = pd.json_normalize(j['rrcData'])
#    df2 = pd.json_normalize(j['privateData'])
    df3 = pd.json_normalize(j['bopData'])
    dfFinal = pd.concat([df1, df3])

    # create and append date column
    date = j['other'][0]['date']
    dfFinal['update_date'] = pd.to_datetime(date)

    # read in the existing file to append to
    existing = pd.read_csv(
        DATA_DIR / "latest.csv",
        parse_dates=["update_date"]
    )

    # check to see if date is already there
    if dfFinal.update_date.unique() in existing.update_date.unique():
        pass
    else:
        # if not append
        existing = pd.concat([existing, dfFinal])
        # Drop duplicates
        existing.drop_duplicates()
        # And write it out
        existing.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
