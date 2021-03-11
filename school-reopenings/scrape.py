import requests,pathlib
from datetime import date
import pandas as pd

data_dir = pathlib.Path(__file__).parent.absolute().joinpath('data')

def main():
    today = date.today()
    now=today.strftime("%Y-%m-%d")

    query="query?f=json&returnGeometry=false&outFields=*&where=1=1"

    url_list={"districts":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/Reopening_Status_to_Districts_FGDB/FeatureServer/0/",
        "charters":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/Join_Reopening_Status_to_Charters_FGDB/FeatureServer/0/",
        "private":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/Join_Reopening_Status_to_Private_Schools_FGDB/FeatureServer/0/"}

    for slug, u in url_list.items():
        url = u+query
        j=requests.get(url)
        data = j.json()
        df = pd.json_normalize(data["features"])
        df.columns = df.columns.str.replace("attributes.","")
    

        df.to_csv(data_dir.joinpath(f"{slug}-{now}.csv"),index=False)
        df.to_csv(data_dir.joinpath(f"{slug}-latest.csv"),index=False)

if __name__ == "__main__":
    main()
    