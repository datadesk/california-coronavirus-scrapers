"""
Download the California Department of Public Health's dataset of probable cases.

Source: https://data.ca.gov/dataset/covid-19-probable-cases
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
    url = "https://data.chhs.ca.gov/dataset/bb31bcdf-2085-4b47-92aa-13cdd6b37435/resource/e787c00b-b22d-4a6e-9a93-7a90d2be2797/download/covid19probablecases.csv"
    df = pd.read_csv(url)
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()

