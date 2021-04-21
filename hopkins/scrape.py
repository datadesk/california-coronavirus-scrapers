"""
Download timeseries data from John Hopkins' GitHub repo.
"""
import pathlib
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download the files as a CSV.
    """
    base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series"
    file_list = [
        "time_series_covid19_confirmed_global.csv",
        "time_series_covid19_deaths_global.csv",
        "time_series_covid19_confirmed_US.csv",
        "time_series_covid19_deaths_US.csv"
    ]
    for f in file_list:
        df = pd.read_csv(f"{base_url}/{f}", thousands=",")
        df.to_csv(DATA_DIR / f, index=False)


if __name__ == '__main__':
    main()
