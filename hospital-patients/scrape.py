"""
Download the California Department of Public Health's hospitilization data.

Source: https://data.ca.gov/dataset/covid-19-hospital-data1
"""
import pathlib
import pandas as pd
import requests as re

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download and export as CSV
    """
    
    # Request data from URL
    url = "https://data.chhs.ca.gov/dataset/2df3e19e-9ee4-42a6-a087-9761f82033f6/resource/47af979d-8685-4981-bced-96a6b79d3ed5/download/covid19hospitalbycounty.csv"
    headers={'User-Agent': 'Mozilla/5.0'}
    response = re.get(url, headers=headers)
    response_str = response.text
    
    # Parse the response string to dataframe
    df = pd.DataFrame([row.split(',') for row in response_str.split('\r\n')])
    # Dataframe will have column names as first row
    # move them to column headers
    df.columns = df.iloc[0]  # Set the first row as column names
    df = df[1:] 
    # lowercase headers
    df.columns = map(str.lower, df.columns)
    
    # Save it to the raw data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
