from src.ingestion import fetch_earthquake_data
from src.preprocessing import preprocess_data
import pandas as pd

def run_pipeline():
    df_raw = fetch_earthquake_data()
    print(f"Fetched {len(df_raw)} raw records")

    df_processed = preprocess_data(df_raw)
    print(f"Processed {len(df_processed)} records")

    df_processed.to_csv("data/processed/earthquakes.csv", index=False)