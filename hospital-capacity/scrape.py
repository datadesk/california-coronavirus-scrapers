"""
Download patient capacity data from the U.S. Department of Health and Human Services.
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
    url = "https://healthdata.gov/api/views/anag-cw7u/rows.csv?accessType=DOWNLOAD"
    r = requests.get(url)
    data = r.content.decode("utf-8")
    df = pd.read_csv(io.StringIO(data), dtype={"fips_code": str, "zip": str})
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == "__main__":
    main()
