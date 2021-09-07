"""
Download patient capacity data from the U.S. Department of Health and Human Services.
"""
import csv
import io
import pathlib
import requests
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"

# Constants
DEFAULT_LIMIT = 5000


def get(url, **kwargs):
    """
    Read data from the requested resource.
    """
    params = {}
    params.update(kwargs)

    response = requests.get(url, params=params, stream=True)
    response.raise_for_status()

    csv_stream = io.StringIO(response.text)
    return csv.DictReader(csv_stream)


def get_all(url, **kwargs):
    """
    Read data from the requested resource, paginating over all results.
    Returns a generator.
    """
    params = {}
    params.update(kwargs)
    if "offset" not in params:
        params["$offset"] = 0
    limit = params.get("limit", DEFAULT_LIMIT)
    params["$limit"] = limit

    while True:
        response = get(url, **params)

        count = 0
        for item in response:
            count += 1
            yield item

        if count < limit:
            return
        params["$offset"] += limit


def main():
    """
    Download the CSV.
    """
    results = get_all("https://healthdata.gov/resource/anag-cw7u.csv", state="CA")
    df = pd.DataFrame(results)
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == "__main__":
    main()
