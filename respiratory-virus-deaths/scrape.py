"""
Download the California Health and Human Services' respiratory deaths dataset.

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
    url = "https://data.chhs.ca.gov/dataset/fb0e792f-0165-414d-af91-130a4309505f/resource/858a3393-7c51-4377-9167-405eb1591d97/download/outputfile.csv"
    df = pd.read_csv(url)
    # Lower case the column headers, since the state likes to jack around with this for no reason
    df.columns = map(str.lower, df.columns)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
