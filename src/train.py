import pandas as pd
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pathlib import Path
import joblib

def train_model(df: pd.DataFrame) -> sk.base.BaseEstimator:
    # Prepare the data
    X = df[["latitude", "longitude", "depth"]]
    y = df["magnitude"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate the model
    score = model.score(X_test, y_test)
    print(f"Model R^2 Score: {score:.2f}")

    return model 
def save_model(model, path: str):
    joblib.dump(model,path)