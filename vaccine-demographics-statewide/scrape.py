"""
Download the California Department of Public Health's dataset of vaccine doses administered by age, gender and race/ethnicity.

Source: https://data.ca.gov/dataset/covid-19-vaccine-progress-dashboard-data/resource/c341576f-90d2-41ec-bdb1-a4e69f40e6a3
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
    url = "https://data.chhs.ca.gov/dataset/e283ee5a-cf18-4f20-a92c-ee94a2866ccd/resource/faee36da-bd8c-40f7-96d4-d8f283a12b0a/download/covid19vaccinesadministeredbydemographics.csv"
    df = pd.read_csv(url)
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
