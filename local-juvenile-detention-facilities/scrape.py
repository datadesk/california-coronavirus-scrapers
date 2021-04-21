"""
Download the BSCC's list of cases at juvenile detention facilities.

https://data.ca.gov/dataset/covid-19-in-local-juvenile-detention-facilities/resource/aa6454de-8c98-4925-8286-91cb0cf7e7b1
"""
import json
import pathlib
import urllib.request
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the data.
    
    Because the csv link changes with date, we need to use the API point. The limit is set at 500000
    to ensure we get all.
    """
    url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=aa6454de-8c98-4925-8286-91cb0cf7e7b1&limit=500000'
    with urllib.request.urlopen(url) as u:
        results = u.read()
        data = json.loads(results)
        df = pd.DataFrame.from_records(data['result']["records"])
        df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
