import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "model"


model = joblib.load(
    MODEL_DIR / "churn_model.joblib"
)

preprocessor = joblib.load(
    MODEL_DIR / "preprocessor.joblib"
)


def predict_churn(customer_data: dict):

    input_df = pd.DataFrame([customer_data])

    transformed = preprocessor.transform(input_df)

    prediction = model.predict(transformed)[0]

    return {

        "prediction": int(prediction),

        "risk": "High Churn"
        if prediction == 1
        else "Low Churn"

    }


if __name__ == "__main__":

    sample = {

        "Recency": 95,
        "Frequency": 3,
        "Monetary": 12000,
        "Avg_Discount": 25,
        "Customer_Tier": "Silver",
        "Favorite_Category": "Fashion"

    }

    print(
        predict_churn(sample)
    )