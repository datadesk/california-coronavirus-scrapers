"""
Download the California Department of Public Health's dataset of cases, deaths and tests by county.

Source: https://data.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state1/
"""
import pathlib
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the Tableau export as a CSV.
    """
    # Download the data
    url = "https://data.chhs.ca.gov/dataset/f333528b-4d38-4814-bebb-12db1f10f535/resource/046cdd2b-31e5-4d34-9ed3-b48cdbc4be7a/download/covid19cases_test.csv"
    df = pd.read_csv(url)
    # Lower case the column headers, since the state likes to jack around with this for no reason
    df.columns = map(str.lower, df.columns)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
