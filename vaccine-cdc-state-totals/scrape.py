"""
Download the CDC's dashboard of data tracking vaccination for states and territories.
"""
import pytz
import pathlib
import requests
import pandas as pd
from datetime import datetime

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the Tableau export as a CSV.
    """
    # Download the data
    url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=vaccination_data"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
    }
    request = requests.get(url, headers=headers)
    data = request.json()["vaccination_data"]

    # Convert it to a dataframe
    df = pd.DataFrame.from_dict(data)
    assert df.shape[0] == 65

    # Deal with dates
    latest_date = df["Date"].unique()[0]
    tz = pytz.timezone("America/Los_Angeles")
    today = datetime.now(tz).date()

    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)
    df.to_csv(DATA_DIR / f"{today}.csv", index=False)


if __name__ == '__main__':
    main()

