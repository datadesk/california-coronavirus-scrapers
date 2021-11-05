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
    assert df.shape[0] == 64

    # Deal with dates
    tz = pytz.timezone("America/Los_Angeles")
    today = datetime.now(tz).date()

    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)
    df.to_csv(DATA_DIR / f"{today}.csv", index=False)

    # Roll up everything
    csv_list = [i for i in DATA_DIR.glob("*.csv") if not str(i).endswith('latest.csv') and not str(i).endswith('timeseries.csv')]
    df = (
        pd.concat(pd.read_csv(c, parse_dates=["Date"],) for c in csv_list)
        .sort_values(["Date", "Location"])
        .drop_duplicates(keep="first")
    )
    df.to_csv(DATA_DIR / "timeseries.csv", index=False)


if __name__ == '__main__':
    main()
