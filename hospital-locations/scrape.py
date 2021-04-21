"""
Download hospital location data from the U.S. Department of Health and Human Services.
"""
import io
import pathlib
import requests
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the metadata endpoint and find the CSV.
    """
    url = "https://opendata.arcgis.com/datasets/9f70e309bb324d3f96c49a3ead7be776_0.csv"
    df = pd.read_csv(url, dtype={"CCN": str, "Zip_Code": str})
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == "__main__":
    main()
