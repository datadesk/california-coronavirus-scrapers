"""
Download the California Department of Public Health's list of cases and deaths at skilled-nursing-facilities

https://data.ca.gov/dataset/covid-19-skilled-nursing-facility-data/resource/264bc8a1-6648-455c-bac3-4f4f4de41cb2
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
    url = "https://data.chhs.ca.gov/dataset/7759311f-1aa8-4ff6-bfbb-ba8f64290ae2/resource/d4d68f74-9176-4969-9f07-1546d81db5a7/download/covid19datanursinghome.csv"
    df = pd.read_csv(url)
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
