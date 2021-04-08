"""
Download the California Department of Public Health's dataset of vaccine doses administered by Healthy Places Index.

Source: https://data.ca.gov/dataset/covid-19-vaccine-progress-dashboard-data/resource/ab5df872-5a84-4839-9199-f0174239e4e6
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
    url = "https://data.chhs.ca.gov/dataset/e283ee5a-cf18-4f20-a92c-ee94a2866ccd/resource/22b05bf3-16e5-4b2b-a66a-6b035e0cd9f4/download/covid19vaccinesadministeredbyhpiquartile.csv"
    df = pd.read_csv(url)
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
