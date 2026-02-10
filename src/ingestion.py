import requests
import pandas as pd


USGS_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"


def fetch_earthquake_data(url: str = USGS_URL) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    records = []

    for feature in data["features"]:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})
        coordinates = geometry.get("coordinates", [None, None, None])

        records.append({
            "magnitude": properties.get("mag"),
            "time": properties.get("time"),
            "place": properties.get("place"),
            "longitude": coordinates[0],
            "latitude": coordinates[1],
            "depth": coordinates[2],
        })

    df = pd.DataFrame(records)
    return df


if __name__ == "__main__":
    df = fetch_earthquake_data()
    print(df.head(5))
