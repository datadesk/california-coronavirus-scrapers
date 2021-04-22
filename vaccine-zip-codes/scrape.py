"""
Download the California Department of Public Health's dataset of vaccines administered by ZIP code.

Source: https://data.ca.gov/dataset/covid-19-vaccine-progress-dashboard-data-by-zip-code
"""
import os
import json
import urllib.request
import pandas as pd
from datetime import datetime
import pytz
import pathlib

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"

def main():
    """
    Download the Tableau export as a CSV.
    """
    # Download the data
    url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=637687ca-18fb-413e-a179-b58efa26aca1&limit=5000'  
    fileobj = urllib.request.urlopen(url)
    response_dict = json.loads(fileobj.read())
    data = response_dict['result']['records']
    df = pd.DataFrame(data)
    # Set date
    tz = pytz.timezone("America/Los_Angeles")
    today = datetime.now(tz).date()
    data_dir = os.path.join(os.path.abspath(""), "data")
    df["date"] = today
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / f"raw/{today}.csv", index=False)
    df.to_csv(DATA_DIR / "latest.csv", index=False)

if __name__ == '__main__':
    main()
