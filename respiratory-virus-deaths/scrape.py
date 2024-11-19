"""
Download the California Health and Human Services' respiratory deaths dataset.

Source: https://data.ca.gov/dataset/respiratory-virus-dashboard-metrics
"""
import json
import pathlib
import pandas as pd

# Pathing
THIS_DIR = pathlib.Path(__file__).parent.absolute()
DATA_DIR = THIS_DIR / "data"


def main():
    """
    Download and export as a CSV.
    """


url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=403d181e-9bc9-4e48-8e3a-efc4bc7cbd9d&limit=5&q=title:jones'  
fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())
print(response_dict)


    # Request data from URL
    url = "https://data.chhs.ca.gov/dataset/fb0e792f-0165-414d-af91-130a4309505f/resource/858a3393-7c51-4377-9167-405eb1591d97/download/outputfile.csv"
    response = re.get(url)
    response_str = response.text
    
    # Parse the response string to dataframe
    df = pd.DataFrame([row.split(',') for row in response_str.split('\r\n')])
    # Dataframe will have column names as first row
    # move them to column headers
    df.columns = df.iloc[0]  # Set the first row as column names
    df = df[1:] 
    
    # Create dataframe and clean
    df = pd.read_csv(url)
    df.columns = map(str.lower, df.columns)
    
    # Save it to the data folder
    df.to_csv(DATA_DIR / "latest.csv", index=False)


if __name__ == '__main__':
    main()
