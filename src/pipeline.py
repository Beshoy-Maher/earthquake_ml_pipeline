from src.ingestion import fetch_earthquake_data, load_data_from_csv, validate_data
from src.preprocessing import preprocess_data
from src.train import train_model, save_model
import pandas as pd
import numpy as np

def run_pipeline():
    #Fetching data
    df_raw = fetch_earthquake_data()
    print(f"Fetched {len(df_raw)} raw records")

    #Preprocessing for data
    df_processed = preprocess_data(df_raw)
    print(f"Processed {len(df_processed)} records")

    #Saving preprocessed data
    df_processed.to_csv("data/processed/earthquakes.csv", index=False)
    print("Saved processed data to data/processed/earthquakes.csv")

    #loading data
    df = load_data_from_csv('data/processed/earthquakes.csv')
    
    #Training
    model = train_model(df)
    save_model(model, 'models/model.joblib')
