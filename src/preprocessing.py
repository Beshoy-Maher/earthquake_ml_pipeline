import pandas as pd


def preprocess_data(df: pd.DataFrame)->pd.DataFrame:
    df = df.copy()
    df['time'] = pd.to_datetime(df['time'], unit='ms', errors='coerce')
    df.dropna(subset=['time', 'magnitude'])

    df['hour'] = df['time'].dt.hour
    df['day'] = df['time'].dt.day
    df['day_of_week'] = df['time'].dt.weekday
    return df
#done