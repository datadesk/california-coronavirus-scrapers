"""
Download the California Department of Social Services' COVID-19 Homeless Impact
Source: https://data.ca.gov/dataset/covid-19-homeless-impact
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
    url = "https://data.ca.gov/dataset/f40b9c5c-ef29-4705-9f12-8325f4fb8fc5/resource/235466b6-0eb9-4ff7-a4b4-8138f474ce83/download/homeless_impact.csv"
    df = pd.read_csv(url)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()