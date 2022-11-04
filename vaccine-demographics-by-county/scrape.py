"""
Download the California Department of Public Health's dataset of vaccine doses administered by age, gender and race/ethnicity by county.

Source: https://data.ca.gov/dataset/covid-19-vaccine-progress-dashboard-data
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
    url = "https://data.chhs.ca.gov/dataset/e283ee5a-cf18-4f20-a92c-ee94a2866ccd/resource/71729331-2f09-4ea4-a52f-a2661972e146/download/covid19vaccinesbycountybydemographic.csv"
    df = pd.read_csv(url)
    
    # split dataframes into two because of large file size
    age_df = df[ df["demographic_category"] == "Age Group" ]
    race_df =  df[ df["demographic_category"] == "Race/Ethnicity" ]
    
    # Save it to the raw data folder
    age_df.to_csv(DATA_DIR / "latest-age-group.csv", index=False)
    race_df.to_csv(DATA_DIR / "latest-race-ethnicity.csv", index=False)


if __name__ == '__main__':
    main()
