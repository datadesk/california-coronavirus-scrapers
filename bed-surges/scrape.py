"""
Download the California Department of Public Health's hospitilization data.

Source: https://data.ca.gov/dataset/covid-19-medical-surge-facilities/resource/ef6675e7-cd3a-4762-ba75-2ef78d6dc334
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
    url = "https://data.ca.gov/dataset/cbbfb307-ac91-47ec-95c0-f05684e06065/resource/ef6675e7-cd3a-4762-ba75-2ef78d6dc334/download/bed_surge.csv"
    df = pd.read_csv(url)
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / "bed-surges.csv", index=False)


if __name__ == '__main__':
    main()
