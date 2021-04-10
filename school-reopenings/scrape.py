import requests,pathlib
from datetime import datetime
import pytz
import pandas as pd

data_dir = pathlib.Path(__file__).parent.absolute().joinpath('data')

def main():
    today = datetime.now(tz=pytz.utc)
    today= today.astimezone(pytz.timezone('US/Pacific'))
    now = today.strftime("%Y-%m-%d")

    query="query?f=json&returnGeometry=false&outFields=*&where=1=1"

    url_list={"districts":"https://services3.arcgis.com/uknczv4rpevve42E/arcgis/rest/services/CA_Trailer_Bill_Districts_Snapshot_Stg/FeatureServer/0/",
        "charters":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/CA_Trailer_Bill_Charter_Schools_Snapshot_Stg/FeatureServer/0/",
        "private":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/CA_Trailer_Bill_Private_Schools_Snapshot_Stg/FeatureServer/0/"}

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

# NEW LINKS AS OF 4/9/2021 - Old links below
#url_list={"districts":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/Reopening_Status_to_Districts_FGDB/FeatureServer/0/",
        #"charters":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/Join_Reopening_Status_to_Charters_FGDB/FeatureServer/0/",
        #"private":"https://services3.arcgis.com/uknczv4rpevve42E/ArcGIS/rest/services/Join_Reopening_Status_to_Private_Schools_FGDB/FeatureServer/0/"}

    