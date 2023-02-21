"""
Download hospital location data from the U.S. Department of Health and Human Services.
"""
import pathlib
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the metadata endpoint and find the CSV.
    
    """
  
    url = "https://opendata.arcgis.com/api/v3/datasets/05b975ad01b842e18d0b02aa655632cb_0/downloads/data?format=csv&spatialRefId=4326&where=1%3D1"
    df = pd.read_csv(url, dtype={"CCN": str, "Zip_Code": str})
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == "__main__":
    main()
