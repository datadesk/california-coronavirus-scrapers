"""
Download the California Department of Public Health's daily totals for cases and deaths at skilled-nursing-facilities

https://data.ca.gov/dataset/covid-19-skilled-nursing-facility-data/resource/13aecf46-f300-4968-960c-ad8e0e7c998d
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
    url = "https://data.chhs.ca.gov/dataset/7759311f-1aa8-4ff6-bfbb-ba8f64290ae2/resource/4676b72c-f61d-4d2e-9fc4-9536f716d0c6/download/covid19aggregatedata.csv"
    df = pd.read_csv(url)
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()

