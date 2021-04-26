"""
Download the status of each county according to California's tier-based reopening framework. 

Source: https://covid19.ca.gov/safer-economy/
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
    url = "https://covid19.ca.gov/countystatus.json"
    df = pd.read_json(url)
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
