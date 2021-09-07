"""
Download the California Department of Public Health's dataset of vaccine doses shipped and delivered.

Source: https://data.ca.gov/dataset/covid-19-vaccine-progress-dashboard-data/resource/7538b895-bc8e-45a9-b303-94bf2f0a0b31
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
    url = "https://data.chhs.ca.gov/dataset/e283ee5a-cf18-4f20-a92c-ee94a2866ccd/resource/e2f470a2-b1e3-4dce-8d33-53b4166f8930/download/vw_derived_vax_shipped_delivered.csv"
    df = pd.read_csv(url)
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
