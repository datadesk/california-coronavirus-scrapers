"""
Download the California Department of Public Health's dataset of cases and deaths by age, race and gender.

Source: https://data.ca.gov/dataset/covid-19-time-series-metrics-by-county-and-state/resource/4d93df07-7c4d-4583-af53-03f950fe4365
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
    url = "https://data.chhs.ca.gov/dataset/f333528b-4d38-4814-bebb-12db1f10f535/resource/e2c6a86b-d269-4ce1-b484-570353265183/download/covid19casesdemographics.csv"
    df = pd.read_csv(url)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
