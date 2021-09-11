"""
Download the CDCR's data of inmate cases and deaths at state prisons.

https://data.ca.gov/dataset/cdcr-population-covid-19-tracking/resource/5a3f496d-04be-4405-aea0-e83e26076efc
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
    url = "https://data.ca.gov/dataset/4a9a896a-e64e-48c2-bb35-5589f80e7c52/resource/5a3f496d-04be-4405-aea0-e83e26076efc/download/covid19dashboard.csv"
    df = pd.read_csv(url)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "inmates/timeseries.csv", index=False)


if __name__ == '__main__':
    main()

